#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


# simple recursion way to solve eating cookies
def eating_cookies_1(n, cache=None):
    if n < 2:
        return 1
    elif n == 2:
        return 2

    return eating_cookies_1(n-1)+eating_cookies_1(n-2) + eating_cookies_1(n-3)


# cache = {}


# incorporating cache to solve eating_cookies:

def eating_cookies(n, cache={}):
    if n < 2:
        return 1
    if n == 2:
        return 2

    if n not in cache:
        cache[n] = eating_cookies(
            n-1)+eating_cookies(n-2) + eating_cookies(n-3)

    return cache[n]


# solved eating_cookies iteratively
def eating_cookies_2(n, cache=None):
    if n < 2:
        return 1
    elif n == 2:
        return 2
    n_0 = 1
    n_1 = 1
    n_2 = 2
    count = 2
    while count < n:
        sum = n_0+n_1+n_2
        n_0 = n_1
        n_1 = n_2
        n_2 = sum
        count += 1
    return sum


# print(eating_cookies_1(15))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
