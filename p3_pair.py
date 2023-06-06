# -*- coding: utf-8 -*-
# @Author  : XFishalways
# @Time    : 2023/6/6 15:30
# @Function:
"""

such that pair(d) will return (p,a) containing a safe prime p with 
d bits and a generator a for Z∗p.

"""
import random

import Crypto.Util.number as num


def pair(s):
    while True:
        p = num.getPrime(s)
        safe_prime = 2 * p + 1
        if num.isPrime(safe_prime):
            break
    while True:
        a = random.randint(2, safe_prime - 1)
        if (safe_prime - 1) % a != 1:
            break

    return safe_prime, a


#####################################################################
# Tests

if __name__ == "__main__":
    print(pair(10))
    print(pair(100))
