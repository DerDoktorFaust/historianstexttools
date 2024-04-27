import re
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


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

def lemmatize_text(data, language='english') -> str:

    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')

    lemmatizer = WordNetLemmatizer()

    # tokenize the sentence while also tagging it for part of speech
    pos_tagged = nltk.pos_tag(nltk.word_tokenize(data))

    data_tagged = list(map(lambda x: (x[0], part_of_speech_tagger(x[1])), pos_tagged))

    lemmatized_data = []

    for word, tag in data_tagged:
        if tag is None:
            lemmatized_data.append(word)
        else:
            lemmatized_data.append(lemmatizer.lemmatize(word, tag))

    return " ".join(lemmatized_data)


def part_of_speech_tagger(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

