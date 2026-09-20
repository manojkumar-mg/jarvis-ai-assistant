from app.nlp.intent import detect_intent

test_commands = [
    "what website did I open",
    "which website did I open",
    "what did I open"
]

for command in test_commands:
    print(f"{command} -> {detect_intent(command)}")