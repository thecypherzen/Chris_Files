#!/usr/bin/env python3
"""
    A play around with the Text Class in nltk.book module

"""


import sys, os

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
        content = tmp.read().split()
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
        print(message, file=res_file)
        for i in range(1,81):
            print("=", file=res_file, end="\n" if i == 80 else "")


# using frequency plot() method
def frequent_n_plots(text=None, n=20, fn="results", clear=True):
    if text is no
    with open(fn, 'a+') as stream:
        with open(".tmp", 'w+') as tmp:
            sys.stdout = tmp
            texts[text].common_contexts(word)
            tmp.seek(0)
            c_contexts = tmp.read()
            os.remove(str(tmp.name))
            sys.stdout = sys.__stdout__

        message = f"{text}: Common Contexts to {word}:\n{c_contexts}"
        print(message, file=stream)

def main():
    words = ["always", "forever", "ancient"]
    for word in words:
        get_similar_words(word)

if __name__ == "__main__":
    main()
