import string


websites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "reddit": "https://www.reddit.com",
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "linkedin": "https://www.linkedin.com",
    "whatsapp": "https://web.whatsapp.com",
    "amazon": "https://www.amazon.in"
}


intent_phrases = {
    "greeting": [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ],

    "time": [
        "time",
        "current hour",
        "what time is it",
        "tell me the time"
    ],

    "date": [
        "date",
        "today's date",
        "current date",
        "what date is it"
    ],
    "help": [
        "help"
    ],
    "version": [
        "version",
        "what version are you",
        "which version are you",
        "tell me your version"
    ]
}


intent_priority = [
    "open_website",
    "time",
    "date",
    "help",
    "version",
    "exit",
    "greeting"
]


def normalize_command(command):
    for punctuation in string.punctuation:
        command = command.replace(punctuation, " ")

    command = command.lower()

    return command


def detect_intent(command):
    command = normalize_command(command)
    words = command.split()

    matched_intents = []

    for intent, phrases in intent_phrases.items():
        if any(phrase in command for phrase in phrases):
            matched_intents.append(intent)

    if "open" in words or "launch" in words or "go to" in command:
        matched_intents.append("open_website")

    if "exit" in words or "quit" in words or "goodbye" in words:
        matched_intents.append("exit")

    for intent in intent_priority:
        if intent in matched_intents:
            return intent

    return "unknown"


def extract_website(command):
    command_lower = command.lower().strip()

    if "https://" in command_lower:
        start = command_lower.index("https://")
        return command[start:].split()[0].rstrip(".,!?")

    if "http://" in command_lower:
        start = command_lower.index("http://")
        return command[start:].split()[0].rstrip(".,!?")

    command = normalize_command(command)
    words = command.split()

    filler_words = ["the", "website", "site"]

    if "open" in words:
        index = words.index("open")

        for word in words[index + 1:]:
            if word not in filler_words:
                return word

    if "launch" in words:
        index = words.index("launch")

        for word in words[index + 1:]:
            if word not in filler_words:
                return word

    if "go" in words and "to" in words:
        index = words.index("go")

        if index + 2 < len(words):
            return words[index + 2]

    return None

def get_website_url(website):
    if not website:
        return None

    if website.startswith("http://") or website.startswith("https://"):
        return website

    if website in websites:
        return websites[website]

    if "." in website:
        return f"https://{website}"

    return f"https://www.{website}.com"