# Definition for singly-linked list.
class DbListNode(object):
    def __init__(self, x, y):
        self.key = x
        self.val = y
        self.next = None
        self.prev = None


class LRUCache:
    """
        leet code: 146
            Use the data structure you know to design and implement an LRU (least recently used) cache mechanism.
            It should support the following operations: get data get and write data put.
            Get data get(key)-If the key (key) exists in the cache, get the value of the key (always a positive number), otherwise return -1.
            Write data put(key, value)-If the key does not exist, write its data value.
            When the cache capacity reaches the upper limit, it should delete the least recently used data value before writing new data to make room for the new data value
        Hash table + doubly linked list
        Hash table: query O(1)
        Doubly linked list: ordered, addition and deletion operations O(1)
        Author: Jeremie
    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hkeys = {}
        # self.top and self.tail serve as sentinel nodes to avoid crossing the boundary
        self.top = DbListNode(None, -1)
        self.tail = DbListNode(None, -1)
        self.top.next = self.tail
        self.tail.prev = self.top

    def get(self, key: int) -> int:

        if key in self.hkeys.keys():
            # Update node order
            cur = self.hkeys[key]
            # Jump out of original position
            cur.next.prev = cur.prev
            cur.prev.next = cur.next
            # Place the most recently used at the head of the linked list
            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur

            return self.hkeys[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hkeys.keys():
            cur = self.hkeys[key]
            cur.val = value
            # Jump out of original position
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

            # Place the most recently used at the head of the linked list
            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur
        else:
            # Add new node to the header
            cur = DbListNode(key, value)
            self.hkeys[key] = cur
            # Place the most recently used at the head of the linked list
            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur
            if len(self.hkeys.keys()) > self.cap:
                self.hkeys.pop(self.tail.prev.key)
                # Remove the original end node
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev

    def __repr__(self):
        vals = []
        p = self.top.next
        while p.next:
            vals.append(str(p.val))
            p = p.next
        return '->'.join(vals)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache)
    cache.get(1)  # returns 1
    cache.put(3, 3)  # This operation will invalidate key 2
    print(cache)
    cache.get(2)  # returns -1 (not found)
    cache.put(4, 4)  # This operation will invalidate key 1
    print(cache)
    cache.get(1)  # returns -1 (not found)
    cache.get(3)  # returns 3
    print(cache)
    cache.get(4)  # returns 4
    print(cache)
