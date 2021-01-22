#!/usr/bin/python
# -*- coding: UTF-8 -*-

from time import time

SIZE = 256


def bm(main, pattern):
    """
    BM algorithm
    Matching rules:
    1. Bad Character Rules
    2. Good character rules
    :param main:
    :param pattern:
    :return:
    """
    assert type(main) is str and type(pattern) is str
    n, m = len(main), len(pattern)

    if n <= m:
        return 0 if main == pattern else -1

    # bc
    bc = [-1] * SIZE
    generate_bc(pattern, m, bc)

    # gs
    suffix = [-1] * m
    prefix = [False] * m
    generate_gs(pattern, m, suffix, prefix)

    i = 0
    while i < n-m+1:
        j = m - 1
        while j >= 0:
            if main[i+j] != pattern[j]:
                break
            else:
                j -= 1

        # The entire pattern has been matched, return
        if j == -1:
            return i

        # 1. Number of shifts after bc rule calculation
        x = j - bc[ord(main[i+j])]

        # 2. Shift number after gs rule calculation
        y = 0
        if j != m - 1:    # Gs exists
            y = move_by_gs(j, m, suffix, prefix)

        i += max(x, y)

    return -1


def generate_bc(pattern, m, bc):
    """
    Generate bad character hash table
    :param pattern:
    :param m:
    :param bc:
    :return:
    """
    for i in range(m):
        bc[ord(pattern[i])] = i


def generate_gs(pattern, m, suffix, prefix):
    """
    Good suffix preprocessing
    :param pattern:
    :param m:
    :param suffix:
    :param prefix:
    :return:
    """
    for i in range(m-1):
        k = 0   # The common suffix length of pattern[:i+1] and pattern
        for j in range(i, -1, -1):
            if pattern[j] == pattern[m-1-k]:
                k += 1
                suffix[k] = j
                if j == 0:
                    prefix[k] = True
            else:
                break


def move_by_gs(j, m, suffix, prefix):
    """
    Calculate the mobile value through a good suffix
    Three situations need to be handled:
    1. The whole good suffix can still be found in the pattern
    2. There is a *suffix substring* in a good suffix that can match the *prefix* of the pattern
    3. Other
    :param j:
    :param m:
    :param suffix:
    :param prefix:
    :return:
    """
    k = m - 1 - j           # j points to the first bad character from back to front, and k is the length of the good suffix for this match

    # 1. The entire good suffix still appears in the remaining characters of the pattern
    if suffix[k] != -1:
        return j - suffix[k] + 1
    else:
        for r in range(j+2, m):     # 2. Suffix substring search from long to short
            if prefix[m-r]:
                return r
        return m                    # 3. Other cases


if __name__ == '__main__':
    print('--- search ---')
    m_str = 'dfasdeeeetewtweyyyhtruuueyytewtweyyhtrhrth'
    p_str = 'eyytewtweyy'

    print('--- time consume ---')
    t = time()
    print('[Built-in Functions] result:', m_str.find(p_str))
    print('[Built-in Functions] time cost: {0:.5}s'.format(time()-t))

    t = time()
    print('[bm] result:', bm(m_str, p_str))
    print('[bm] time cost: {0:.5}s'.format(time()-t))
