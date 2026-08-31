from app.voice.speech import listen
from app.core.jarvis import Jarvis


assistant = Jarvis()

command = listen()

if command:
    assistant.process_command(command)