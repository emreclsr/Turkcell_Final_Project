def clean_text(dataframe, col_name):
    """
    Function that cleans the text of the dataframe.
    - Converts the text to lowercase
    - Removes punctuation
    - Removes numbers
    - Replace special characters
    - Remove multiple spaces
    - Remove specific characters

    Parameters
    ----------
    dataframe: pandas dataframe
    col_name: str

    Returns
    -------
    dataframe: pandas dataframe

    """
    # Normalize Case Folding
    dataframe[col_name] = dataframe[col_name].str.lower()
    # Remove hashtags
    dataframe[col_name] = dataframe[col_name].str.replace("#\w+", " ", regex=True)
    # Remove mentions
    dataframe[col_name] = dataframe[col_name].str.replace("@\w+", " ", regex=True)
    # Remove Punctuation
    dataframe[col_name] = dataframe[col_name].str.replace("[^\w\s]", " ", regex=True)
    # Remove Numbers
    dataframe[col_name] = dataframe[col_name].str.replace("\d", " ", regex=True)
    # Replace special characters
    dataframe[col_name] = dataframe[col_name].str.replace("\n", " ")
    # Remove multiple spaces
    dataframe[col_name] = dataframe[col_name].str.replace("\s+", " ", regex=True)
    # Remove specific characters
    dataframe[col_name] = dataframe[col_name].str.replace("<", " ", regex=True)
    return dataframe


def remove_stopwords(dataframe, col_name):
    """
    Function that removes stopwords from the text of the dataframe.

    Parameters
    ----------
    dataframe: pandas dataframe
    col_name: str

    Returns
    -------
    dataframe: pandas dataframe

    """
    import nltk
    stopwords = nltk.corpus.stopwords.words("turkish")
    dataframe[col_name] = dataframe[col_name].apply(lambda x: " ".join(x for x in x.split() if x not in stopwords))
    return dataframe


def remove_rare_words(dataframe, col_name, threshold=1):
    """
    Function that removes rare words from the text of the dataframe.

    Parameters
    ----------
    dataframe: pandas dataframe
    col_name: str
    threshold: int

    Returns
    -------
    dataframe: pandas dataframe

    """
    import pandas as pd

    temp_df = pd.Series(" ".join(dataframe[col_name]).split()).value_counts()
    rare_words = temp_df[temp_df <= threshold]
    dataframe[col_name] = dataframe[col_name].apply(lambda x: " ".join(x for x in x.split() if x not in rare_words))

    return dataframe, rare_words


def tokenize(dataframe, col_name):
    """
    Function that tokenizes the text of the dataframe.
    Parameters
    ----------
    dataframe: pandas dataframe
    col_name: str

    Returns
    -------
    dataframe: pandas dataframe

    """
    dataframe.reset_index(drop=True, inplace=True)
    from nltk.tokenize import word_tokenize
    for i in range(dataframe.shape[0]):
        dataframe[col_name][i] = word_tokenize(dataframe[col_name][i])
    return dataframe


def normalize(normalizer, dataframe, col_name):
    """
    Function that normalizes the text of the dataframe. Before using this function, tokenize the text.
    Parameters
    ----------
    dataframe: pandas dataframe
    col_name: str

    Returns
    -------
    dataframe: pandas dataframe

    """

    from tqdm import tqdm

    for i in tqdm(range(dataframe.shape[0])):
        for j in range(len(dataframe[col_name][i])):
            dataframe[col_name][i][j] = normalizer.normalize(dataframe[col_name][i][j])

    dataframe[col_name] = dataframe[col_name].apply(lambda x: " ".join(x))

    return dataframe

def drop_words(dataframe, col_name):
    """
    Function that drops irrelevant words from the text of the dataframe.

    Parameters
    ----------
    dataframe: pandas dataframe
    col_name: str

    Returns
    -------
    dataframe: pandas dataframe

    """
    word_list = ["a", "b", "c", "d", "e", "f", "g", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "q", "r",
                 "s", "ş", "t", "u", "ü", "v", "w", "x", "y", "z", "_"] + ["aa", "br", "te", "sn", "wi", "bir", "iki",
                                                                           "üç", "dört", "beş", "sekiz", "dokuz",
                                                                           "ürün", "ol", "al", "turkcell"]

    dataframe[col_name] = dataframe[col_name].apply(lambda x: " ".join([word for word in x.split()
                                                                        if word not in word_list]))
    return dataframe





