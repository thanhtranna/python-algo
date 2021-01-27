#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List

Layer_nums = List[int]


def yh_triangle(nums: List[Layer_nums]) -> int:
    """
    Starting from the root node and going down, the nodes passed in the process only need to store the smallest path and
    :param nums:
    :return:
    """
    assert len(nums) > 0
    n = len(nums)   # Number of layers
    memo = [[0]*n for i in range(n)]
    memo[0][0] = nums[0][0]

    for i in range(1, n):
        for j in range(i+1):
            # There are two numbers at the beginning and end of each layer, and there is only one path to reach
            if j == 0:
                memo[i][j] = memo[i-1][j] + nums[i][j]
            elif j == i:
                memo[i][j] = memo[i-1][j-1] + nums[i][j]
            else:
                memo[i][j] = min(memo[i-1][j-1] + nums[i][j],
                                 memo[i-1][j] + nums[i][j])
    return min(memo[n-1])


def yh_triangle_space_optimization(nums: List[Layer_nums]) -> int:
    assert len(nums) > 0
    n = len(nums)
    memo = [0] * n
    memo[0] = nums[0][0]

    for i in range(1, n):
        for j in range(i, -1, -1):
            if j == i:
                memo[j] = memo[j-1] + nums[i][j]
            elif j == 0:
                memo[j] = memo[j] + nums[i][j]
            else:
                memo[j] = min(memo[j-1] + nums[i][j], memo[j] + nums[i][j])
    return min(memo)


def yh_triangle_bottom_up(nums: List[Layer_nums]) -> int:
    assert len(nums) > 0
    n = len(nums)
    memo = nums[-1].copy()

    for i in range(n-1, 0, -1):
        for j in range(i):
            memo[j] = min(memo[j] + nums[i-1][j], memo[j+1] + nums[i-1][j])
    return memo[0]


if __name__ == '__main__':
    nums = [[3], [2, 6], [5, 4, 2], [6, 0, 3, 2]]
    print(yh_triangle(nums))
    print(yh_triangle_space_optimization(nums))
    print(yh_triangle_bottom_up(nums))
