from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# API anahtarınızı çevresel değişkenden alarak yapılandırın
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def chat_with_bot(user_message):
    # Eğitim odaklı bir yanıt istemek için modeli başlatın
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    
    # Kullanıcı mesajını ekleyerek modelden yanıt alın
    response = model.generate_content([f"Eğitimci gibi cevapla: {user_message}"])
    
    return response.text

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message")
    bot_response = chat_with_bot(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
