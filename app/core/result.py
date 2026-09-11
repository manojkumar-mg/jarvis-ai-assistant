class CommandResult:

    def __init__(self, success, message, data=None):
        self.success = success
        self.message = message
        self.data = data

    def __repr__(self):
        return (
            f"CommandResult("
            f"success={self.success}, "
            f"message={self.message!r}, "
            f"data={self.data!r})"
        )