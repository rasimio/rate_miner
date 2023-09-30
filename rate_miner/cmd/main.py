from dependency_injector.wiring import Provide, inject
from rate_miner.pkg.application import Application
from rate_miner import internal


@inject
def main(application: Application = Provide[internal.Main.application]):
    application.execute_instruction()


if __name__ == "__main__":
    Main = internal.Main()
    Main.wire(modules=[__name__, "rate_miner"])
    main()
