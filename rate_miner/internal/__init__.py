from dependency_injector import containers, providers

from rate_miner.pkg.security import EncryptionManager
from rate_miner.pkg.application import Application
from rate_miner.internal import selector
from rate_miner.pkg.database import Postgresql
from rate_miner import config
from rate_miner.pkg import server


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
