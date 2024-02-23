#!/usr/bin/env python3
from nltk.book import text1
from matplotlib import pyplot as plt
from nltk.probability import FreqDist
from matplotlib.ticker import MultipleLocator

# words = ["the", "and"]
word = "this"
freqDist = FreqDist(text1)
word_freq = freqDist[word]
x = [1]
y = [word_freq]
print(x, y)
plt.bar(x, y, color="#355E3B")
plt.xlabel(word)
plt.gca().xaxis.set_major_locator(MultipleLocator(0.5))
plt.ylabel("Frequency")
plt.savefig("text1_plot_this")
