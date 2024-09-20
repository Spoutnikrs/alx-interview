#!/usr/bin/python3
"""
Main file for testing
"""


def makeChange(coins, amount):
    """
    Determine the fewest number of coins needed to meet a given amount.

    Args:
        coins (list): List of coin denominations available.
        amount (int): The total amount of money to change.

    Returns:
        int: Minimum number of coins needed to make the amount.
             Returns -1 if the amount cannot be made with the available coins.

    Approach:
        Sort coins in descending order.
        Use the highest denomination possible first to minimize the total coin count.
    """

    # Input validation
    if amount < 0:
        return -1
    if amount == 0:
        return 0
    if not coins:
        return -1

    # Sort coins in descending order to try larger coins first
    coins.sort(reverse=True)

    coin_count = 0  # Initialize the count of coins

    for coin in coins:
        if amount == 0:
            break  # If exact amount is achieved, stop

        # Use as many of the current coin denomination as possible
        num_of_coins = amount // coin
        amount -= num_of_coins * coin
        coin_count += num_of_coins

    # If exact amount can't be achieved, return -1
    return coin_count if amount == 0 else -1
