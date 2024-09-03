from dataclasses import dataclass
from multiprocessing import Lock


@dataclass
class Delay:
    step: float
    set_actual_lock: Lock
    get_actual_lock: Lock
    actual: float = 0


@dataclass
class Endpoint:
    delay: Delay
    url: str
    label: str
