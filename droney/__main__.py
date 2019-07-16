
from droney import app
from droney.bot.cli import Cli  # noqa

bot = app.new(name='example', mode='cli')  # type: Cli


@bot.command("add")
def add(x: int, y: int) -> None:
    result = f"{x} + {y} = {x + y}"
    bot.success(result)


bot.run()
