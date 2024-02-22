"""
 convertupper.py
"""
def capitalise(filename):
    """ Creates a new file with the prefix 'encrypted_'
        added to the name of the original file.
        All the alphabetic characters in the new
        are capitalized.  This function does not
        disturb the contents of the original file. """
    with open(filename, 'r') as infile:
        with open('encrypted_' + filename, 'w') as outfile:
            for line in infile:
                line = line.strip().upper()
                print(line, file=outfile)
