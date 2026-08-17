from datetime import datetime
from app.commands.greeting import hello
from app.commands.utility import time,date,show_help
from app.commands.system import shutdown
from app.automation.browser import open_website

class Jarvis:
    def __init__(self):
        self.name="JARVIS"
        self.version="0.2.0"

    def start(self):
    

        print("="*50)
        print(f"Hello, I am {self.name}")
        print(f"Version :{self.version}")
        print("="*50)

        while True:
            command=input("\nJarvis>").strip().lower()

            if command == "help":
                show_help()

            elif command=="version":
                print(f"current version :{self.version}")

            elif command=="time":
                time()

            elif command=="date":
                date()

            elif command=="hello":
                hello()

            elif command.startswith("open "):
                parts = command.split()

                if len(parts) > 1:
                    url = parts[1]
                    open_website(url)
                else:
                    print("Please provide a website URL.")

            elif command=="exit":
                shutdown()
            
            
            else:
                print("Sorry,I don't understand that command.")
                return True
            

      
    def show_help(self):
        print("\nAvailable commands")
        print("---------------------")
        print("help")
        print("vesion")
        print("time")
        print("date")
        print("hello")
        print("exit")

    def shutdown(self):
        print("Goodbye : shutting down JARVIS....") 