#!/usr/bin/python
# -*- coding: UTF-8 -*-

is_match = False


def rmatch(r_idx: int, m_idx: int, regex: str, main: str):
    global is_match
    if is_match:
        return

    if r_idx >= len(regex):     # The regular strings are all matched
        is_match = True
        return

    # The regular string has not been matched, but the main string has not matched
    if m_idx >= len(main) and r_idx < len(regex):
        is_match = False
        return

    if regex[r_idx] == '*':     # * Match 1 or more arbitrary characters, recursively search each case
        for i in range(m_idx, len(main)):
            rmatch(r_idx+1, i+1, regex, main)
    elif regex[r_idx] == '?':   # ? Match 0 or 1 arbitrary character, in two cases
        rmatch(r_idx+1, m_idx+1, regex, main)
        rmatch(r_idx+1, m_idx, regex, main)
    else:                       # Non-special characters need to match exactly
        if regex[r_idx] == main[m_idx]:
            rmatch(r_idx+1, m_idx+1, regex, main)


if __name__ == '__main__':
    regex = 'ab*eee?d'
    main = 'abcdsadfkjlekjoiwjiojieeecd'
    rmatch(0, 0, regex, main)
    print(is_match)
