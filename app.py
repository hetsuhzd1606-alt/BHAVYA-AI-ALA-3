from flask import Flask, render_template, request, jsonify
import datetime
import random

app = Flask(_name_)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_msg = request.json.get("message", "").lower().strip()
    current_time = datetime.datetime.now().strftime("%I:%M %p")

    # ---------- GREETING RESPONSES ----------
    if any(word in user_msg for word in ["hi", "hey", "hello", "hii", "hyy", "yo", "hola", "sup", "whatsup", "morning", "afternoon", "evening"]):
        reply = random.choice([
            "Hey there 👋! I’m TechMate, your smart chatbot assistant.",
            "Hello! I’m TechMate, your tech-savvy virtual buddy 🤖.",
            "Hi there! I’m TechMate — ready to chat about tech, cars, and more 🚀."
        ])
        reply += "\n\nYou can ask me about:\n• 💻 IT & Cybersecurity\n• ✈ Airplanes\n• 🚗 Cars\n• 🤖 AI & Technology\nTry saying something like ‘Tell me about AI’ or ‘How does a plane fly?’"

    # ---------- ABOUT CHATBOT ----------
    elif "who are you" in user_msg or "your name" in user_msg or "about you" in user_msg:
        reply = "I’m TechMate, a rule-based chatbot built using Python + Flask. I love talking about technology, vehicles, and cybersecurity 🔐."

    elif "what can you do" in user_msg or "help" in user_msg or "functions" in user_msg:
        reply = (
            "Here’s what I can do for you:\n"
            "• Explain IT & Cybersecurity concepts 💻\n"
            "• Talk about cars and airplanes 🚗✈\n"
            "• Share facts about AI, Python, or programming 🤖\n"
            "• Tell you the current time ⏰\n"
            "• Just have a friendly chat 😄"
        )

    # ---------- TIME ----------
    elif "time" in user_msg:
        reply = f"⏰ The current time is {current_time}. Always a good time to learn something new!"

    # ---------- IT & PROGRAMMING ----------
    elif "python" in user_msg:
        reply = "🐍 Python is a powerful programming language — great for AI, automation, and web development!"

    elif "ai" in user_msg or "artificial intelligence" in user_msg:
        reply = "🧠 AI (Artificial Intelligence) is the ability of machines to mimic human thinking, learning, and problem-solving."

    elif "computer" in user_msg:
        reply = "💻 A computer is a digital device that processes data through instructions to perform tasks."

    elif "cloud" in user_msg:
        reply = "☁ Cloud computing lets users store and access data online instead of using local devices."

    elif "data" in user_msg or "database" in user_msg:
        reply = "📂 A database stores and manages structured information so it can be quickly retrieved and analyzed."

    # ---------- CYBERSECURITY ----------
    elif "cybersecurity" in user_msg or "security" in user_msg:
        reply = "🔐 Cybersecurity is the protection of systems and data from digital attacks using firewalls, encryption, and secure networks."

    elif "hacking" in user_msg or "hacker" in user_msg:
        reply = "⚠ Hacking means gaining unauthorized access to systems. Ethical hackers use this skill legally to find and fix vulnerabilities."

    elif "firewall" in user_msg:
        reply = "🔥 A firewall monitors and filters network traffic — blocking harmful connections and allowing safe data to pass."

    elif "virus" in user_msg or "malware" in user_msg:
        reply = "🦠 Malware and viruses are harmful programs that can steal or damage your data. Use antivirus software to stay protected."

    # ---------- AIRPLANES ----------
    elif "plane" in user_msg or "airplane" in user_msg or "jet" in user_msg:
        reply = "✈ Airplanes fly because of lift, created by air flowing faster over the wings than beneath them."

    elif "pilot" in user_msg:
        reply = "👨‍✈ Pilots control and navigate aircraft, managing communication, altitude, and flight systems."

    elif "airport" in user_msg:
        reply = "🛫 Airports are designed for takeoffs, landings, and passenger management — with control towers ensuring safe air traffic."

    elif "engine" in user_msg and "plane" in user_msg:
        reply = "A jet engine pushes air backward to move the airplane forward — it’s Newton’s Third Law in action! 🚀"

    # ---------- CARS ----------
    elif "car" in user_msg or "automobile" in user_msg:
        reply = "🚗 Cars convert fuel into energy using engines, or electricity in EVs. Modern cars even use AI for self-driving!"

    elif "tesla" in user_msg or "elon musk" in user_msg:
        reply = "⚡ Tesla, founded by Elon Musk, makes electric cars and self-driving technology using advanced AI."

    elif "engine" in user_msg and "car" in user_msg:
        reply = "An engine converts fuel or electricity into motion to move your car forward. 🔧"

    elif "fuel" in user_msg or "petrol" in user_msg or "diesel" in user_msg:
        reply = "⛽ Cars mostly run on petrol or diesel, but EVs like Tesla run on electricity stored in batteries."

    # ---------- SMALL TALK ----------
    elif "how are you" in user_msg:
        reply = "I’m great, thanks for asking! 😊 How about you?"

    elif "thank" in user_msg:
        reply = random.choice(["You’re welcome!", "Glad I could help!", "Anytime!", "No worries 😊"])

    elif "bye" in user_msg or "exit" in user_msg or "goodnight" in user_msg:
        reply = "👋 Goodbye! Keep learning and stay awesome 🚀"

    # ---------- FALLBACK ----------
    else:
        reply = (
            "Hmm 🤔 I’m not sure about that, but I’m great with tech, cybersecurity, and vehicles!\n"
            "Try asking:\n• 'What is AI?'\n• 'How does a car engine work?'\n• 'What is cybersecurity?'\n• 'How do planes fly?'"
        )

    return jsonify({"reply": reply})


if _name_ == "_main_":
    app.run(debug=True)
