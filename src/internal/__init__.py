from dependency_injector import containers, providers

from src.pkg.security import EncryptionManager
from src.pkg.application import Application
from src.internal import selector
from src.pkg.database import Postgresql
from src import config
from src.pkg import server


class Main(containers.DeclarativeContainer):
    cfg = config.load()
    psql = Postgresql(host=cfg.PostgreSQL.Host,
                      port=cfg.PostgreSQL.Port,
                      db=cfg.PostgreSQL.DB,
                      password=cfg.PostgreSQL.Password,
                      user=cfg.PostgreSQL.User)
    _encryption_manager = providers.Singleton(EncryptionManager)
    _selector = providers.Factory(selector.Selector)
    server = providers.Factory(server.ServerAPI,
                               port=cfg.Server.Port,
                               host=cfg.Server.Host,
                               selector=_selector)
    application = providers.Factory(
        Application, server=server,
    )
