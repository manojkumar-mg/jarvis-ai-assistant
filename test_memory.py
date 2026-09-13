from app.core.jarvis import Jarvis

jarvis = Jarvis()

commands = [
    "hello",
    "what time is it",
    "open youtube",
    "what was my last command",
    "what was my last intent",
    "history"
]

for command in commands:
    print(f"\n>>> {command}")
    jarvis.process_command(command)