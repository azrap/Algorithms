#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies_1(n, cache=None):
    if n < 2:
        return 1
    elif n == 2:
        return 2

    return eating_cookies_1(n-1)+eating_cookies_1(n-2) + eating_cookies_1(n-3)


def eating_cookies(n, cache=None):
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
