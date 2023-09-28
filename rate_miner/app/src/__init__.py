from dependency_injector import containers, providers

from rate_miner.app.src.security import EncryptionManager
from rate_miner.pkg.application import Application
from rate_miner.app.src import selector
from rate_miner.pkg.settings import EliseConfigurator


class Main(containers.DeclarativeContainer):
    _encryption_manager = providers.Singleton(EncryptionManager)
    _selector = providers.Factory(selector.Selector, )
    _application = providers.Factory(
        Application, encryption_manager=_encryption_manager
    )
