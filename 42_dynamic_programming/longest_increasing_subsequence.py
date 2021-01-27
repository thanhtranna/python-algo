#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List


def longest_increasing_subsequence(nums: List[int]) -> int:
    """
    A DP solution of the longest sub-ascending sequence, transformed from the backtracking solution, and the idea is similar to the knapsack problem of limited items
    Calculate the current possible length of lis for each decision, repeat sub-problems merge, the merge strategy is the smallest element at the end of lis
    Time complexity: O(n^2)
    Space complexity: O(n^2), can be optimized to O(n)
    The reference answer on leetcode is not efficient, provide another idea as a reference
    https://leetcode.com/problems/longest-increasing-subsequence/solution/
    :param nums:
    :return:
    """
    if not nums:
        return 0

    n = len(nums)
    # memo[i][j] represents the i-th decision, the smallest value of the last element of lis with length j
    # Each decision is based on all possible conversions of the last decision, and the space can be optimized to O(n) similar to a backpack
    memo = [[-1] * (n+1) for _ in range(n)]

    # The first column is assigned a value of 0, which means that no number is selected for each decision
    for i in range(n):
        memo[i][0] = 0
    # The first decision to choose the first number in the array
    memo[0][1] = nums[0]

    for i in range(1, n):
        for j in range(1, n+1):
            # case 1: lis with length j exists after the last decision, nums[i] is larger than the last element of lis with length j-1
            if memo[i-1][j] != -1 and nums[i] > memo[i-1][j-1]:
                memo[i][j] = min(nums[i], memo[i-1][j])

            # case 2: lis with length j exists after the last decision, nums[i] is smaller than the last element of lis with length j-1/etc.
            if memo[i-1][j] != -1 and nums[i] <= memo[i-1][j-1]:
                memo[i][j] = memo[i-1][j]

            if memo[i-1][j] == -1:
                # case 3: lis with length j does not exist, nums[i] is larger than the last element of lis with length j-1
                if nums[i] > memo[i-1][j-1]:
                    memo[i][j] = nums[i]
                # case 4: lis with length j does not exist, nums[i] is smaller than the last element of lis with length j-1/etc.
                break

    for i in range(n, -1, -1):
        if memo[-1][i] != -1:
            return i


if __name__ == '__main__':
    # The input required is a positive integer greater than 0 (can be optimized to support any integer)
    nums = [2, 9, 3, 6, 5, 1, 7]
    print(longest_increasing_subsequence(nums))
