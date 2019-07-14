
from . import Bot
from riposte import Riposte


class Cli(Bot):

    def setup(self):
        self.app = Riposte(prompt=f"{self.name}:~$ ")
        return self.app

    def run(self):
        print("running...")
        self.app.run()

    def _command(self, func, name, *args, **kwargs):
        print("func", func, name)
        # print("args", args)
        # print("kwargs", kwargs)
        self.app.command(name)(func)

    def success(self, *args, **kwargs):
        self.app.success(*args, **kwargs)
