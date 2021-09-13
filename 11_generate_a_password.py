from random import sample


def read_file(path):
    """Reads a .txt file. It shoud have the following format:
    `number\twors`. Returns a list of tuples. Each contains two information
    the numbers and the corresponding word.

    Args:
        path (str): path to the wordlist.

    Returns:
        list: enumerated words from the file.
    """
    word_list = []
    with open(path, 'r') as file:
        for line in file.readlines():
            number, word = line.strip().split('\t')
            word_list.append((int(number), word))
    return word_list


def generate_passphrase(num_words, path='files\\wordlist.txt'):
    """Generates a password using a list of words.

    Args:
        num_words (int): the length of the password,
        path (str, optional): the path to the wordlist. Defaults to 'files\\wordlist.txt'.

    Returns:
        str: generated password.
    """
    drawn_numbers = [int(''.join(sample(['1', '2', '3', '4', '5', '6'], 5))) for _ in range(num_words)]
    word_list = read_file(path)
    word_tuples = [x[1] for x in word_list if x[0] in drawn_numbers]
    return ' '.join(word_tuples)


if __name__ == "__main__":
    print(generate_passphrase(7))
