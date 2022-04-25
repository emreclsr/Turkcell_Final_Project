from model.preprocess import *
from twitter.get_tweets import *
import warnings
warnings.filterwarnings("ignore")


def model_main(normalizer, revisedDict, tfidf_load, svc_load):
    print("Starting new session...", end="\r", flush=True)
    print("Getting tweets...", end="\r", flush=True)
    save_tweets()
    print("Preprocessing tweets...", end="\r", flush=True)
    preprocess_df = preprocess(normalizer, revisedDict)
    print("Prediction...", end="\r", flush=True)
    predicted_df = predict(preprocess_df, tfidf_load, svc_load)


