
from abc import ABC, abstractmethod


class Bot(ABC):

    def __init__(self, name, mode=None):
        super(Bot, self).__init__()
        self.name = name
        self.mode = mode

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def _command(self, func, name, *args, **kwargs):
        pass

    def command(self, name, *args, **kwargs):
        def wrapper(func):
            # print("args", args)
            # print("kwargs", kwargs)
            # print("magic", func)
            self._command(func, name, *args, **kwargs)
            return func

        # NOTE: code here is executed before wrapper :)
        # print("TEST")
        return wrapper
