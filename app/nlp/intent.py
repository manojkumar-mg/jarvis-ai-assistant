def detect_intent(command):
    if "hello" in command or "hi" in command or "hey" in command:
        return "greeting"

    elif "time" in command :
        return "time"

    elif "date" in command:
        return "date"