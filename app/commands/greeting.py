from app.core.result import CommandResult


def hello():
    return CommandResult(
        True,
        "Hello! How can I help you?"
    )