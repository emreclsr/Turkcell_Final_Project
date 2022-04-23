from flask import Flask, render_template, request
from helpers.model_result_html import *


app = Flask(__name__)


@app.route("/")
def hello():
        return render_template("index.html")


@app.route("/table", methods=["POST"])
def submit():
    # HTML -> .py
    if request.method == "POST":
        model_results_to_html()
    # .py -> HTML
    return render_template("tweets.html")




if __name__ == "__main__":
    app.run()