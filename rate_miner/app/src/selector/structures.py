from dataclasses import dataclass


@dataclass
class WithdrawBody:
    wallet_number: str
    middle_name: str
    first_name: str
    amount_usd: float
    receive_place_code: str
    totp_token: str


@dataclass
class CalcAmountBody:
    amount_usd: float


@dataclass
class WalletBalanceBody:
    wallet_number: str


@dataclass
class FindBody:
    tx_id: str


@dataclass
class WalletUpdate:
    wallet_number: str
    status: str


@dataclass
class WalletCreateBody:
    wallet_number: str
    token: str
