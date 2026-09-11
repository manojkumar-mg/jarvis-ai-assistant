from app.core.result import CommandResult


def shutdown():
    return CommandResult(
        True,
        "Goodbye. Shutting down JARVIS..."
    )