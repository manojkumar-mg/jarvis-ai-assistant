from app.commands.greeting import hello
from app.commands.utility import time, date, show_help
from app.commands.system import shutdown
from app.automation.browser import open_website
from app.nlp.intent import detect_intent

class Jarvis:

    def __init__(self):
        self.name = "JARVIS"
        self.version = "0.2.0"

    def start(self):
        print("=" * 50)
        print(f"Hello, I am {self.name}")
        print(f"Version : {self.version}")
        print("=" * 50)

        while True:
            command = input("\nJarvis>").strip().lower()

            if not self.process_command(command):
                break

    def process_command(self, command):

        intent = detect_intent(command)

        if command == "help":
            show_help()

        elif command == "version":
            print(f"Current version : {self.version}")

        elif command == "time":
            time()

        elif command == "date":
            date()

        elif intent == "greeting":
            hello()

        elif command == "open" or command.startswith("open "):
            parts = command.split()

            if len(parts) > 1:
                url = parts[1]
                open_website(url)
            else:
                print("Please provide a website URL.")

        elif command == "exit":
            shutdown()
            return False

        else:
            print("Sorry, I don't understand that command.")

        return True