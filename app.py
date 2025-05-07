from flask import Flask, render_template, request
from app.chatbot import load_chain
from dotenv import load_dotenv
import os

load_dotenv()

print("Loaded API Key:", os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)
chain = load_chain()

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        query = request.form["query"]
        result = chain.run(query)
        response = result
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
