import argparse

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict


def summarize(ranks, sentences, length):
    if int(length) > len(sentences): 
        print("Error, more sentences requested than available. Use --l (--length) flag to adjust.")
        exit()

    indexes = nlargest(int(length), ranks, key=ranks.get)
    final_sentences = [sentences[j] for j in sorted(indexes)]
    return ' '.join(final_sentences) 

def score_tokens(filterd_words, sentence_tokens):
    word_freq = FreqDist(filterd_words)

    ranking = defaultdict(int)

    for i, sentence in enumerate(sentence_tokens):
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                ranking[i] += word_freq[word]
                
    return ranking


def tokenize_content(content):
    stop_words = set(stopwords.words('english') + list(punctuation))
    words = word_tokenize(content.lower())
    
    return [
        sent_tokenize(content),
        [word for word in words if word not in stop_words]    
    ]

def sanitize_input(data):
    replace = {
        ord('\f') : ' ',
        ord('\t') : ' ',
        ord('\n') : ' ',
        ord('\r') : None
    }

    return data.translate(replace)

def read_file(path):
    try:
        with open(path, 'r') as file:
            return file.read()

    except IOError as e:
        print("Fatal Error: File ({}) could not be located or is not readable.".format(path))


def summController(numberOfSentences): 
    content = read_file("content.txt")
    content = sanitize_input(content)

    sentence_tokens, word_tokens = tokenize_content(content)  
    sentence_ranks = score_tokens(word_tokens, sentence_tokens)

    return summarize(sentence_ranks, sentence_tokens, numberOfSentences)
    
