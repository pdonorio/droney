import typing
import importlib
from . import DEFAULT_TYPE, ALLOWED_TYPES
from .bot import Btype


def new(name: str, mode: typing.Optional[str] = None) -> Btype:

    if mode is None:
        mode = DEFAULT_TYPE

    if mode not in ALLOWED_TYPES:
        raise AttributeError(f"Invalid mode: {mode}")
    else:
        print("new", name, mode)

    module = importlib.import_module(f'droney.bot.{mode}')
    MyClass = getattr(module, mode.capitalize())
    instance = MyClass(name, mode=mode)
    instance.setup()
    return instance
