# -*- coding: utf-8 -*-
# @Author  : XFishalways
# @Time    : 2023/6/6 15:30
# @Function: generate a safe prime and a random primitive root, with calculating the execution time

import Crypto.Util.number as num
import random
import time


def pair(s):
    start_time = time.time()

    while True:
        p = num.getPrime(s)
        safe_prime = 2 * p + 1
        if num.isPrime(safe_prime):
            break
    while True:
        a = random.randint(2, safe_prime - 1)
        if (safe_prime - 1) % a != 1:
            break

    end_time = time.time()
    execution_time = end_time - start_time

    return safe_prime, a, execution_time

