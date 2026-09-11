import webbrowser
from app.core.result import CommandResult


def open_website(url):
    try:
        opened = webbrowser.open(url)

        if opened:
            return CommandResult(
                True,
                f"Website opened successfully.",
                {"url": url}
            )

        return CommandResult(
            False,
            "I couldn't open the website.",
            {"url": url}
        )

    except Exception as e:
        return CommandResult(
            False,
            "Something went wrong while opening the website.",
            {
                "url": url,
                "error": str(e)
            }
        )