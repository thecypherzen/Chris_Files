#!/usr/bin/env python3
from nltk.book import text1
from matplotlib import pyplot as plt

# words = ["the", "and"]
# word = "this"
text1.dispersion_plot(['this'])
plt.savefig(f"./text1_this")
