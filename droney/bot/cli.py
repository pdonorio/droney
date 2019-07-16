
from . import Bot
from typing import Callable
from riposte import Riposte


class Cli(Bot):

    def setup(self) -> Riposte:
        self.app = Riposte(prompt=f"{self.name}:~$ ")
        return self.app

    def run(self) -> None:
        print("running...")
        self.app.run()

    def _command(self, func: Callable, name: str, *args, **kwargs) -> None:
        # print("func", func, name)
        # print("args", args)
        # print("kwargs", kwargs)
        self.app.command(name)(func)

    def success(self, *args, **kwargs) -> None:
        self.app.success(*args, **kwargs)
