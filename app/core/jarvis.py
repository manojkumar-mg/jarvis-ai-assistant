from app.commands.greeting import hello
from app.commands.utility import time, date, show_help
from app.commands.system import shutdown
from app.automation.browser import open_website
from app.nlp.intent import detect_intent, extract_website, get_website_url
from app.voice.tts import speak
from app.voice.speech import listen

class Jarvis:

    def __init__(self):
        self.name = "JARVIS"
        self.version = "0.2.0"

    def start(self):
        print("=" * 50)
        print(f"Hello, I am {self.name}")
        print(f"Version : {self.version}")
        speak(f"Hello, I am {self.name}. Version {self.version}.")
        print("=" * 50)

        while True:
            command = listen()

            if not command:
                continue

            if not self.process_command(command):
                break

    def process_command(self, command):

        intent = detect_intent(command)

        if command == "help":
            show_help()

        elif command == "version":
            response = f"Current version : {self.version}"
            print(response)
            speak(response)

        elif intent == "time":
            response = time()
            print(response)
            speak(response)

        elif intent == "date":
            response = date()
            print(response)
            speak(response)

        elif intent == "greeting":
            response = hello()
            print(response)
            speak(response)

        elif intent == "open_website":
            website = extract_website(command)
            url = get_website_url(website)

            if url:
                response = f"Opening {website}..."
                print(response)
                speak(response)
                open_website(url)

            else:
                response = f"I don't have {website} configured yet."
                print(response)
                speak(response)

        elif intent == "exit":
            response = shutdown()
            print(response)
            speak(response)
            return False

        else:
            response = "Sorry, I don't understand that command."
            print(response)
            speak(response)

        return True