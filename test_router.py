from app.core.router import route_command


print("Testing greeting:")
print(route_command("greeting"))

print("\nTesting time:")
print(route_command("time"))

print("\nTesting date:")
print(route_command("date"))

print("\nTesting unknown intent:")
print(route_command("unknown"))

print("\nTesting website:")
route_command("open_website", "https://www.youtube.com")