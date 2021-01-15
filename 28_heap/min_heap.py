class Heap(object):
    '''
    Small top heap with index starting from 0
    Reference: https://github.com/python/cpython/blob/master/Lib/heapq.py
    author: Ben
    '''

    def __init__(self, nums):
        self._heap = nums

    def _siftup(self, pos):
        '''
        Top-down stacking
        Promote the maximum value of the child nodes of the pos node to the pos position
        '''
        start = pos
        startval = self._heap[pos]
        n = len(self._heap)
        # Complete Binary Tree Features
        child = pos * 2 + 1
        # Compare leaf nodes
        while child < n:
            right = child + 1
            # The characteristics of the balanced binary tree, the big ones are on the right
            if right < n and not self._heap[right] > self._heap[child]:
                child = right
            self._heap[pos] = self._heap[child]
            pos = child
            child = pos * 2 + 1
        self._heap[pos] = startval

        # At this time only pos is uncertain
        self._siftdown(start, pos)

    def _siftdown(self, start, pos):
        '''
        Minimum heap: Nodes larger than start are already the smallest heap except pos
        Take pos as the leaf node and start as the element between the root nodes for sorting. Swap the pos leaf node to the correct sort position
        Operation: Starting from the leaf node, when the value of the parent node is greater than the child node, the value of the parent node is reduced to the child node
        '''
        startval = self._heap[pos]
        while pos > start:
            parent = (pos - 1) >> 1
            parentval = self._heap[parent]
            if parentval > startval:
                self._heap[pos] = parentval
                pos = parent
                continue
            break
        self._heap[pos] = startval

    def heapify(self):
        '''
        Heaping: Heaping from back to front (from bottom to top), the subtree of the pos node in _siftup is already ordered,
        So the number of nodes to be sorted is slowly decreasing
        1. Because the nodes from n/2+1 to n are leaf nodes (characteristic of a complete binary tree), they have no child nodes,
        Therefore, only the nodes from n/2 to 0 need to be piled up, and the corresponding parent node is the root node, and the highest value is filtered upward.
        Then exchange the corresponding root node and the highest value found
        2. Because the root node of the tree to be sorted has not been sorted at the beginning, in order to ensure the order of the root node,
        Need to swap the root nodes in the subtree to the correct order
        '''
        n = len(self._heap)
        for i in reversed(range(n // 2)):
            self._siftup(i)

    def heappop(self):
        '''
        Pop the top of the heap O(logn)
        '''
        tail = self._heap.pop()
        # To avoid breaking the full binary tree feature, fill the end of the heap to the beginning of the heap
        # At this time, only the top of the heap is unsorted, and only one top-down heap is required
        if self._heap:
            peak = self._heap[0]
            self._heap[0] = tail
            self._siftup(0)
            return peak
        return tail

    def heappush(self, val):
        '''
        Add elements to the end of the heap O(logn)
        '''
        n = len(self._heap)
        self._heap.append(val)
        # At this time, only the nodes at the end of the heap are unsorted, and the added nodes are iterated to the correct position
        self._siftdown(0, n)

    def __repr__(self):
        vals = [str(i) for i in self._heap]
        return '>'.join(vals)


if __name__ == '__main__':
    h = Heap([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    h.heapify()
    print(h)
    print(h.heappop())
    print(h)
    h.heappush(3.5)
    print(h)
    h.heappush(0.1)
    print(h)
    h.heappush(0.5)
    print(h)
    print(h.heappop())
    print(h)
