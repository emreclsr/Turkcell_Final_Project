# import pickle
import tqdm
import pandas as pd
from helpers.preprocess_func import *
from helpers.lemmatizer import *
import warnings
warnings.filterwarnings("ignore")



def preprocess(normalizer, revisedDict):
    # Dataframe is the base dataframe
    df = pd.read_csv("tweets.csv")

    prediction = df[df["prediction"].isnull()]
    if prediction.shape[0] == 0:
        return pd.DataFrame()

    clean_text(prediction, "tweet")
    remove_stopwords(prediction, "tweet")
    tokenize(prediction, "tweet")
    normalize(normalizer, prediction, "tweet")
    drop_words(prediction, "tweet")
    tokenize(prediction, "tweet")

    # Lemmatizer
    for i in range(prediction.shape[0]):
        x = []
        for j in range(len(prediction["tweet"][i])):
            x.append(lemmatize(prediction["tweet"][i][j], revisedDict))

        prediction["tweet"][i] = " ".join(x)

    return prediction


def predict(dataframe, tfidf_load, svc_load):
    if dataframe.shape[0] == 0:
        return

    # Dataframe is prediction dataframe
    df = pd.read_csv("tweets.csv")

    new_tweets = tfidf_load.transform(dataframe["tweet"])
    dataframe["prediction"] = svc_load.predict(new_tweets)
    dataframe["proba_0"] = svc_load.predict_proba(new_tweets)[:, 0]
    dataframe["proba_1"] = svc_load.predict_proba(new_tweets)[:, 1]

    predicted = dataframe[["id", "prediction", "proba_0", "proba_1"]]

    new_df = df.set_index("id").combine_first(predicted.set_index("id")).reset_index()

    new_df.to_csv("tweets.csv", index=False)
