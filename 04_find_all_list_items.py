def index_all(ls, value):
    """Finds all indexes of a given value
    inside a list. Can be nested.

    Args:
        ls (list): list containing any objects,
        value: some value (can be string, int, whatever).

    Returns:
        list: list containing indexes of the given value
        in the list. Given in the format of nested list.
        The length of a single list gives the knowledge how
        nested the value was. For example the real index
        of a value for the output [[0, 0, 0, 3]] would be
        ls[0][0][0][3].
    """
    indexes = []
    for i in range(len(ls)):
        if ls[i] == value:
            indexes.append([i])
        elif isinstance(ls[i], list):
            for index in index_all(ls[i], value):
                indexes.append([i] + index)
    return indexes


if __name__ == "__main__":
    assert index_all([1, 2, 3], 2) == [[1]]
    assert index_all([2, 1, [1, 2], [1, 3, 2]], 2) == [[0], [2, 1], [3, 2]]
    assert index_all([1, 2, [1, [1, 2], [1, 2]]], 2) == [[1], [2, 1, 1], [2, 2, 1]]
    assert index_all([[[1, 3, 4, 2]], 2], 2) == [[0, 0, 3], [1]]
