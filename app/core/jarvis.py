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

        self.last_command = None
        self.last_intent = None
        self.command_history = []


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
        result = None
    

        if intent in ["help", "time", "date", "greeting"]:
            result = route_command(intent)
            self.respond(result)

        elif intent == "version":
            result = CommandResult(
            True,
            f"Current version: {self.version}"
            )

            self.respond(result)

        elif intent == "last_command":
            if self.last_command:
                result = CommandResult(
                True,
                f"Your last command was: {self.last_command}"
                )
            else:
                result = CommandResult(
                False,
                "I don't have a previous command yet."
            )

            self.respond(result)

        elif intent == "last_intent":
            if self.last_intent:
                result = CommandResult(
                True,
                f"Your last intent was: {self.last_intent}"
                )
            else:
                result = CommandResult(
                False,
                "I don't have a previous intent yet."
            )

            self.respond(result)

        elif intent == "history":
            if self.command_history:
                history_text = "Command History:\n"

                for index, item in enumerate(self.command_history, start=1):
                    status = "Success" if item["success"] else "Failed"

                    history_text += (
                        f"{index}. {item['command']} "
                        f"| Intent: {item['intent']} "
                        f"| Status: {status}\n"
                        )

                result = CommandResult(
                    True,
                    history_text
                    )
            else:
                result = CommandResult(
                False,
                "There is no command history yet."
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
            result = CommandResult(
            False,
            "Sorry, I don't understand that command."
            )
            self.respond(result)

        self.last_command = command
        self.last_intent = intent

        self.command_history.append({
            "command": command,
            "intent": intent,
            "success": result.success if result else False,
            "response": result.message if result else ""
        })
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