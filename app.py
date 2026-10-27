from flask import Flask, render_template, request
from services.gemini_service import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.form.get("prompt", "").strip()

    if not prompt:
        return render_template(
            "result.html",
            prompt=prompt,
            response="Please enter a question."
        )

    try:
        print("User Prompt:", prompt)

        response = get_response(prompt)
        print("Gemini Response:", response)

        return render_template(
            "result.html",
            prompt=prompt,
            response=response
        )

    except Exception as e:
        print("Error:", e)
        return render_template(
            "result.html",
            prompt=prompt,
            response=f"Error: {e}"
        )

if __name__ == "__main__":
    print("Flask app starting...")
    app.run(debug=True)
