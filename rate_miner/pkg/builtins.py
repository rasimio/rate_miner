from dataclasses import dataclass
from typing import Optional


@dataclass
class Result:
    err: Optional[Exception]
