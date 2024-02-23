#!/usr/bin/env python3
from nltk.book import text1
from matplotlib import pyplot as plt
from nltk.probability import FreqDist

# words = ["the", "and"]
word = "this"
freqDist = FreqDist(text1)
word_freq = freqDist[word]
plt.plot(word_freq)
plt.savefig("text1_plot_this")
