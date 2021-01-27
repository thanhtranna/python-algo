#!/usr/bin/python
# -*- coding: UTF-8 -*-

from time import time


def kmp(main, pattern):
    """
    kmp string matching
    :param main:
    :param pattern:
    :return:
    """
    assert type(main) is str and type(pattern) is str

    n, m = len(main), len(pattern)

    if m == 0:
        return 0
    if n <= m:
        return 0 if main == pattern else -1

    # Solve next array
    next = get_next(pattern)

    j = 0
    for i in range(n):
        # In pattern[:j], recurse from long to short to find the longest prefix substring that matches the suffix substring
        while j > 0 and main[i] != pattern[j]:
            # If next[j-1] = -1, then take the match from the starting character
            j = next[j-1] + 1

        if main[i] == pattern[j]:
            if j == m-1:
                return i-m+1
            else:
                j += 1
    return -1


def get_next(pattern):
    """
    next array generation
    note:
    The difficulty of understanding is that next[i] is solved according to next[0], next[1]…… next[i-1]
    The value of next[i] depends on the value of the previous next array, the solution idea:
    1. First take the previous longest matching prefix substring, and its subscript is next[i-1]
    2. Compare the next character, if it matches, directly assign next[i] to next[i-1]+1, because i-1 is already the longest
    *3. If it does not match, you need to recursively find the second-longest matched prefix substring. The hard thing to understand here is the recursive method, next[i-1]
         Is the subscript end of the longest matching prefix substring of i-1, then *next[next[i-1]]* is the subscript of the second longest matching prefix substring
         end
    *4. The recursive exit is when the next character of the second-longest prefix substring matches the current one or -1 is encountered. When -1 is encountered, it means that no one was found.
         What to match the prefix substring, then you need to find the first character of pattern to compare
    ps: The value of next[m-1] is actually meaningless and can be ignored when solving. There is also a way to shift the next array to the right on the Internet.
    :param pattern:
    :return:
    """
    m = len(pattern)
    next = [-1] * m

    next[0] = -1

    # for i in range(1, m):
    for i in range(1, m-1):
        # The longest prefix substring matched when taking i-1
        j = next[i-1]
        while j != -1 and pattern[j+1] != pattern[i]:
            # The subscript of the second longest prefix substring is next[next[i-1]]
            j = next[j]

        # According to the condition of jumping out of while above, when j=-1, pattern[0] needs to be compared with the current character
        # If j!=-1, then pattern[j+1] and pattern[i] must be equal
        # If the following characters are also matched, the subscript of the longest prefix substring of i is next[i-1]+1
        if pattern[j+1] == pattern[i]:
            j += 1
        next[i] = j

    return next


if __name__ == '__main__':
    m_str = "aabbbbaaabbababbabbbabaaabb"
    p_str = "abbabbbabaa"

    print('--- search ---')
    t = time()
    print('[Built-in Functions] result:', m_str.find(p_str))
    print('[Built-in Functions] time cost: {0:.5}s'.format(time()-t))

    t = time()
    print('[kmp] result:', kmp(m_str, p_str))
    print('[kmp Functions] time cost: {0:.5}s'.format(time()-t))
