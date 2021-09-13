def simplify(phrase):
    """Creates a lowercase phrase consisting
    only letters (simplifies the inputed string).

    Args:
        phrase (str): string to simplify.

    Returns:
        str: simplified string.
    """
    return ''.join([sign for sign in phrase.lower() if sign.isalpha()])


def is_palindrome(phrase):
    """Checks whether a sentence is a palindrome.

    Args:
        phrase (str): any string containing words.

    Returns:
        boolean: True if simplified phrase is a palindrome
        False otherwise.
    """
    simplified = simplify(phrase)
    return simplified == simplified[::-1]


if __name__ == "__main__":
    assert simplify('I am a Dog.') == 'iamadog'
    assert simplify('I am a dog - a big one; I have 3 sharp teeths.') == 'iamadogabigoneihavesharpteeths'
    assert is_palindrome('Go hang a salami - Im a lasagna hog.') is True
    assert is_palindrome('I am a dog.') is False
