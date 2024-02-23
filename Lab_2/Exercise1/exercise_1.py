#!/usr/bin/env python3
"""
    A play around with the Text Class in nltk.book module

"""


import sys, os
from matplotlib import pyplot as plt
from nltk.probability import FreqDist

# redirect initial messages out of stdout and import texts
tempf = open(".tempf", 'w+')
if not tempf:
    sys.exit(1)

sys.stdout = tempf
from nltk.book import *
sys.stdout = sys.__stdout__

# close and delete temp file
fn = str(tempf.name)
if os.path.exists(fn):
    os.remove(fn)

# define texts
texts = {"text1": text1, "text2":text2, "text3":text3, "text4":text4,\
         "text5":text5, "text6":text6, "text7":text7, "text8": text8,\
        "text9":text9}

# Functions

# get similar words from text set
def generate_similar(text, word):
    with open(".tmp", 'w+') as tmp:
        sys.stdout = tmp
        text.similar(word)
        tmp.seek(0)
        content = tmp.read()
        if content == "No matches\n":
            content = []
        else:
            content = content.split()
        os.remove(tmp.name)
        sys.stdout = sys.__stdout__
    return ", ".join(content)

# get similar words using similar() method
def get_similar_words(word=None, name=None, fn="results", clear=True):
    # check if word passed it not a string
    if not isinstance(word, str):
        return

    # delete file if on first call, else
    if clear:
        get_similar_words.called_before = \
            getattr(get_similar_words, "called_before", False)
        if not get_similar_words.called_before:
            if os.path.exists(fn):
                os.remove(fn)
            get_similar_words.called_before = True

    # prepare results
    message = [f"[ Words Similar to '{word}' in: ]"]
    if name is None:
        for key, text in texts.items():
            content = generate_similar(text, word)
            if len(content) > 0:
                message.append(f"{key}: {content}")
    else:
        if name in texts.keys():
            content = generate_similar(texts[name], word)
            if len(content) > 0:
                message.append(f"{name}: {content}")

    # delimit and print to file
    message = "\n".join(message)
    with open(fn, 'a+') as res_file:
        print(message, file=res_file, end="\n\n")
        for i in range(1,81):
            print("=", file=res_file, end="\n" if i == 80 else "")


# using frequency plot() method
def plot_n_words(text_id, n=20):
    f_dist = FreqDist(texts[text_id])
    f_dist = dict(sorted((item for item in f_dist.items() \
                          if item[0].isalpha()), reverse=True, \
                         key=lambda item: item[1]))
    x_points = [i for i in range(1, n+1)]
    y_points = [count for count in f_dist.values()][ :n]
    x_ticks = [word for word in f_dist.keys()][ :n]

    plt.bar(x_points, y_points, color="#006400")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(x_points, x_ticks)
    plt.title(f"Chart of {n} Most Frequent Words in {text_id}")
    plt.savefig(f"freq_{n}_words_{text_id}_fig")


def frequent_n_plots(name=None, n=20):
    if name is not None and not isinstance(name, str):
        print(f"{type(name)} not supported")
        return
    if name is None:
        for key in texts.keys():
            plot_n_words(key, n)
    elif name not in texts.keys():
        return
    else:
        plot_n_words(name, n)

def main():
    words = ["government", "pleasure", "holy", "things"]
    for word in words:
        get_similar_words(word)
#    frequent_n_plots(n=10)
if __name__ == "__main__":
    main()
