#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List, Tuple


def bag(items_info: List[int], capacity: int) -> int:
    """
    For a backpack with a fixed capacity, calculate the maximum weight of the combination of items that can be loaded into the backpack
    :param items_info: weight of each item
    :param capacity: backpack capacity
    :return: Maximum loading weight
    """
    n = len(items_info)
    memo = [[-1]*(capacity+1) for i in range(n)]
    memo[0][0] = 1
    if items_info[0] <= capacity:
        memo[0][items_info[0]] = 1

    for i in range(1, n):
        for cur_weight in range(capacity+1):
            if memo[i-1][cur_weight] != -1:
                memo[i][cur_weight] = memo[i-1][cur_weight]   # Uncheck
                if cur_weight + items_info[i] <= capacity:    # Selected
                    memo[i][cur_weight + items_info[i]] = 1

    for w in range(capacity, -1, -1):
        if memo[-1][w] != -1:
            return w


def bag_with_max_value(items_info: List[Tuple[int, int]], capacity: int) -> int:
    """
    A backpack with a fixed capacity, calculate the maximum value of the combination of items that can be loaded into the backpack
    :param items_info: the weight and value of the item
    :param capacity: backpack capacity
    :return: Maximum loading value
    """
    n = len(items_info)
    memo = [[-1]*(capacity+1) for i in range(n)]
    memo[0][0] = 0
    if items_info[0][0] <= capacity:
        memo[0][items_info[0][0]] = items_info[0][1]

    for i in range(1, n):
        for cur_weight in range(capacity+1):
            if memo[i-1][cur_weight] != -1:
                memo[i][cur_weight] = memo[i-1][cur_weight]
                if cur_weight + items_info[i][0] <= capacity:
                    memo[i][cur_weight + items_info[i][0]] = max(memo[i][cur_weight + items_info[i][0]],
                                                                 memo[i-1][cur_weight] + items_info[i][1])
    return max(memo[-1])


if __name__ == '__main__':
    # [weight, ...]
    items_info = [2, 2, 4, 6, 3]
    capacity = 9
    print(bag(items_info, capacity))

    # [(weight, value), ...]
    items_info = [(3, 5), (2, 2), (1, 4), (1, 2), (4, 10)]
    capacity = 8
    print(bag_with_max_value(items_info, capacity))
