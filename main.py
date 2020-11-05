import nltk
from nltk.book import *

dist = FreqDist(text7)

vocab1 = dist.keys()

freqwords = [w for w in vocab1 if len(w) > 5 and dist[w] > 100]

print(freqwords)




