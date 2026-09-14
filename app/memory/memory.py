import json
import os


class Memory:

    def __init__(self, file_path="app/memory/memory.json"):
        self.file_path = file_path
        self.data = []

    def load(self):
        if not os.path.exists(self.file_path):
            self.data = []
            return

        with open(self.file_path, "r") as file:
            self.data = json.load(file)

    def save(self):
        with open(self.file_path, "w") as file:
            json.dump(self.data, file, indent=4)

    def add(self, item):
        self.data.append(item)
        self.save()

    def clear(self):
        self.data = []
        self.save()

    def get_recent(self, limit=5):
        return self.data[-limit:]

    def search(self, keyword):
        keyword = keyword.lower()

        results = []

        for item in self.data:
            command = item.get("command", "").lower()

            if keyword in command:
                results.append(item)

        return results

    def find(self, keyword):
        results = self.search(keyword)

        if not results:
            return None

        return results