#!/usr/bin/python3
""" doc """


def minOperations(n):
    """ doc """
    operations = 0

    if n <= 1:
        return 0

    for i in range(2, n + 1):
        while n % i == 0:
            operations += i
            n = n / i
    return operations
