import os
from getpass import getpass

from src.pkg.application import ApplicationProgram
from src.pkg.encryption_shield import Shield


class EncryptionManager(ApplicationProgram):
    def __init__(self):
        self.encryption_key: str = ""

    def run(self):
        os.system("cls" if os.name == "nt" else "clear")
        self.encryption_key = getpass(prompt="Enter encryption key: ")
        while True:
            self.algo()

    def algo(self):
        action = self.recognize_action()
        if action == 1:
            print(
                "Here is a cipher: ",
                Shield.encrypt_by_key(
                    key=self.encryption_key,
                    message=input("Please, enter the target message: "),
                ),
            )
        elif action == 2:
            print(
                "Here is a message: ",
                Shield.decrypt_by_key(
                    key=self.encryption_key,
                    message=input("Please, enter the target cipher: "),
                ),
            )
        elif action == 3:
            self.__init__()

    @staticmethod
    def recognize_action() -> int:
        input("Press enter to continue")
        os.system("cls" if os.name == "nt" else "clear")
        print("1: for encrypt")
        print("2: for decrypt")
        print("3: for change key")
        action = int(input("Select action: "))
        return action
