import re
import random

class SimpleChatbot:
    def __init__(self):
        self.intents = {
            "greeting": ["hello", "hi", "hey"],
            "farewell": ["bye", "goodbye", "see you"],
            "help": ["help", "support", "assist"],
            "fact": ["fact", "random fact"],
            "joke": ["joke", "funny", "laugh"],
            "quote": ["quote", "inspire", "wisdom"],
        }
        self.facts = [
            "Honey never spoils.",
            "Octopuses have three hearts.",
            "Bananas are berries, but strawberries aren't.",
            "A group of flamingos is called a 'flamboyance'."
        ]
        self.jokes = [
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't scientists trust atoms? Because they make up everything!",
        ]
        self.quotes = [
            "The best way to get started is to quit talking and begin doing. – Walt Disney",
            "Success is not in what you have, but who you are. – Bo Bennett",
        ]
        self.responses = {
            "greeting": "Hello! How can I assist you today?",
            "farewell": "Goodbye! Have a great day.",
            "help": "I'm here to help. What do you need assistance with?",
            "fact": None,
            "joke": None,
            "quote": None,
            "default": "Sorry, I didn't understand that. Can you rephrase?",
        }

    def preprocess(self, message):
        return re.sub(r'[^\w\s]', '', message.lower().strip())

    def detect_intent(self, message):
        for intent, keywords in self.intents.items():
            for keyword in keywords:
                if keyword in message:
                    return intent
        return "default"

    def generate_response(self, intent):
        if intent == "fact":
            return f"Here's a random fact: {random.choice(self.facts)}"
        if intent == "joke":
            return f"Here's a joke: {random.choice(self.jokes)}"
        if intent == "quote":
            return f"Inspirational quote: {random.choice(self.quotes)}"
        return self.responses.get(intent, self.responses["default"])

    def chat(self, message):
        clean_msg = self.preprocess(message)
        intent = self.detect_intent(clean_msg)
        response = self.generate_response(intent)
        return response
    










   