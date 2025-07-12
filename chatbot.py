from nlu import interpret
from dialogue_manager import DialogueManager
from response_generator import generate_response

dm = DialogueManager()

def chat():
    print("🤖 Hello! I'm your assistant. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("🤖 Goodbye!")
            break

        intent, entities = interpret(user_input)
        action = dm.decide(intent, entities)
        response = generate_response(action, entities)
        print(f"🤖 {response}")

if __name__ == "__main__":
    chat()
import re

def interpret(text):
    text = text.lower()
    if "weather" in text:
        return "get_weather", {}
    elif "name" in text:
        return "get_name", {}
    elif "joke" in text:
        return "tell_joke", {}
    else:
        return "unknown", {}
class DialogueManager:
    def __init__(self):
        self.context = {}

    def decide(self, intent, entities):
        if intent == "get_weather":
            return "fetch_weather"
        elif intent == "get_name":
            return "ask_name"
        elif intent == "tell_joke":
            return "tell_joke"
        else:
            return "fallback"
import random

def generate_response(action, entities):
    if action == "fetch_weather":
        return "It's sunny and 28°C outside."
    elif action == "ask_name":
        return "I'm ChatBot 3000. What's your name?"
    elif action == "tell_joke":
        return random.choice([
            "Why did the computer show up late? It had a hard drive!",
            "I would tell you a UDP joke, but you might not get it."
        ])
    else:
        return "I'm not sure how to respond to that."




