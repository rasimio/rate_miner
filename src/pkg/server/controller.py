from typing import Dict

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.pkg.application import ApplicationProgram
from src.pkg.clean_fastapi.routable import Routable


class ServerAPI(ApplicationProgram):
    def __init__(self, port: int, host: str, **servers):
        self.app = FastAPI()
        self.port = port
        self.host = host
        self.servers: Dict[str, Routable.__subclasses__] = servers
        self.server_initialize()
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def server_initialize(self):
        for k, v in self.servers.items():
            self.app.include_router(v.router)

    def run(self):
        uvicorn.run(self.app, host=self.host, port=self.port)
