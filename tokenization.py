import nltk

# Download 'punkt' if not already downloaded
nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize

corpus = "Hello world. This is a test."
sentences = sent_tokenize(corpus)
print(sentences)
