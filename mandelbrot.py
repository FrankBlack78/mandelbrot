#!/usr/bin/env python3

from math import log, log2

MAX_ITER = 16464


def mandelbrot(c):
    """
    :param c: A complex number.
    :return: Number of iterations needed to reach a modulus greater than 2. If more than MAX_ITER, then MAX_ITER.
    """
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z * z + c
        n += 1

    if n == MAX_ITER:
        return MAX_ITER

    return n + 1 - log(log2(abs(z)))


if __name__ == '__main__':
    for a in range(-10, 10, 5):
        for b in range(-10, 10, 5):
            c = complex(a / 10, b / 10)
            print(c, mandelbrot(c))
