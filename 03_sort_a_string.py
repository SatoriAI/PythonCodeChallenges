def sort_words(phrase):
    """Sorts a string. Cases of the letters
    are omitted.

    Args:
        phrase (str): words separated with a with space.

    Returns:
        str: string containing the original words
        in alphabetical order.
    """
    return ' '.join(sorted(phrase.split(' '), key=lambda x: x.lower()))


if __name__ == "__main__":
    assert sort_words('string of words') == 'of string words'
    assert sort_words('banana ORANGE apple') == 'apple banana ORANGE'
