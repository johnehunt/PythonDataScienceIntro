from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ['play', "playing", 'played', 'plays']

for word in words:
    print(stemmer.stem(word)), words
