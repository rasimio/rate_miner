from dataclasses import dataclass


@dataclass
class EncryptionKeyBody:
    key: str
    signature: str
    time_stamp: str
