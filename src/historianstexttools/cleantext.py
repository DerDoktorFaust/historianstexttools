import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import spacy


def clean_text(data, remove_punctuation=True, lowercase=True, removestopwords=True, stopwordslanguage='english',
               removefrequentwords=False, frequentwords=[], lemmatize=True) -> str:

    if remove_punctuation == True:
        data = remove_punct(data)

    if lowercase == True:
        data = apply_lowercase(data)

    if removestopwords == True:
        data = remove_stopwords(data, stopwordslanguage)

    if removefrequentwords == True:
        data = remove_frequent_words(data, frequentwords)

    return data

def remove_punct(data) -> str:
    return re.sub(r'[^\w\s]', '', data)


def apply_lowercase(data) -> str:
    return data.lower()


def remove_stopwords(data, language='english') -> str:

    nltk.download('stopwords')
    stop_words = set(stopwords.words(language))
    word_tokens = word_tokenize(data)
    filtered_data = [word for word in word_tokens if not word.lower() in stop_words]

    return " ".join(filtered_data)


def remove_frequent_words(data, frequentwords) -> str:

    word_tokens = word_tokenize(data)
    filtered_data = [word for word in word_tokens if not word.lower() in frequentwords]

    return " ".join(filtered_data)

def lemmatize_text(data, language='en') -> str:

    nlp = spacy.load("en_core_web_sm")
    import en_core_web_sm

    filtered_data = load_model(data)

    return " ".join([token.lemma_ for token in filtered_data])
