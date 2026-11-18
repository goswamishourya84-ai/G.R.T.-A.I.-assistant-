import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/chat")
def chat():
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        return jsonify(error="AI server setup pending hai. API key hosting settings mein configure karni hogi."), 503
    message = ((request.get_json(silent=True) or {}).get("message") or "").strip()
    if not message:
        return jsonify(error="Message khaali hai."), 400
    try:
        result = OpenAI(api_key=key).responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            input=message
        )
        return jsonify(reply=result.output_text)
    except Exception:
        return jsonify(error="AI se connection nahi ho paya. Server settings check karein."), 502

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))\n