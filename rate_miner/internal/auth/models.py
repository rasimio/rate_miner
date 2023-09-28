from dataclasses import dataclass


@dataclass
class RegisterBody:
    login: str
    password: str
    invite_token: str


@dataclass
class RegisteredUserInfo:
    totp_token: str


@dataclass
class RegisterResponse:
    success: bool
    info: RegisteredUserInfo


@dataclass
class LoginBody:
    login: str
    password: str
    totp: str


@dataclass
class User:
    user_id: int
    session_key: str
