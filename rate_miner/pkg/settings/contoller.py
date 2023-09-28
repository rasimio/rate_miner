from typing import Dict

from dotenv import load_dotenv


class EliseConfigurator:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.wallets: Dict = {}
        self.load()

    @staticmethod
    def load():
        load_dotenv(verbose=True)
