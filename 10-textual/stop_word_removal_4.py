# to download the NLTK data libraries
# import nltk
# nltk.download()

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(text)

tokenized_filtered_text = [w for w in word_tokens if not w in stop_words]

print(tokenized_filtered_text)
