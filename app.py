from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://dummy:7898@cluster0.vqo76q2.mongodb.net/?appName=Cluster0")
db = client["studentdb"]
collection = db["students"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    try:
        name = request.form["name"]
        email = request.form["email"]

        collection.insert_one({
            "name": name,
            "email": email
        })

        return render_template("success.html")

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)