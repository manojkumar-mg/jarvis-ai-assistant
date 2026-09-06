import string


websites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com"
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
    ]
}


intent_priority = [
    "open_website",
    "time",
    "date",
    "exit",
    "greeting"
]


def normalize_command(command):
    for punctuation in string.punctuation:
        command = command.replace(punctuation, "")

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
    command = normalize_command(command)
    words = command.split()

    filler_words = ["the", "website", "site"]

    if "open" in words:
        index = words.index("open")

        for word in words[index + 1:]:
            if word not in filler_words:
                return word

    elif "launch" in words:
        index = words.index("launch")

        for word in words[index + 1:]:
            if word not in filler_words:
                return word

    return None


def get_website_url(website):
    return websites.get(website)