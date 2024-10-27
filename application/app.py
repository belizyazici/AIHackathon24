from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# API key configuration
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def chat_with_bot(user_message):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content([f"Eğitimci gibi cevapla: {user_message}"])
    return response.text

@app.route("/")
def home():
    return render_template("website.html")

@app.route("/fifth")
def fifth():
    return render_template("fifth.html")

@app.route("/sixth")
def sixth():
    return render_template("sixth.html")

@app.route("/seventh")
def seventh():
    return render_template("seventh.html")

@app.route("/eighth")
def eighth():
    return render_template("eighth.html")


@app.route("/dil")
def dil():
    return render_template("dil.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message")
    bot_response = chat_with_bot(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
