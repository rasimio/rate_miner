from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken


class Shield:
    @staticmethod
    def generate_key() -> bytes:
        key = Fernet.generate_key()
        return key

    @staticmethod
    def decrypt_by_key(key: str, message: str) -> str:
        f = Fernet(key=key)
        decrypted_message = f.decrypt(message.encode())
        return decrypted_message.decode()

    @staticmethod
    def encrypt_by_key(key: str, message: str) -> str:
        f = Fernet(key=key)
        encrypted_message = f.encrypt(message.encode())
        return encrypted_message.decode()
