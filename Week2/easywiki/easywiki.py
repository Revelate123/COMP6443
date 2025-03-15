from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "4e9800998ecf"


@app.route("/")
def index():
    session.clear()
    session["user"] = "admin"
    
    return "<div>Goodbye hello<div>"



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)