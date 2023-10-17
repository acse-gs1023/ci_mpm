from functools import cache
__all__ = ['my_sum', 'factorial']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    if n == 1 or n == 0:
        return 1

    else:
        return n*factorial(n-1)
