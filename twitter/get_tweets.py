import os
import twint
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


def get_tweets():
    c = twint.Config()
    c.Search = "turkcell"
    c.Store_csv = True
    c.Lang = "tr"
    c.Limit = 20
    c.Hide_output = True
    c.Output = "temp_tweet.csv"

    twint.run.Search(c)


def save_tweets():
    os.remove("temp_tweet.csv")

    get_tweets()

    df = pd.read_csv("tweets.csv")
    temp_df = pd.read_csv("temp_tweet.csv")

    temp_df = temp_df.iloc[::-1]
    temp_df.reset_index(drop=True, inplace=True)

    for i in range(temp_df.shape[0]):
        if temp_df["id"][i] not in list(df["id"]):
            df = df.append(temp_df.iloc[i])

    df = df[df["username"] != "turkcellhizmet"]

    df.to_csv("tweets.csv", index=False)
