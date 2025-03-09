from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "$hallICompareTHEE2aSummersday"


@app.route("/")
def index():
    session["admin"] = True
    session["secret_key"] = "$hallICompareTHEE2aSummersday"
    return "<div>Hello<div>"



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)