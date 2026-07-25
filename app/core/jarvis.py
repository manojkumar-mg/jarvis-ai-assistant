from datetime import datetime

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
                self.show_help()

            elif command=="version":
                print(f"current version :{self.version}")

            elif command=="time":
                current_time=datetime.now().strftime("%I:%M:%S %p")
                print(f"current Time: {current_time}")

            elif command=="date":
                current_date=datetime.now().strftime("%d-%m-%y")
                print(f"Today's date: {current_date}")

            elif command=="hello":
                print("Hello how can I help you?")

            elif command=="exit":
                self.shutdown()
                return False
            
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