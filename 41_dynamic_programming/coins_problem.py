#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List


def coins_dp(values: List[int], target: int) -> int:
    # memo[i]Indicates the minimum number of coins required when target is i
    memo = [0] * (target+1)
    # 0元的时候为0个
    memo[0] = 0

    for i in range(1, target+1):
        min_num = 999999
        # For all n in values
        # memo[i] is min(memo[i-n1], memo[i-n2], ...) + 1
        for n in values:
            if i >= n:
                min_num = min(min_num, 1 + memo[i-n])
            else:   # The values in values should be sorted from small to large
                break
        memo[i] = min_num

    # print(memo)
    return memo[-1]


min_num = 999999


def coins_backtracking(values: List[int], target: int, cur_value: int, coins_count: int):
    if cur_value == target:
        global min_num
        min_num = min(coins_count, min_num)
    else:
        for n in values:
            if cur_value + n <= target:
                coins_backtracking(values, target, cur_value+n, coins_count+1)


if __name__ == '__main__':
    values = [1, 3, 5]
    target = 23
    print(coins_dp(values, target))
    coins_backtracking(values, target, 0, 0)
    print(min_num)
