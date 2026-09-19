from app.nlp.intent import split_commands


test_commands = [
    "open youtube and tell me the time",
    "open github then tell me the date",
    "hello",
    "open youtube"
]

for command in test_commands:
    print(f"\nInput: {command}")
    print("Output:", split_commands(command))
    