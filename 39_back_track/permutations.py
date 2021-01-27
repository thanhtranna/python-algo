#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List

permutations_list = []  # Global variables to record each output


def permutations(nums: List, n: int, pick_count: int):
    """
    Select the full array of n numbers from nums
    Backtracking method, use a stack to record the current path information
    When n==0, it means that the number in the stack is enough, output and terminate the traversal
    :param nums:
    :param n:
    :param pick_count:
    :return:
    """
    if n == 0:
        print(permutations_list)
    else:
        for i in range(len(nums) - pick_count):
            permutations_list[pick_count] = nums[i]
            nums[i], nums[len(nums) - pick_count -
                          1] = nums[len(nums) - pick_count - 1], nums[i]
            permutations(nums, n-1, pick_count+1)
            nums[i], nums[len(nums) - pick_count -
                          1] = nums[len(nums) - pick_count - 1], nums[i]


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    n = 3
    print('--- list ---')
    print(nums)

    print('\n--- pick num ---')
    print(n)

    print('\n--- permutation list ---')
    permutations_list = [0] * n
    permutations(nums, n, 0)
