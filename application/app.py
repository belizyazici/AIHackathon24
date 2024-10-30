from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# API key configuration
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def chat_with_bot(user_message):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content([f"Eğitimci gibi cevapla (ortaokul seviyesi): {user_message}. Lütfen karmaşık terimler kullanma ve bilgi düzeyini 8. sınıf seviyesine kadar sınırla."])
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

@app.route("/turkce")
def turkce():
    return render_template("turkce.html")

@app.route("/turkcesix")
def turkcesix():
    return render_template("turkcesix.html")

@app.route("/fen")
def fen():
    return render_template("fen.html")

@app.route("/fenseven")
def fenseven():
    return render_template("fenseven.html")

@app.route("/matematik")
def matematik():
    return render_template("matematik.html")

@app.route("/sosyal")
def sosyal():
    return render_template("sosyal.html")

@app.route("/sosyaleight")
def sosyaleight():
    return render_template("sosyaleight.html")

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
