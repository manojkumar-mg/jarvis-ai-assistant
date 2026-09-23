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
    ],
    "last_command": [
        "last command",
        "what was my last command",
        "what did I just say",
        "what did I say last"
    ],
    "last_intent": [
        "last intent",
        "what was my last intent",
        "what intent did you detect",
        "what was the previous intent"
    ],
    "history": [
        "history",
        "show my history",
        "show command history",
        "show my command history",
        "what commands did I use"
    ],
    "search_memory": [
        "search memory",
        "find in memory",
        "search my memory"
    ],
    "reference": [
        "is it still open",
        "is it open",
        "is that still open",
        "what about it",
        "what about that",
        "the website",
        "open that website again",
        "open it again",
        "open that again",
        "launch the same website"
    ],
    "open_last_website": [
        "go there",
        "open it",
        "open that",
        "take me there",
        "go to it",
        "take me back there",
        "open that site again",
        "go back there",
        "return to that website",
    ],
    "repeat": [
        "repeat that",
        "say that again",
        "repeat your answer",
        "what did you say",
        "say it again"
    ],

    "last_website": [
        "what website did i open",
        "which website did i open",
        "what did i open"
    ],
    "context": [
        "what did I just do",
        "what did I just open",
        "what was I doing",
        "what happened",
        "what did you just do",
        "what website did I open",
        "which site did I visit",
        "tell me what I opened",
        "what site did I open"
    ],
    "follow_up": [
        "what about that",
        "tell me more",
        "and then",
        "what next",
        "continue"
]

}


intent_priority = [
    "open_website",
    "last_website",
    "open_last_website",
    "time",
    "date",
    "help",
    "version",
    "last_command",
    "last_intent",
    "repeat",
    "follow_up",
    "reference",
    "context",
    "history",
    "search_memory",
    "exit",
    "greeting"
]

def normalize_command(command):
    for punctuation in string.punctuation:
        command = command.replace(punctuation, " ")

    command = command.lower()

    return command

def phrase_matches(command, phrase):
    command = normalize_command(command)
    phrase = normalize_command(phrase)

    command_words = command.split()
    phrase_words = phrase.split()

    phrase_length = len(phrase_words)

    for i in range(len(command_words) - phrase_length + 1):
        if command_words[i:i + phrase_length] == phrase_words:
            return True

    return False

def detect_intent(command):
    command = normalize_command(command)
    words = command.split()

    matched_intents = []

    for intent, phrases in intent_phrases.items():
        if any(phrase_matches(command, phrase) for phrase in phrases):
            matched_intents.append(intent)

    if (
        "open" in words
        and not any(
            phrase_matches(command, phrase)
            for phrase in (
                intent_phrases.get("context", [])
                + intent_phrases.get("reference", [])
                + intent_phrases.get("open_last_website", [])
            )
        )
    ):
        matched_intents.append("open_website")

    if "launch" in words or "go to" in command:
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

    filler_words = [
        "the",
        "website",
        "site",
        "please",
        "can",
        "you",
        "could",
        "would"
    ]

    if "open" in words:
        index = words.index("open")
        words = words[index + 1:]

    elif "launch" in words:
        index = words.index("launch")
        words = words[index + 1:]

    elif "go" in words and "to" in words:
        index = words.index("to")
        words = words[index + 1:]

    else:
        return None

    for word in words:
        if word not in filler_words:
            return word

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

def extract_memory_keyword(command):
    command = normalize_command(command)
    words = command.split()

    keywords = [
        "search",
        "memory",
        "find",
        "in"
    ]

    words = [word for word in words if word not in keywords]

    return " ".join(words).strip()


def split_commands(command):
    """
    Splits a multi-command sentence into individual commands.
    """

    command = command.strip()

    separators = [
        " and then ",
        " then ",
        " and "
    ]

    for separator in separators:
        if separator in command.lower():
            parts = command.lower().split(separator)

            commands = [
                part.strip()
                for part in parts
                if part.strip()
            ]

            return commands

    return [command]