from random import randint
from time import time


def waiting_game():
    """Simple game. Asks the user to press Enter after a certain,
    random generated value of time.
    """
    number_of_seconds = randint(2, 4)
    print('Your target time is {} seconds.'.format(number_of_seconds))
    text = input('---Press Enter to Begin---')
    if text == '':
        start = time()
        text = input('...Press Enter again after {} seconds...'.format(number_of_seconds))
        if text == '':
            elapsed = time() - start
            msg = 'Elapsed time: {:.4f} seconds ({:.4f} seconds {})'
            if elapsed > number_of_seconds:
                print(msg.format(elapsed, abs(number_of_seconds-elapsed), 'too slow'))
            else:
                print(msg.format(elapsed, abs(number_of_seconds-elapsed), 'too fast'))


if __name__ == "__main__":
    waiting_game()
