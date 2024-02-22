""" Uses a dictionary to group the words in a text file according to
    their length (number of letters).

    Noted issues:
    1. punctuation marks are included in words.
    2. punctuation marks
"""

import sys     # For argv global command line arguments list
import re


def main():
     """  Group the words by length in a text file.  """
     if len(sys.argv) < 2:   # Did the user not supply a file name?
         print('Usage:  python groupwords.py <filename>')
         print('     where <filename> is the name of a text file.')
     else:   # User provided file name
         filename = sys.argv[1]
         groups = {}        # Initialize grouping dictionary
         with open(filename, 'r') as f:  # Open the file for reading
             words = f.read()  # Read in content of the  entire file

             # MY MODIFICATION - START
             # Make list of individual words, factoring in punctuations
             words = re.split(r'[ ;:,.?()\[\]{}&/"]+|-{2,}', words)
             words = " ".join(words)
             words = words.split()
             # MY MODIFICATION - END

             for word in words:
                 word = word.lower()  # Make the word all in lower case
                 # Compute the word's length

                 size = len(word)
                 if size in groups:
                     if word not in groups[size]:  # Avoid duplicates
                         groups[size] += [word]  # Add the word to its group
                 else:
                     groups[size] = [word]   # Add the word to a new group
             # Show the groups
             for size, group in sorted(groups.items()):
                 print(size, ':', group)


if __name__ == '__main__':
     main()
