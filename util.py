import random
import string


def random_word(length=12):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
