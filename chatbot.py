import json
import random
import re
from logger import log_interaction

class AdvancedChatbot:
    def __init__(self):
        with open("intents.json", "r") as file:
            self.intents = json.load(file)["intents"]

        with open("knowledge.json", "r") as file:
            self.knowledge = json.load(file)

    def match_intent(self, message):
        for intent in self.intents:
            for pattern in intent["patterns"]:
                if re.search(rf"\b{pattern}\b", message.lower()):
                    return random.choice(intent["responses"])
        return None

    def knowledge_lookup(self, message):
        for key in self.knowledge:
            if key in message.lower():
                return self.knowledge[key]
        return "Sorry, I don't have info on that yet."

    def respond(self, message):
        # Intent matching
        reply = self.match_intent(message)
        if reply:
            return reply

        # Knowledge lookup
        return self.knowledge_lookup(message)
