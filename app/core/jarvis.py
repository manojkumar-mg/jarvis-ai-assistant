from app.utils.logger import logger 

class Jarvis:
    def __init__(self):
        self.name="JARVIS"
        self.version="0.2.0"

    def start(self):
        logger.info("Jarvis has started")

        print("="*50)
        print(f"Hello, I am {self.name}")
        print("Your AI Assistent is now online.")
        print(f"Version :{self.version}")
        print("="*50)