
import importlib


def new(name, mode=None):
    if mode is None:
        mode = 'cli'
    print("new", name, mode)

    module = importlib.import_module(f'droney.bot.{mode}')
    MyClass = getattr(module, mode.capitalize())
    instance = MyClass(name, mode=mode)
    instance.setup()
    return instance
