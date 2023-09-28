import datetime
import hashlib
import time
import uuid

import pyotp
from typing import Union
from fastapi import Header, HTTPException
from rate_miner.internal.repository.root.user import UserModel, UserTable
from rate_miner.internal.repository.root.session import SessionModel, SessionTable
from rate_miner.internal.auth import models
from rate_miner.internal.repository import Arrow
from rate_miner.pkg.clean_fastapi import Routable, get, post
from rate_miner.pkg.settings import EliseConfigurator
from rate_miner.internal.auth.models import User


class Auth(Routable):
    def __init__(self, elise: EliseConfigurator, arrow: Arrow):
        super().__init__(kernel_route="/auth")
        self.elise = elise
        self.union_access = "test"
        self.arrow = arrow
        self.user_model = UserModel()
        self.session_model = SessionModel()

    @post("/register/")
    async def register(self, data: models.RegisterBody) -> models.RegisterResponse:
        user = self.user_model.read(connection=self.arrow.connect_to_scheme(),
                                    user_login=data.login)
        if user:
            return models.RegisterResponse(
                success=False,
                info=models.RegisteredUserInfo(
                    totp_token=""
                )
            )
        token = pyotp.random_base32()
        self.user_model.create(connection=self.arrow.connect_to_scheme(),
                               user=UserTable(
                                   id=None,
                                   user_login=data.login,
                                   user_password=hashlib.sha512(data.password.encode("UTF-8")).hexdigest(),
                                   totp=self.arrow.encrypt(message=token),
                                   role_id=1,
                                   date_create=datetime.datetime.now()
                               ))
        return models.RegisterResponse(
            success=True,
            info=models.RegisteredUserInfo(
                totp_token=token
            )
        )

    @post("/login/")
    async def login(self, data: models.LoginBody):
        user = self.login_user(data=data)
        self.user_verify(user=user, data=data)
        session_key = self.register_session(user=user)
        return {"access": session_key.session_key}

    @get("/logout/")
    async def logout(self, auth: Union[str, None] = Header(default=None)):
        await self.authenticate(auth_header=auth)
        await self.delete_session(auth=auth)

    def login_user(self, data: models.LoginBody) -> UserTable:
        user = self.user_model.read(connection=self.arrow.connect_to_scheme(),
                                    user_login=data.login)
        if not user:
            raise HTTPException(status_code=405, detail="No such user registered")
        user = user[0]
        return user

    def user_verify(self, user: UserTable, data: models.LoginBody):
        self.password_verify(user=user, data=data)
        self.totp_verify(user=user, totp_code=data.totp)

    @staticmethod
    def password_verify(user: UserTable, data: models.LoginBody):
        if hashlib.sha512(
                data.password.encode("UTF-8")).hexdigest() != user.user_password:
            raise HTTPException(status_code=401, detail="invalid password")

    def totp_verify(self, user: Union[UserTable, User], totp_code: str):
        if type(user) == User:
            user: UserTable = self.user_model.read(connection=self.arrow.connect_to_scheme(),
                                                   id=user.user_id)[0]
        totp = pyotp.TOTP(self.arrow.decrypt(message=user.totp))
        if not totp.verify(totp_code):
            raise HTTPException(status_code=401, detail="invalid totp")

    async def delete_session(self, auth: Union[str, None]):
        access_token = await self.read_auth_token(auth=auth)
        self.session_model.delete(connection=self.arrow.connect_to_scheme(),
                                  session_key=access_token)

    def register_session(self, user: UserTable) -> User:
        session_key = hashlib.sha512(
            (str(int(time.time())) + uuid.uuid4().hex + str(user.id)).encode("UTF-8")).hexdigest()
        session_user = User(
            user_id=user.id,
            session_key=session_key
        )
        self.session_model.create(connection=self.arrow.connect_to_scheme(),
                                  session=SessionTable(
                                      id=None,
                                      session_key=session_key,
                                      user_id=user.id,
                                      date_create=datetime.datetime.now()
                                  ))
        return session_user

    @staticmethod
    async def read_auth_token(auth: str):
        return auth.replace("Bearer ", "")

    async def authenticate(self, auth_header: Union[str, None]) -> User:
        if not auth_header:
            raise HTTPException(status_code=401)
        access_token = await self.read_auth_token(auth=auth_header)
        user = self.session_model.read(connection=self.arrow.connect_to_scheme(),
                                       session_key=access_token)
        if not user:
            raise HTTPException(status_code=401)
        return User(
            user_id=user[0].user_id,
            session_key=access_token
        )
