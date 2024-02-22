from matplotlib import pyplot as plt

import re

def plot_Zipfs_Law (filename):
    ''' Plots Zipf's Law for the text in the file named filename.'''

    frequency = {}

    with open(filename, 'r') as content:
        text_string = content.read()
        words = re.findall(r'\b[A-Za-z][a-z]{2,9}\b', text_string)

        for word in words:
            count = frequency.get(word, 0)
            frequency[word] = count + 1

    most_frequent = dict(sorted(frequency.items(), key=lambda elem: elem[1], reverse=True))

    y = []
    for key, (words, frequency) in enumerate(most_frequent.items()):
        y += frequency,

    plt.plot (range(1,len(y)+1), y, label=filename)

plot_Zipfs_Law ("Brown.txt")
plot_Zipfs_Law ("Shake.txt")
plot_Zipfs_Law ("Bible.txt")

plt.title("Zipf's Law for different texts (using log scales)")
plt.legend()
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.xscale('log') # Use log scale for the X axis
plt.yscale('log') # Use log scale for the Y axis

plt.show()
