import time
import pickle
from model.preprocess import *
from twitter.get_tweets import *
from zemberek import (TurkishSentenceNormalizer, TurkishMorphology)
import warnings
warnings.filterwarnings("ignore")

morphology = TurkishMorphology.create_with_defaults()
normalizer = TurkishSentenceNormalizer(morphology)

with open("model/revisedDict.pkl", 'rb') as f:
    revisedDict = pickle.load(f)

tfidf_load = pickle.load(open("model/tfidf_fit.pkl", "rb"))
svc_load = pickle.load(open("model/svm_model.pkl", "rb"))


while True:
    print("Starting new session...")
    print("Getting tweets...")
    save_tweets()
    print("Preprocessing tweets...")
    preprocess_df = preprocess(normalizer, revisedDict)
    print("Prediction...")
    predicted_df = predict(preprocess_df, tfidf_load, svc_load)
    for i in range(120, 0, -1):
        print(f"Prediction done wait {i} seconds to start new session...", end="\r", flush=True)
        time.sleep(1)


