from matplotlib import pyplot as plt

import re
results_file = "my_results"

def plot_Zipfs_Law (filename):
    ''' Plots Zipf's Law for the text in the file named filename.'''

    frequency = {}

    with open(filename, 'r') as content:
        text_string = content.read()
        words = re.findall(r'\b[A-Za-z][a-z]{2,9}\b', text_string)
        words_count = 0

        for word in words:
            count = frequency.get(word, 0)
            frequency[word] = count + 1
            words_count += 1

    most_frequent = dict(sorted(frequency.items(), key=lambda elem: elem[1], reverse=True))

    y = []
    for _, frequency in most_frequent.items():
        y.append(frequency)

    # MY ADDITION
    # get counts of frequencies == 1, == 2 and > 2.
    counts = {}
    for f in y:
        if f == 1:
            count = counts.get('f=1', 0)
            counts['f=1'] = count + 1
        elif f == 2:
            count = counts.get('f=2', 0)
            counts['f=2'] = count + 1
        elif f > 2:
            count = counts.get('f>2', 0)
            counts['f>2'] = count + 1

    # calculate their percentages and output
    message = "PERCENTAGES SUMMARY:\n"

    total_count = len(y)
    for key, count in counts.items():
        message += f"{key}: {round((count / total_count) * 100, 2)}\n"
    message += '\n'

    with open(results_file, 'w') as f:
        f.write(message)

    plt.plot(range(1, len(y) + 1), y, label=filename)
    return words_count


def init_files(*argsv):
    file_names = {}
    for file in argsv:
        file_names[file] = {}
        file_names[file]["found"] = 0
        file_names[file]["missing"] = 0
    return file_names

def main():
    files = init_files("Brown.txt", "Shake.txt", "Bible.txt")
    message = "WORDS COUNT SUMMARY:\n"
    for file in files.keys():
        # count total words in each file
        with open(file, 'r') as f:
            total_words = f.read().split()

        words_found = plot_Zipfs_Law(file)
        files[file]["found"] = words_found
        files[file]["missing"] = len(total_words) - words_found

        message += "{}: Found: {} | Missing: {}\n".format(
            file, files[file]["found"], files[file]["missing"]
        )

    with open(results_file, 'a') as f:
        f.write(message)

if __name__ == "__main__":
    main()


plt.title("Zipf's Law for different texts (using log scales)")
plt.legend()
plt.xlabel("Rank")
plt.ylabel("Words")
plt.xscale('log') # Use log scale for the X axis
plt.yscale('log') # Use log scale for the Y axis
plt.show()
