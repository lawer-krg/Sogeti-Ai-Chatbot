import re
import random
import spacy
from transformers import pipeline

class NLPChatbot:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.intent_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        self.candidate_intents = [
            "greeting", "farewell", "help", "fact", "joke", "quote", "weather", "small talk"
        ]
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

    def extract_entities(self, message):
        doc = self.nlp(message)
        return [(ent.text, ent.label_) for ent in doc.ents]

    def detect_intent(self, message):
        classification = self.intent_classifier(
            message, self.candidate_intents
        )
        intent = classification["labels"][0] if classification["scores"][0] > 0.5 else "default"
        return intent

    def generate_response(self, intent):
        if intent == "fact":
            return f"Here's a random fact: {random.choice(self.facts)}"
        if intent == "joke":
            return f"Here's a joke: {random.choice(self.jokes)}"
        if intent == "quote":
            return f"Inspirational quote: {random.choice(self.quotes)}"
        return self.responses.get(intent, self.responses["default"])

    def chat(self, message):
        entities = self.extract_entities(message)
        intent = self.detect_intent(message)
        response = self.generate_response(intent)
        return {
            "response": response,
            "entities": entities,
            "intent": intent
        }