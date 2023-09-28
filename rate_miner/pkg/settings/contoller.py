from typing import Dict

from dotenv import load_dotenv


class EliseConfigurator:
    def __init__(self):
        self.load()

    @staticmethod
    def load():
        load_dotenv(verbose=True)
