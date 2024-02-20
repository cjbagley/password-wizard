from abc import ABC, abstractmethod
from argparse import Namespace, _SubParsersAction


class AbstractOption(ABC):
    @abstractmethod
    def add_sub_parser(self, subparser: _SubParsersAction) -> None:
        pass

    @abstractmethod
    def execute(self, args: Namespace) -> int:
        pass
