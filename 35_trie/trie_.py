#!/usr/bin/python
# -*- coding: UTF-8 -*-

from queue import Queue
import pygraphviz as pgv

OUTPUT_PATH = '/home/thanhtran/'


class Node:
    def __init__(self, c):
        self.data = c
        self.is_ending_char = False
        # Use ordered arrays to reduce space consumption and support more characters
        self.children = []

    def insert_child(self, c):
        self._insert_child(Node(c))

    def _insert_child(self, node):
        """
        Insert a child node
        :param c:
        :return:
        """
        v = ord(node.data)
        idx = self._find_insert_idx(v)
        length = len(self.children)

        if idx == length:
            self.children.append(node)
        else:
            self.children.append(None)
            for i in range(length, idx, -1):
                self.children[i] = self.children[i-1]
            self.children[idx] = node

    def has_child(self, c):
        return True if self.get_child(c) is not None else False

    def get_child(self, c):
        """
        Search child nodes and return
        :param c:
        :return:
        """
        start = 0
        end = len(self.children) - 1
        v = ord(c)

        while start <= end:
            mid = (start + end)//2
            if v == ord(self.children[mid].data):
                return self.children[mid]
            elif v < ord(self.children[mid].data):
                end = mid - 1
            else:
                start = mid + 1
        # Cannot find return None
        return None

    def _find_insert_idx(self, v):
        """
        Binary search, find the insertion position of the ordered array
        :param v:
        :return:
        """
        start = 0
        end = len(self.children) - 1

        while start <= end:
            mid = (start + end)//2
            if v < ord(self.children[mid].data):
                end = mid - 1
            else:
                if mid + 1 == len(self.children) or v < ord(self.children[mid+1].data):
                    return mid + 1
                else:
                    start = mid + 1
        # v < self.children[0]
        return 0

    def __repr__(self):
        return 'node value: {}'.format(self.data) + '\n' \
               + 'children:{}'.format([n.data for n in self.children])


class Trie:
    def __init__(self):
        self.root = Node(None)

    def gen_tree(self, string_list):
        """
        Create trie tree
        1. Traverse the characters of each string, starting from the root node, if there is no corresponding child node, create
        2. The end node of each string is marked in red (is_ending_char)
        :param string_list:
        :return:
        """
        for string in string_list:
            n = self.root
            for c in string:
                if n.get_child(c) is None:
                    n.insert_child(c)
                n = n.get_child(c)
            n.is_ending_char = True

    def search(self, pattern):
        """
        search for
        1. Traverse the characters in the pattern string and search from the root node. If the child node does not exist on the way, return False
        2. After traversing the pattern string, it means that the pattern string exists, and then check whether the last node in the tree is red, yes
            Return True, otherwise False
        :param pattern:
        :return:
        """
        assert type(pattern) is str and len(pattern) > 0

        n = self.root
        for c in pattern:
            if n.get_child(c) is None:
                return False
            n = n.get_child(c)

        return True if n.is_ending_char is True else False

    def draw_img(self, img_name='Trie.png'):
        """
        Draw the trie tree
        :param img_name:
        :return:
        """
        if self.root is None:
            return

        tree = pgv.AGraph('graph foo {}', strict=False, directed=False)

        # root
        nid = 0
        color = 'black'
        tree.add_node(nid, color=color, label='None')

        q = Queue()
        q.put((self.root, nid))
        while not q.empty():
            n, pid = q.get()
            for c in n.children:
                nid += 1
                q.put((c, nid))
                color = 'red' if c.is_ending_char is True else 'black'
                tree.add_node(nid, color=color, label=c.data)
                tree.add_edge(pid, nid)

        tree.graph_attr['epsilon'] = '0.01'
        tree.layout('dot')
        tree.draw(OUTPUT_PATH + img_name)
        return True


if __name__ == '__main__':
    string_list = ['abc', 'abd', 'abcc', 'accd', 'acml',
                   'P@trick', 'data', 'structure', 'algorithm']

    print('--- gen trie ---')
    print(string_list)
    trie = Trie()
    trie.gen_tree(string_list)
    trie.draw_img()

    print('\n')
    print('--- search result ---')
    search_string = ['a', 'ab', 'abc', 'abcc',
                     'abe', 'P@trick', 'P@tric', 'Patrick']
    for ss in search_string:
        print('[pattern]: {}'.format(ss),
              '[result]: {}'.format(trie.search(ss)))
