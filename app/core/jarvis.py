from app.core.router import route_command
from app.nlp.intent import detect_intent, extract_website, get_website_url
from app.voice.tts import speak
from app.voice.speech import listen
from app.commands.system import shutdown
from app.core.result import CommandResult

class Jarvis:

    def __init__(self):
        self.name = "JARVIS"
        self.version = "0.4.0"

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

        if intent in ["help", "time", "date", "greeting"]:
            result = route_command(intent)
            self.respond(result)

        elif intent == "version":
            result = CommandResult(
            True,
            f"Current version: {self.version}"
            )

            self.respond(result)

        elif intent == "open_website":
            website = extract_website(command)
            url = get_website_url(website)

            if url:
                result = route_command(intent, url)
                self.respond(result)

            else:
                result = CommandResult(
                False,
                "I could not identify the website."
                )
                self.respond(result)

        elif intent == "exit":
            result = shutdown()
            self.respond(result)
            return False

        else:
            response = "Sorry, I don't understand that command."
            print(response)
            speak(response)

        return True
    def respond(self, result):
    
            if not result:
                return
    
            if isinstance(result, CommandResult):
                print(result.message)
                speak(result.message)
            else:
                print(result)
                speak(str(result))