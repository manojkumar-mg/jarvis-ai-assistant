from app.core.router import route_command
from app.nlp.intent import detect_intent, extract_website, get_website_url, extract_memory_keyword,split_commands
from app.voice.tts import speak
from app.voice.speech import listen
from app.commands.system import shutdown
from app.core.result import CommandResult
from app.memory.memory import Memory

meta_intents = [
    "last_command",
    "last_intent",
    "context",
    "history",
    "search_memory",
    "reference",
    "repeat"
]

class Jarvis:

    def __init__(self):
        self.name = "JARVIS"
        self.version = "0.4.0"

        self.memory = Memory()
        self.memory.load()

        self.command_history = self.memory.data.copy()

        self.last_command = None
        self.last_intent = None
        self.last_response = None

        self.context = {
            "last_action": None,
            "last_website": None
        }

        if self.command_history:
            for item in reversed(self.command_history):

                if item["intent"] in meta_intents:
                    continue

                self.last_command = item["command"]
                self.last_intent = item["intent"]
                self.context["last_action"] = item["command"]

                if item["intent"] == "open_website":
                    data = item.get("data")

                    if data:
                        self.context["last_website"] = data.get("url")

                break

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

            if command:
                commands = split_commands(command)

                for individual_command in commands:
                    self.process_command(individual_command)

                    if detect_intent(individual_command) == "exit":
                        return      
   

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

                command = self.last_command

                result = CommandResult(
                        True,
                        f"You last asked me to: {command}."
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

        elif intent == "search_memory":
            keyword = extract_memory_keyword(command)
            results = self.memory.search(keyword)

            if results:
                history_text = "Memory Search Results:\n"

                for index, item in enumerate(results, start=1):
                    history_text += (
                        f"{index}. {item['command']} "
                        f"| Intent: {item['intent']} "
                        f"| Status: {'Success' if item['success'] else 'Failed'}\n"
                        )

                result = CommandResult(
                    True,
                    history_text,
                    results
                )
            else:
                result = CommandResult(
                False,
                f"I couldn't find anything related to {keyword}."
                )

            self.respond(result)

        elif intent == "context":

            if self.last_command:

                result = CommandResult(
                    True,
                    self.get_action_summary()
                )

            else:

                result = CommandResult(
                    False,
                    "I don't have any recent action in my context."
            )

            self.respond(result)
        elif intent == "reference":

            if self.context["last_website"]:

                website = self.context["last_website"]

                website = website.replace("https://www.", "")
                website = website.replace("https://", "")
                website = website.replace("http://www.", "")
                website = website.replace("http://", "")
                website = website.split(".")[0]

                result = CommandResult(
                True,
                f"You're referring to {website.capitalize()}."
                )

            elif self.context["last_action"]:

                result = CommandResult(
                True,
                f"You're referring to your last action: {self.context['last_action']}"
                )

            else:

                result = CommandResult(
                False,
                "I don't have enough context to know what you're referring to."
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

        elif intent == "last_website":

            website_url = self.context["last_website"]

            if website_url:

                website = website_url.replace("https://www.", "")
                website = website.replace("https://", "")
                website = website.replace("http://www.", "")
                website = website.replace("http://", "")
                website = website.split(".")[0]

                result = CommandResult(
                    True,
                    f"The last website you opened was {website.capitalize()}."
                )

            else:

                result = CommandResult(
                    False,
                    "I don't have a recently opened website."
                )

            self.respond(result)

        elif intent == "repeat":

            if self.last_response:

                result = CommandResult(
                True,
                self.last_response
            )

            else:

                result = CommandResult(
                        False,
                        "I don't have anything to repeat yet."
                    )

            self.respond(result)


        elif intent == "open_last_website":

            website_url = self.context["last_website"]

            if website_url:
                result = route_command("open_website", website_url)
                self.respond(result)
            else:
                result = CommandResult(
                    False,
                    "I don't have a recently opened website."
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


        if intent not in meta_intents:
            self.last_command = command
            self.last_intent = intent
            self.context["last_action"] = command

            if intent == "open_website":
                self.context["last_website"] = result.data.get("url") if result.data else None


        self.command_history.append({
            "command": command,
            "intent": intent,
            "success": result.success if result else False,
            "response": result.message if result else "",
            "data": result.data if result else None
        })

        self.memory.add({
            "command": command,
            "intent": intent,
            "success": result.success if result else False,
            "response": result.message if result else "",
            "data": result.data if result else None
        })
        return True

    def get_action_summary(self):

        if self.last_intent == "time":
            return "You just checked the time."

        elif self.last_intent == "date":
            return "You just checked the date."

        elif self.last_intent == "greeting":
            return "You just greeted me."


        elif self.last_intent == "open_last_website":
            website = self.context["last_website"]

            if website:
                website = website.replace("https://www.", "")
                website = website.replace("https://", "")
                website = website.replace("http://www.", "")
                website = website.replace("http://", "")
                website = website.split(".")[0]

                display_names = {
                    "github": "GitHub",
                    "youtube": "YouTube",
                    "linkedin": "LinkedIn",
                    "whatsapp": "WhatsApp",
                    "instagram": "Instagram",
                    "facebook": "Facebook",
                    "reddit": "Reddit",
                    "google": "Google",
                    "amazon": "Amazon"
                }

                website_name = display_names.get(
                    website.lower(),
                    website.capitalize()
                )

                return f"You just reopened {website_name}."

        elif self.last_intent == "open_website":

            website = self.context["last_website"]

            if website:
                website = website.replace("https://www.", "")
                website = website.replace("https://", "")
                website = website.replace("http://www.", "")
                website = website.replace("http://", "")
                website = website.split(".")[0]

                display_names = {
                        "github": "GitHub",
                        "youtube": "YouTube",
                        "linkedin": "LinkedIn",
                        "whatsapp": "WhatsApp",
                        "instagram": "Instagram",
                        "facebook": "Facebook",
                        "reddit": "Reddit",
                        "google": "Google",
                        "amazon": "Amazon"
                        }

                website_name = display_names.get(
                        website.lower(),
                        website.capitalize()
                    )

                return f"You just opened {website_name}."



            if self.last_command:
                return f"You recently executed: {self.last_command}."

        return "I don't have a recent action to summarize."
    
    def respond(self, result):
            self.last_response = result.message
    
            if not result:
                return
    
            if isinstance(result, CommandResult):
                
                print(result.message)
                speak(result.message)
            else:
                print(result)
                speak(str(result))