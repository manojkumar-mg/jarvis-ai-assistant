import json
import os


class Memory:

    def __init__(self, file_path="app/memory/memory.json"):
        self.file_path = file_path
        self.data = []
        self.facts = {}

    def load(self):
        if not os.path.exists(self.file_path):
            self.data = []
            self.facts = {}
            return

        with open(self.file_path, "r") as file:
            stored_data = json.load(file)

        # Support existing memory.json format
        if isinstance(stored_data, list):
            self.data = stored_data
            self.facts = {}

        elif isinstance(stored_data, dict):
            self.data = stored_data.get("commands", [])
            self.facts = stored_data.get("facts", {})

    def save(self):
        with open(self.file_path, "w") as file:
            json.dump(
                {
                    "commands": self.data,
                    "facts": self.facts
                },
                file,
                indent=4
            )

    def add(self, item):
        self.data.append(item)
        self.save()

    def add_fact(self, key, value):
        self.facts[key.lower()] = value
        self.save()

    def get_fact(self, key):
        return self.facts.get(key.lower())

    def clear(self):
        self.data = []
        self.facts = {}
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