import pickle


class DictSaver:
    """Saves a dictionary using pickle library. Capable
    also of retrieving it from a given path.
    """

    @staticmethod
    def save_dict(dct, path='files\\dict.pickle'):
        with open(path, 'wb') as file:
            pickle.dump(dct, file)

    @staticmethod
    def read_dict(path='files\\dict.pickle'):
        with open(path, 'rb') as file:
            return pickle.load(file)


if __name__ == "__main__":
    dictionary = {1: 1, 2: 2}
    DictSaver.save_dict(dictionary)
    assert dictionary == DictSaver.read_dict()
