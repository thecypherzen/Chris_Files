#!/usr/bin/env python3
from nltk.book import text1
from matplotlib import pyplot as plt
from nltk.probability import FreqDist




fDist = FreqDist(text1)
#clean_dict = sorted(item for item in fDist.items() if item[0].isalnum())
fDist = dict(sorted((item for item in fDist.items() if item[0].isalpha()), \
            reverse=True, key=lambda item: item[1]))

x_points = [i for i in range(1, 11)]
y_points = [f for _, f in fDist.items()][:10]
words = [word for word, _ in fDist.items()][:10]

print(words)
print(x_points)
print(y_points)

plt.bar(x_points, y_points, color="#355E3B", width=0.5, label=words)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.savefig("first_n_fequency")
