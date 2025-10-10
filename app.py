from flask import Flask, render_template, request
from datetime import datetime
import re
import random

app = Flask(__name__)

# --- Language detection placeholder ---
def get_language(msg):
    return "en"  # Always English for simplicity

# --- Responses database ---
RESPONSES = {
    "en": {
        "hi": [
            "Hello! 👋 I can chat about IT, cricket, grammar, food, math, or just say hi. What would you like to do?",
            "Hi there! 😊 Ask me anything about IT, cricket, grammar, food, or math!",
            "Hey! 👋 I'm ChatBuddy 🤖 — your friendly helper for tech, cricket, and fun topics."
        ],
        "how_are_you": [
            "I'm doing great, thanks! 😊 How about you?",
            "All good here! How are you feeling today?",
            "I'm fine and ready to chat!"
        ],
        "name": [
            "I'm ChatBuddy 🤖, your friendly assistant.",
            "You can call me ChatBuddy!",
            "ChatBuddy at your service!"
        ],
        "bye": [
            "Goodbye! Have a great day! 👋",
            "See you later! Stay awesome!",
            "Bye! Come back soon!"
        ],
        "help": [
            "I can chat about IT, cricket, grammar, food, math, or just say hi! What would you like to talk about?"
        ]
    }
}


# --- Chatbot Logic ---
def chatbot_reply(message):
    msg = message.lower().strip()
    lang = get_language(msg)
    res = RESPONSES.get(lang, RESPONSES["en"])

    # --- Greetings ---
    if any(word in msg for word in ["hi", "hello", "hey", "hola", "salut"]):
        return random.choice(res["hi"])
    elif any(phrase in msg for phrase in ["how are you", "how r u", "cómo estás", "ça va"]):
        return random.choice(res["how_are_you"])
    elif any(phrase in msg for phrase in ["your name", "nombre", "ton nom"]):
        return random.choice(res["name"])
    elif any(word in msg for word in ["bye", "adios", "au revoir"]):
        return random.choice(res["bye"])
    elif any(word in msg for word in ["help", "ayuda", "aide"]):
        return random.choice(res["help"])

    # --- Time & Date ---
    elif any(word in msg for word in ["time", "hora", "heure"]):
        return "⏰ The current time is " + datetime.now().strftime("%H:%M:%S")
    elif any(word in msg for word in ["date", "fecha", "date"]):
        return "📅 Today's date is " + datetime.now().strftime("%Y-%m-%d")

    # --- Math ---
    elif re.search(r'^[0-9\+\-\*\/\.\s]+$', msg):
        try:
            result = eval(msg)
            return f"🧮 The result of `{msg}` is {result}"
        except Exception:
            return "⚠️ Please enter a valid math expression, e.g., `2+2` or `3*5`."

    # --- Food ---
    if "pizza" in msg:
        return "🍕 Pizza is delicious! What's your favorite topping?"
    if "burger" in msg:
        return "🍔 Burgers are always tasty! Cheese or no cheese?"
    if any(word in msg for word in ["food", "eat", "meal", "comida", "nourriture"]):
        return "😋 I love food! What's your favorite dish?"

    # --- IT ---
    if "python" in msg:
        return "🐍 Python is amazing! Use it for web dev, AI, or automation."
    if "cpu" in msg:
        return "🖥️ CPU is the brain of your computer."
    if "ram" in msg:
        return "💾 RAM stores temporary data for running programs."
    if "database" in msg:
        return "🗄️ Databases store and manage information efficiently."
    if "network" in msg:
        return "🌐 Networks connect devices and share data!"
    if any(word in msg for word in ["computer", "hardware", "software", "programming"]):
        return "💡 Computers are powerful tools — hardware and software working together!"

    # --- Cricket ---
    if "cricket" in msg:
        return "🏏 Cricket is exciting! Who's your favorite player?"
    if "virat" in msg:
        return "🏏 Virat Kohli is a phenomenal batsman!"
    if "rohit" in msg:
        return "🏏 Rohit Sharma is a world-class opener!"
    if "bumrah" in msg:
        return "🏏 Jasprit Bumrah is an incredible fast bowler!"
    if "pant" in msg:
        return "🏏 Rishabh Pant is a dynamic wicketkeeper-batsman!"
    if "india" in msg:
        return "🇮🇳 India has many top players like Virat, Rohit, Bumrah, and Pant!"

    # --- Grammar ---
    if "noun" in msg:
        return "📘 Noun = person, place, thing, or idea. Example: dog, city, happiness."
    if "verb" in msg:
        return "📘 Verb = action word. Example: run, eat, play."
    if "adjective" in msg:
        return "📘 Adjective = describes a noun. Example: happy, blue, tall."
    if "grammar" in msg or "english" in msg:
        return "✏️ I can explain English grammar basics like nouns, verbs, and adjectives."

    # --- Default ---
    return "🤔 Sorry, I didn’t understand that. Try asking about IT, cricket, grammar, food, or math!"


# --- Flask Routes ---
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_msg = request.args.get("msg", "")
    return chatbot_reply(user_msg)


if __name__ == "__main__":
    app.run(debug=True)
