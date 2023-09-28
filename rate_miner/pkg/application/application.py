import sys
from abc import ABC, abstractmethod
from typing import Dict


class ApplicationProgram(ABC):
    @abstractmethod
    def run(self):
        pass


class Application:
    def __init__(self, **kwargs):
        self.instructions: Dict[str, ApplicationProgram.__subclasses__] = kwargs

    def execute_instruction(self):
        run_type = sys.argv[1]
        if run_type in self.instructions:
            self.instructions[run_type].run()
        else:
            raise ValueError("There is no such instruction..")
