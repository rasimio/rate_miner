from dependency_injector import containers, providers

from rate_miner.pkg.security import EncryptionManager
from rate_miner.pkg.application import Application
from rate_miner.internal import selector


class Main(containers.DeclarativeContainer):
    _encryption_manager = providers.Singleton(EncryptionManager)
    _selector = providers.Factory(selector.Selector, )
    _application = providers.Factory(
        Application, encryption_manager=_encryption_manager
    )
