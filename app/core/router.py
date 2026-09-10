from app.commands.utility import time, date, show_help
from app.commands.greeting import hello
from app.automation.browser import open_website


commands = {
    "time": time,
    "date": date,
    "greeting": hello,
    "help": show_help,
    "open_website": open_website
}


def route_command(intent, *args):
    handler = commands.get(intent)

    if not handler:
        return None

    return handler(*args)