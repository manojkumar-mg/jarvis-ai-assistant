from app.core.router import route_command
from app.nlp.intent import detect_intent, extract_website, get_website_url
from app.voice.tts import speak
from app.voice.speech import listen
from app.commands.system import shutdown


class Jarvis:

    def __init__(self):
        self.name = "JARVIS"
        self.version = "0.3.0"

    def start(self):
        print("=" * 50)
        print(f"Hello, I am {self.name}")

        speak(
            f"Hello, I am {self.name}. "
            f"Version {self.version}."
        )

        print(f"Version : {self.version}")
        print("=" * 50)

        while True:
            command = listen()

            if not command:
                continue

            if not self.process_command(command):
                break

    def process_command(self, command):

        intent = detect_intent(command)

        if intent == "help":
            route_command(intent)

        elif intent == "version":
            response = f"Current version : {self.version}"
            print(response)
            speak(response)

        elif intent in ["time", "date", "greeting"]:
            response = route_command(intent)

            if response:
                print(response)
                speak(response)

        elif intent == "open_website":
            website = extract_website(command)
            url = get_website_url(website)

            if url:
                response = f"Opening {website}..."
                print(response)
                speak(response)

                route_command(intent, url)

            else:
                response = "I could not identify the website."
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