
def test_usage():
    from droney import app

    bot = app.new(name='test')

    @bot.command('example')
    def name():
        msg = "It's working"
        print(msg)
        return msg

    # bot.run()
