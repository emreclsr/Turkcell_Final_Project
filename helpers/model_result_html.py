import pandas as pd
import warnings
warnings.filterwarnings("ignore")


def model_results_to_html():
    df = pd.read_csv("tweets.csv")
    df = df.iloc[::-1]
    df.reset_index(inplace=True, drop=True)
    df2 = df[["id", "date", "time", "username", "tweet", "prediction", "proba_0", "proba_1", "link"]]
    df2["prediction"][df2["prediction"] == 0] = "Olumsuz"
    df2["prediction"][df2["prediction"] == 1] = "Olumlu"

    # df2.to_html("templates/tweets.html", render_links=True, justify="left")

    boostrap_link = '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">'
    # render dataframe as html
    html = df2.to_html(render_links=True, justify="left")
    html = html.replace('class="dataframe"', 'class="table table-striped table-hover"')

    text_file = open("templates/tweets.html", "w", encoding="utf-8")
    text_file.write(boostrap_link + '\n' + html)
    text_file.close()

