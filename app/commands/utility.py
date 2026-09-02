from datetime import datetime

def time():
    current_time = datetime.now().strftime("%I:%M:%S %p")
    return f"Current Time: {current_time}"

def date():
    current_date = datetime.now().strftime("%d-%m-%Y")
    return f"Today's Date: {current_date}"

def show_help():
    print("\nAvailable Commands")
    print("-------------------")
    print("help")
    print("version")
    print("time")
    print("date")
    print("hello")
    print("exit")