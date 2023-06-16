"""
https://docs.python.org/3/library/random.html

"""

import random

#randit is including a and  b
def random_number(a, b) -> int:
    a_integer = random.randint(a, b)
    return a_integer

def random_float(start = 1.1, stop = 5.0) -> float:
    #I need random fload not 0.0000 to 0.9999 but also from 1 to 5
    randomFloat = random.uniform(start, stop)
    return randomFloat








