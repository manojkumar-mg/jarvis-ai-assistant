from datetime import datetime

def time():
    current_time=datetime.now().strftime("%I:%M:%S %p")
    print(f"current Time: {current_time}")

def date():
    current_date=datetime.now().strftime("%d-%m-%y")
    print(f"Today's date: {current_date}")

def show_help():
    print("\nAvailable Commands")
    print("-------------------")
    print("help")
    print("version")
    print("time")
    print("date")
    print("hello")
    print("exit")