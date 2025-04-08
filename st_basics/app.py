import google.generativeai as genai
from flask import Flask, request, render_template, jsonify

API_KEY = "AIzaSyAe31LNhxbM8AnF0VV4DfstauQleSP8OjY"
genai.configure(api_key=API_KEY)


app = Flask(__name__)

# Function to analyze sentiment
def analyze_sentiment(text):
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = f"Analyze the sentiment of this text: '{text}'. Reply with only Positive, Negative, or Neutral."
    response = model.generate_content(prompt)
    return response.text.strip()

# API route for sentiment analysis
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    sentiment = analyze_sentiment(text)
    return jsonify({"sentiment": sentiment})

# Route to render frontend
@app.route("/")
def index():
    return render_template("index.html")





