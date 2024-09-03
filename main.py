from dependency_injector.wiring import Provide, inject
from src.pkg.application import Application
from src import internal


@inject
def main(application: Application = Provide[internal.Main.application]):
    application.execute_instruction()

# entrypoint of application

if __name__ == "__main__":
    Main = internal.Main()
    Main.wire(modules=[__name__, "src"])
    main()
