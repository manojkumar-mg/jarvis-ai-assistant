from app.core.jarvis import Jarvis

assistant = Jarvis()

print("\n--- Opening GitHub ---")
assistant.process_command("open github")

print("\n--- Asking Last Command ---")
assistant.process_command("what was my last command")