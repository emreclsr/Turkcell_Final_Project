from model.preprocess import *
from twitter.get_tweets import *
import warnings
warnings.filterwarnings("ignore")


def model_main(normalizer, revisedDict, tfidf_load, svc_load):
    print("Starting new session...")
    print("Getting tweets...")
    save_tweets()
    print("Preprocessing tweets...")
    preprocess_df = preprocess(normalizer, revisedDict)
    print("Prediction...")
    predicted_df = predict(preprocess_df, tfidf_load, svc_load)


