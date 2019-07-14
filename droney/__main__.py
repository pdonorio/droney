
from droney import app

bot = app.new(name='paolo')


@bot.command("add")
def add(x: int, y: int):
    result = f"{x} + {y} = {x + y}"
    bot.success(result)


bot.run()
