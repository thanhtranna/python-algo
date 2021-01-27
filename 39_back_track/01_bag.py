#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List

# List of items selected by the backpack
picks = []
picks_with_max_value = []


def bag(capacity: int, cur_weight: int, items_info: List, pick_idx: int):
    """
    Backtracking method to solve 01 backpack, exhaustive
    :param capacity: backpack capacity
    :param cur_weight: current weight of the backpack
    :param items_info: item weight and value information
    :param pick_idx: the index of the current item
    :return:
    """
    # After inspecting all items, or filling them up midway
    if pick_idx >= len(items_info) or cur_weight == capacity:
        global picks_with_max_value
        if get_value(items_info, picks) > \
                get_value(items_info, picks_with_max_value):
            picks_with_max_value = picks.copy()
    else:
        item_weight = items_info[pick_idx][0]
        if cur_weight + item_weight <= capacity:    # Selected
            picks[pick_idx] = 1
            bag(capacity, cur_weight + item_weight, items_info, pick_idx + 1)

        picks[pick_idx] = 0                         # 不选
        bag(capacity, cur_weight, items_info, pick_idx + 1)


def get_value(items_info: List, pick_items: List):
    values = [_[1] for _ in items_info]
    return sum([a*b for a, b in zip(values, pick_items)])


if __name__ == '__main__':
    # [(weight, value), ...]
    items_info = [(3, 5), (2, 2), (1, 4), (1, 2), (4, 10)]
    capacity = 8

    print('--- items info ---')
    print(items_info)

    print('\n--- capacity ---')
    print(capacity)

    picks = [0] * len(items_info)
    bag(capacity, 0, items_info, 0)

    print('\n--- picks ---')
    print(picks_with_max_value)

    print('\n--- value ---')
    print(get_value(items_info, picks_with_max_value))
