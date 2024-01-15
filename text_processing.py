import re
import nltk

from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords

from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet

nltk.download('punkt')
nltk.download('wordnet')

def perform_stemming(text):
    stemmer = PorterStemmer()
    words = nltk.word_tokenize(text)
    stemmed_words = [stemmer.stem(word) for word in words]
    return ' '.join(stemmed_words)

def perform_lemmatization(text):
    lemmatizer = WordNetLemmatizer()
    words = nltk.word_tokenize(text)
    lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in words]
    return ' '.join(lemmatized_words)

def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV, "J": wordnet.ADJ}
    return tag_dict.get(tag, wordnet.NOUN)


def tokenize_text(text):
    return word_tokenize(text)

def remove_characters(text):
    if isinstance(text, str):
        return re.sub(r'[^\w\s]', '', text)
    else:
        return text

def remove_stopwords(text):
    if isinstance(text, str):
        stop_words = set(stopwords.words('english'))
        return [word for word in text if word.lower() not in stop_words]
    else:
        return text

def remove_stopwords2(text):
    if not isinstance(text, list):
        raise ValueError("Input should be a list of words")

        stop_words = set(stopwords.words('english'))
        return [word for word in text if word.lower() not in stop_words]
    else:
        return text


def convert_to_lowercase(text):
    if isinstance(text, str):
        return text.lower()
    else:
        return text

def remove_emojis(text):
    if isinstance(text, str):
        emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F" # emoticons
        u"\U0001F300-\U0001F5FF" # symbols & pictographs
        u"\U0001F680-\U0001F6FF" # transport & map symbols
        u"\U0001F1E0-\U0001F1FF" # flags (iOS)
        "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', text)
    else:
        return text

def remove_extra_spaces(text):
    if isinstance(text, str):
        return re.sub(' +', ' ', text)
    else:
        return text
    
def remove_numbers(text):
    if isinstance(text, str):
        return re.sub(r'\d+', '', text)
    else:
        return text

def remove_emails(text):
    if isinstance(text, str):
        return re.sub(r'@\S+', '', text)
    else:
        return text

def remove_hastags(text):
    if isinstance(text, str):
        return re.sub(r'#\S+', '', text)
    else:
        return text

def remove_links(text):
    if isinstance(text, str):
        return re.sub(r'http\S+', '', text)
    else:
        return text
    
def remove_users(text):
    if isinstance(text, str):
        return re.sub(r'@\S+', '', text)
    else:
        return text