from datetime import datetime
from app.core.result import CommandResult


def time():
    current_time = datetime.now().strftime("%I:%M:%S %p")

    return CommandResult(
        True,
        f"Current Time: {current_time}"
    )


def date():
    current_date = datetime.now().strftime("%d %B %Y")

    return CommandResult(
        True,
        f"Today's Date: {current_date}"
    )


def show_help():
    message = (
        "Available Commands\n"
        "-------------------\n"
        "help\n"
        "version\n"
        "time\n"
        "date\n"
        "hello\n"
        "open <website>\n"
        "exit"
    )

    return CommandResult(True, message)