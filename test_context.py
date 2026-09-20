from app.core.jarvis import Jarvis

assistant = Jarvis()

print("\n--- Opening YouTube ---")
assistant.process_command("open youtube")

print("\n--- Opening GitHub ---")
assistant.process_command("open github")

print("\n--- Opening It Again ---")
assistant.process_command("open it again")