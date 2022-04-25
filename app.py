from flask import Flask, render_template, request
from helpers.model_result_html import *
from model.model_main import *
import warnings
import pickle
from zemberek import (TurkishSentenceNormalizer, TurkishMorphology)
warnings.filterwarnings("ignore")

print("Preloading models...", end="\r", flush=True)

morphology = TurkishMorphology.create_with_defaults()
normalizer = TurkishSentenceNormalizer(morphology)

with open("model/revisedDict.pkl", 'rb') as f:
    revisedDict = pickle.load(f)

tfidf_load = pickle.load(open("model/tfidf_fit.pkl", "rb"))
svc_load = pickle.load(open("model/svm_model.pkl", "rb"))

print("Preloading done...")
#-------------------------------------------------------

app = Flask(__name__)


@app.route("/")
def hello():
        return render_template("index.html")


@app.route("/table", methods=["POST"])
def submit():
    # HTML -> .py
    if request.method == "POST":
        # value = request.form["value"]
        # print(value)
        model_main(normalizer, revisedDict, tfidf_load, svc_load)
        model_results_to_html()
    # .py -> HTML
    return render_template("tweets.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)