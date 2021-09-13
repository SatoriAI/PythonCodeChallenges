from collections import Counter
from random import randint


def roll_dice(*args, reps=1000000):
    """Simulates rolling n dices with any numbers
    of sides. Prints the probability of all possible
    outputs.

    Args:
        reps (int, optional): number of Monte Carlo simulations. Defaults to 1000000.
    """
    outcomes = []
    for _ in range(reps):
        outcomes.append(sum([randint(1, dice) for dice in args]))

    probs = sorted([(key, value / reps) for key, value in Counter(outcomes).items()], key=lambda x: x[0])
    for prob in probs:
        print('{}\t{:0.2f}%'.format(prob[0], prob[1]*100))


if __name__ == "__main__":
    roll_dice(6, 6)
