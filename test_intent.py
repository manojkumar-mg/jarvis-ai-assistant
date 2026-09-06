from app.nlp.intent import detect_intent,extract_website,get_website_url

print(detect_intent("hello jarvis"))
print(detect_intent("what time is it"))
print(detect_intent("tell me today's date"))
print(detect_intent("open github"))
print(detect_intent("launch youtube"))
print(detect_intent("go to github"))


print(extract_website("open github"))
print(extract_website("please launch youtube"))
print(extract_website("please go to github"))

print(get_website_url("github"))

print(detect_intent("please launch youtube"))
print(detect_intent("go to google"))

print(extract_website("please launch youtube"))
print(extract_website("go to google"))

print(get_website_url("youtube"))
print(get_website_url("google"))

print(extract_website("hey jarvis, please open youtube for me"))


print(extract_website("HEY JARVIS, OPEN YOUTUBE!"))
print(extract_website("Open Google, please!"))
print(extract_website("LAUNCH GITHUB!!!"))




