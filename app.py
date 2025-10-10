from flask import Flask, render_template, request
from datetime import datetime
import re
import random

app = Flask(__name__)

# --- Chatbot setup ---
def get_language(msg):
    return "en"  # For now, always English

RESPONSES = {
    "en": {
        "hi": [
            "Hello! 👋 I can chat about IT, cricket, grammar, food, math, or just say hi. What would you like to do?",
            "Hi there! 😊 I can answer questions about IT, cricket, grammar, food, or math. Ask me anything!",
            "Hey! 👋 I'm ChatBuddy 🤖. I can help you with IT topics, cricket info, grammar lessons, food talk, or math problems."
        ],
        "how_are_you": [
            "I'm doing great, thanks! 😊 How about you?", 
            "All good here! How are you feeling today?", 
            "I'm fine! Ready to chat with you."
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

def chatbot_reply(message):
    msg = message.lower().strip()
    lang = get_language(msg)
    res = RESPONSES.get(lang, RESPONSES["en"])

    # --- Greetings ---
    if any(word in msg for word in ["hi","hello","hey","hola","salut"]):
        return random.choice(res["hi"])
    elif any(word in msg for word in ["how are you","how r u","cómo estás","ça va"]):
        return random.choice(res["how_are_you"])
    elif any(word in msg for word in ["your name","nombre","ton nom"]):
        return random.choice(res["name"])
    elif any(word in msg for word in ["bye","adios","au revoir"]):
        return random.choice(res["bye"])
    elif any(word in msg for word in ["help","ayuda","aide"]):
        return random.choice(res["help"])

    # --- Time & Date ---
    elif any(word in msg for word in ["time","hora","heure"]):
        return "⏰ The current time is " + datetime.now().strftime("%H:%M:%S")
    elif any(word in msg for word in ["date","fecha","date"]):
        return "📅 Today's date is " + datetime.now().strftime("%Y-%m-%d")

    # --- Math ---
    elif re.search(r'[\d\s\+\-\*\/]+', msg):
        try:
            expr = re.sub(r'[^0-9\+\-\*\/\.]', '', msg)
            result = eval(expr)
            return f"🧮 The result of `{expr}` is {result}"
        except:
            return "⚠️ Please enter a valid math expression, e.g., `2+2` or `3*5`."

    # --- Food ---
    if "pizza" in msg:
        return "🍕 Pizza is delicious! What's your favorite topping?"
    if "burger" in msg:
        return "🍔 Burgers are always tasty! Cheese or no cheese?"
    if any(word in msg for word in ["food","eat","meal","comida","nourriture"]):
        return "😋 I love food! What's your favorite dish?"

    # --- IT ---
    if "python" in msg:
        return "🐍 Python is amazing! You can use it for web dev, AI, or automating tasks. Have you tried coding in Python?"
    if any(word in msg for word in ["computer","cpu","ram","database","network"]):
        if "cpu" in msg: return "🖥️ CPU is the brain of your computer."
        if "ram" in msg: return "💾 RAM stores temporary data while programs run."
        if "database" in msg: return "🗄️ Databases help store structured information."
        if "network" in msg: return "🌐 Networks connect computers. Cool, right?"
        return "I can chat about programming, hardware, databases, and networking. Ask me anything!"

    # --- Cricket ---
    if any(word in msg for word in ["cricket","virat","rohit","bumrah","pant","india"]):
        if "virat" in msg: return "🏏 Virat Kohli is a phenomenal player!"
        if "rohit" in msg: return "🏏 Rohit Sharma is a top-class opener."
        if "bumrah" in msg: return "🏏 Jasprit Bumrah delivers insane fast balls!"
        if "pant" in msg: return "🏏 Rishabh Pant is a talented wicketkeeper-batsman."
        if "india" in msg: return "🇮🇳 India has amazing cricket players like Virat, Rohit, Bumrah, and Pant."
        return "Cricket is thrilling! Who's your favorite player?"

    # --- Grammar ---
    if any(word in msg for word in ["noun","verb","adjective"]):
        if "noun" in msg: return "📘 Noun: a person, place, thing, or idea. Example: `dog`, `city`, `happiness`."
        if "verb" in msg: return "📘 Verb: an action word. Example: `run`, `eat`, `play`."
        if "adjective" in msg: return "📘 Adjective: describes a noun. Example: `happy`, `blue`, `tall`."
    if "grammar" in msg or "english" in msg:
        return "✏️ I can teach English grammar basics like nouns, verbs, adjectives, and more!"

    # --- Fallback ---
    return "🤔 Sorry, I didn't understand. Ask me about IT, cricket, grammar, food, math, or just say hi!"

# --- Flask routes ---
@app.route("/")
def home():
    return render_template("index.html")  # HTML file in templates folder

@app.route("/get")
def get_bot_response():
    user_msg = request.args.get("msg")  # GET request
    return chatbot_reply(user_msg)

if __name__ == "__main__":
    app.run(debug=True)
