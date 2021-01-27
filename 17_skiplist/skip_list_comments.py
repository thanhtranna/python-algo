import random


class SkipListNode(object):

    def __init__(self, val, high=1):
        # Node stored value
        self.data = val
        # Node corresponds to the depth of the index layer
        self.deeps = [None] * high


class SkipList(object):
    """
        An implementation of skip list.
        The list stores positive integers without duplicates.
        An implementation method of skip table.
        The jump table stores positive integers, and the stored ones are not repeated.
        Author: Ben
    """

    def __init__(self):
        # Maximum depth of index layer
        self.__MAX_LEVEL = 16
        # Jump table height
        self._high = 1
        # The first node of each index layer, the default value is None
        self._head = SkipListNode(None, self.__MAX_LEVEL)

    def find(self, val):
        cur = self._head
        # From the top level of the index, locate the value you want to find layer by layer
        # The upper and lower index layers are corresponding, and the starting point of the lower layer is the node corresponding to the maximum value of the previous index layer that is less than the inserted value
        for i in range(self._high-1, -1, -1):
         # In the same index layer, find the node corresponding to the maximum value less than the inserted value
            while cur.deeps[i] and cur.deeps[i].data < val:
                cur = cur.deeps[i]

        if cur.deeps[0] and cur.deeps[0].data == val:
            return cur.deeps[0]
        return None

    def insert(self, val):
        '''
        When adding, obtain the number of index layers to be updated through a random function,
        A pointer to add a new node to the index layer below the given height
        '''
        high = self.randomLevel()
        if self._high < high:
            self._high = high
        # Apply for a new node
        newNode = SkipListNode(val, high)
        # cache is used to cache the largest node in the corresponding index layer that is less than the inserted value
        cache = [self._head] * high
        cur = self._head

        # Look for nodes smaller than the inserted value at each index layer below the random height
        for i in range(high-1, -1, -1):
            # Look for nodes less than the inserted value in each index layer
            #! The upper and lower index layers are corresponding, and the starting point of the lower layer is the node corresponding to the maximum value of the previous index layer that is less than the inserted value
            while cur.deeps[i] and cur.deeps[i].data < val:
                cur = cur.deeps[i]
            cache[i] = cur

        # Insert a new node in each index layer smaller than the height
        for i in range(high):
            # new.next = prev.next \ prev.next = new.next
            newNode.deeps[i] = cache[i].deeps[i]
            cache[i].deeps[i] = newNode

    def delete(self, val):
        '''
        When deleting, delete the corresponding nodes in each index layer
        '''
        # cache is used to cache the largest node in the corresponding index layer that is less than the inserted value
        cache = [None] * self._high
        cur = self._head
        # Cache each index layer to locate nodes less than the inserted value
        for i in range(self._high-1, -1, -1):
            while cur.deeps[i] and cur.deeps[i].data < val:
                cur = cur.deeps[i]
            cache[i] = cur
        # If the given value exists, update the corresponding node in the index layer
        if cur.deeps[0] and cur.deeps[0].data == val:
            for i in range(self._high):
                if cache[i].deeps[i] and cache[i].deeps[i].data == val:
                    cache[i].deeps[i] = cache[i].deeps[i].deeps[i]

    def randomLevel(self, p=0.25):
        '''
            #define ZSKIPLIST_P 0.25      /* Skiplist P = 1/4 */
            https://github.com/antirez/redis/blob/unstable/src/t_zset.c
        '''
        high = 1
        for _ in range(self.__MAX_LEVEL - 1):
            if random.random() < p:
                high += 1
        return high

    def __repr__(self):
        vals = []
        p = self._head
        while p.deeps[0]:
            vals.append(str(p.deeps[0].data))
            p = p.deeps[0]
        return '->'.join(vals)


if __name__ == '__main__':
    sl = SkipList()
    for i in range(100):
        sl.insert(i)
    print(sl)
    p = sl.find(7)
    print(p.data)
    sl.delete(37)
    print(sl)
    sl.delete(37.5)
    print(sl)
