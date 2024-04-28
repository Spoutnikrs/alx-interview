#!/usr/bin/python3
""" doc """


def minOperations(n):
    operations = 0

    if n <= 1:
        return 0

    i = 2
    while i * i <= n:
        while n % i == 0:
            operations += i
            n //= i
        i += 1

    if n > 1:
        operations += n

    return operations
