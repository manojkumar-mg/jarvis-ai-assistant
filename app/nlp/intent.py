websites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com"
}


def detect_intent(command):
    words = command.split()

    if "hello" in words or "hi" in words or "hey" in words:
        return "greeting"

    elif "time" in words:
        return "time"

    elif "date" in words:
        return "date"

    elif "open" in words or "launch" in words or "go to" in command:
        return "open_website"

    return "unknown"


def extract_website(command):
    words = command.split()

    if "open" in words:
        index = words.index("open")
        website = words[index + 1]

    elif "launch" in words:
        index = words.index("launch")
        website = words[index + 1]

    elif "go to" in command:
        index = words.index("go")
        website = words[index + 2]

    return website


def get_website_url(website):
    return websites[website]