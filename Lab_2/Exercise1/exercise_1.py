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
# using similar()
def get_similar(word=None, text="text1", fn="results"):
    if any(not isinstance(item, str) for item in [word, text]):
        return
    with open(fn, 'a+') as stream:
        with open(".tmp", 'w+') as tmp:
            sys.stdout = tmp
            texts[text].similar(word)
            tmp.seek(0)
            similar_words = tmp.read()
            os.remove(str(tmp.name))
            sys.stdout = sys.__stdout__

        message = f"{text}: Words similar to {word}:\n{similar_words}"
        print(message, file=stream)

# using common_contexts() method
def get_common_contexts(word=None, text="text1", fn="results"):
    if any(not isinstance(item, str) for item in [word, text]):
        return
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
    text = "text6"
    for word in words:
        get_similar(word, text)

if __name__ == "__main__":
    main()

