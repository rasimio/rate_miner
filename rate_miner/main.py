from dependency_injector.wiring import Provide, inject
import app
from app import src
from pkg.application import Application


@inject
def main(application: Application = Provide[app.src.Main.application]):
    application.execute_instruction()


if __name__ == "__main__":
    Main = app.src.Main()
    Main.wire(modules=[__name__, "app"])
    main()
