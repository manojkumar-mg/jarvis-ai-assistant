from app.commands.greeting import hello
from app.commands.utility import time, date, show_help
from app.commands.system import shutdown
from app.automation.browser import open_website
from app.nlp.intent import detect_intent, extract_website, get_website_url

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

        elif intent == "time":
            time()

        elif intent == "date":
            date()

        elif intent == "greeting":
            hello()

        elif intent == "open_website":
            website = extract_website(command)
            url = get_website_url(website)

            if url:
                print(f"Opening {website}...")
                open_website(url)
            else:
                print(f"I don't have {website} configured yet.")

        elif intent == "exit":
            shutdown()
            return False
        elif intent == "unknown":
            print("Sorry, I don't understand that command.")    

        else:
            print("Sorry, I don't understand that command.")

        

        return True