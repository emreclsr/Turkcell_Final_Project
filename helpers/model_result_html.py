import pandas as pd


def model_results_to_html():
    df = pd.read_csv("tweets.csv")
    df = df.iloc[::-1]
    df.reset_index(inplace=True, drop=True)
    df2 = df[["id", "date", "time", "username", "tweet", "prediction", "proba_0", "proba_1", "link"]]
    df2["prediction"][df2["prediction"] == 0] = "Olumsuz"
    df2["prediction"][df2["prediction"] == 1] = "Olumlu"
    df2.to_html("templates/tweets.html")

