import re

from collections import Counter


def count_words(path):
    """Counts words in a .txt file and displays
    the 20 most frequent words (with the number of appearance).

    Args:
        path (str): path to the .txt file.
    """
    with open(path, 'r', encoding='utf8') as file:
        words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        words = [word.lower() for word in words]
    print(f'Total number of words: {len(words)}\n')
    print('20 Most frequent words:')
    for word, value in Counter(words).most_common(20):
        print(f'{word} \t {value}')


if __name__ == "__main__":
    count_words(path='files/The Complete Work of W. Shakespeares.txt')
