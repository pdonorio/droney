
from abc import ABC, abstractmethod
from typing import Callable, Optional, TypeVar


class Bot(ABC):

    def __init__(self, name: str, mode: Optional[str]=None):
        # super(Bot, self).__init__()
        self.name = name
        self.mode = mode

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def _command(self, func: Callable, name, *args, **kwargs):
        pass

    def command(self, name: str, *args, **kwargs) -> Callable:
        def wrapper(func: Callable) -> Callable:
            # print("args", args)
            # print("kwargs", kwargs)
            # print("magic", func)
            self._command(func, name, *args, **kwargs)
            return func

        # NOTE: code here is executed before wrapper :)
        # print("TEST")
        return wrapper


Btype = TypeVar('Btype', bound=Bot)
