def is_prime(n):
    """Checks whether an integer is a prime.

    Args:
        n (int): positive integer.

    Returns:
        boolean: True if n is prime, False otherwise.
    """
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True


def get_prime_factors(n):
    """Computes prime factors of n.

    Args:
        n (int): positive integer.

    Returns:
        list: list containing all prime factors of n.
    """
    if is_prime(n):
        return [n]
    prime_factors = []
    for i in range(2, n+1):
        while n % i == 0:
            if n % i == 0 and is_prime(i):
                n = n / i
                prime_factors.append(i)
    return prime_factors


if __name__ == "__main__":
    assert is_prime(3) is True
    assert is_prime(25) is False
    assert is_prime(7829) is True
    assert get_prime_factors(5) == [5]
    assert get_prime_factors(630) == [2, 3, 3, 5, 7]
    assert get_prime_factors(1024) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
