from app.commands.utility import time, date, show_help
from app.commands.greeting import hello

commands = {
    "time": time,
    "date": date,
    "greeting": hello,
    "help": show_help
}

def route_command(intent):
    handler = commands.get(intent)

    if handler:
        return handler()

    return None