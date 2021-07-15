from collections import Counter
from nltk.util import bigrams, trigrams
from nltk.tokenize import word_tokenize
import re

raw_text = "Many people do not like football, although football is very popular in the UK."
text = re.sub('[^a-zA-Z0-9]', ' ', raw_text)
word_tokens = word_tokenize(text)

# Splitting sentence into bigrams and trigrams
print(list(word_tokens))
print(list(bigrams(word_tokens)))
print(list(trigrams(word_tokens)))

# Find most common words
print(Counter(word_tokens).most_common(2))
