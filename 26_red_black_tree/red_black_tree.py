#!/usr/bin/python
# -*- coding: UTF-8 -*-

from queue import Queue
import pygraphviz as pgv
import random


OUTPUT_PATH = '/home/thanhtran/'


class TreeNode:
    def __init__(self, val=None, color=None):
        self.val = val
        assert color in ['r', 'b']
        self.color = 'red' if color == 'r' else 'black'

        self.left = None
        self.right = None
        self.parent = None

    def is_black(self):
        return self.color == 'black'

    def set_black(self):
        self.color = 'black'
        return

    def set_red(self):
        self.color = 'red'


class RedBlackTree:
    """
    Red-black tree implementation
    Reference materials:
    1. "Introduction to Algorithms"
    Chapter 13 The Red-Black Tree
    13.3 Insert p178
    13.4 Delete p183
    2. Red-Black Tree (2): Delete
    https://zhuanlan.zhihu.com/p/25402654
    """

    def __init__(self, val_list=None):
        self.root = None
        self.black_leaf = TreeNode(color='b')  # Shared black leaf node

        # Available array initialization
        if type(val_list) is list:
            for n in val_list:
                assert type(n) is int
                self.insert(n)

    def search(self, val):
        """
        search
        :param val:
        :return:
        """
        if self.root is None:
            return None

        n = self.root
        while n != self.black_leaf:
            if val < n.val:
                n = n.left
            elif val > n.val:
                n = n.right
            else:
                return n
        return None

    def insert(self, val):
        """
        insert
        :param val:
        :return:
        """
        assert type(val) is int

        new_node = TreeNode(val, 'r')  # The newly inserted node is red

        # Root node
        if self.root is None:
            self.root = new_node
        else:
            n = self.root
            while n != self.black_leaf:  # Black leaf node
                p = n
                if val < n.val:
                    n = n.left
                elif val > n.val:
                    n = n.right
                else:
                    # The value already exists, insertion failed
                    raise KeyError('val:{} already exists')

            if val < p.val:
                p.left = new_node
            else:
                p.right = new_node
            new_node.parent = p

        new_node.left = new_node.right = self.black_leaf
        # Adjust after insertion
        self._insert_fixup(new_node)

    def _insert_fixup(self, node):
        """
        Insert adjustment
        Reference: "Introduction to Algorithms" 13.3 p178-179
        :param node:
        :return:
        """
        n = node
        while n is not self.root and not n.parent.is_black():
            # Father p uncle u grandfather g
            p = self.parent(n)
            u = self.bro(p)
            g = self.parent(p)

            if not u.is_black():        # case 1
                p.set_black()           # case 1
                u.set_black()           # case 1
                g.set_red()             # case 1
                n = g                   # case 1
                continue

            if p == g.left:     # p is the left node
                if n == p.right:        # case 2
                    self.rotate_l(p)    # case 2
                    n, p = p, n         # case 2
                p.set_black()           # case 3
                g.set_red()             # case 3
                self.rotate_r(g)        # case 3
            else:               # p is the right node
                if n == p.left:         # case 2
                    self.rotate_r(p)    # case 2
                    n, p = p, n         # case 2
                p.set_black()           # case 3
                g.set_red()             # case 3
                self.rotate_l(g)        # case 3

        # The root node is forced to be black. There are two situations where the root node is red:
        # 1. It is red when newly inserted
        # 2. It turns red after adjustment in case 1
        self.root.color = 'black'

    def delete(self, val):
        """
        delete
        :param val:
        :return:
        """
        assert type(val) is int

        n = self.search(val)
        if n is None:
            print('can not find any nodes with value: {}'.format(val))
            return

        self._delete_node(n)

    def _delete_node(self, node):
        """
        Delete the internal implementation of the node
        Reference: "Introduction to Algorithms" 13.4 p183-184
        The implementation method is fine-tuned. When n has 2 child nodes, copy s to n and delete s (s has at most one child node)
        :param node:
        :return:
        """
        n = node

        # The number of children of n is equal to 2
        if self.children_count(n) == 2:
            # Looking for successor s of n
            s = n.right
            while s.left != self.black_leaf:
                s = s.left
            n.val = s.val
            # Convert delete n to delete s
            n = s

        # The number of child nodes of n is less than 2
        if n.left == self.black_leaf:
            c = n.right
        else:
            c = n.left
        self._transplant(n, c)

        # The deleted node is black and needs to be adjusted
        if n.is_black():
            self._delete_fixup(c)
        return

    def _delete_fixup(self, node):
        """
        Delete adjustment
        Reference: "Introduction to Algorithms" 13.4 p185-187
        :param node:
        :return:
        """
        n = node
        while n != self.root and n.is_black():
            p = self.parent(n)
            b = self.bro(n)

            # Symmetrical left and right nodes
            if p.left == n:
                if not b.is_black():
                    b.set_black()                   # case 1
                    p.set_red()                     # case 1
                    self.rotate_l(p)                # case 1
                    # new bro after rotate
                    b = self.bro(n)                 # case 1

                if b.left.is_black() and b.right.is_black():
                    b.set_red()                     # case 2
                    n = p                           # case 2
                else:
                    if b.right.is_black():
                        b.left.set_black()          # case 3
                        b.set_red()                 # case 3
                        self.rotate_r(b)            # case 3
                        # new bro after rotate
                        b = self.bro(n)             # case 3

                    # Note that because p may be red or black, you cannot assign a color directly, you can only copy
                    b.color = p.color               # case 4
                    p.set_black()                   # case 4
                    b.right.set_black()             # case 4
                    self.rotate_l(p)                # case 4
                    # trick, After adjustment, jump out of while
                    n = self.root                   # case 4
            else:
                if not b.is_black():
                    b.set_black()                   # case 1
                    p.set_red()                     # case 1
                    self.rotate_r(p)                # case 1
                    # new bro after rotate
                    b = self.bro(n)                 # case 1

                if b.left.is_black() and b.right.is_black():
                    b.set_red()                     # case 2
                    n = p                           # case 2
                else:
                    if b.left.is_black():
                        b.right.set_black()         # case 3
                        b.set_red()                 # case 3
                        self.rotate_l(b)            # case 3
                        # new bro after rotate
                        b = self.bro(n)             # case 3

                    # Note that because p may be red or black, you cannot assign a color directly, you can only copy
                    b.color = p.color               # case 4
                    p.set_black()                   # case 4
                    b.left.set_black()              # case 4
                    self.rotate_r(p)                # case 4
                    # trick, 调整结束跳出while
                    n = self.root                   # case 4

        # Set n to black, jump out of the while loop above, there are two situations
        # 1. n is the root node, just ignore the additional black
        # 2. If n is a red node, it is dyed black
        n.set_black()

    def _transplant(self, n1, n2):
        """
        Node migration, n2 -> n1
        :param n1: original node
        :param n2: transplant node
        :return:
        """
        if n1 == self.root:
            if n2 != self.black_leaf:
                self.root = n2
                n2.parent = None
            else:
                self.root = None    # Will come in only when the root node is deleted
        else:
            p = self.parent(n1)
            if p.left == n1:
                p.left = n2
            else:
                p.right = n2

            n2.parent = p

    def rotate_l(self, node):
        """
        Left hand
        :param node:
        :return:
        """
        if node is None:
            return

        if node.right is self.black_leaf:
            return
            # raise Exception('try rotate left , but the node "{}" has no right child'.format(node.val))

        p = self.parent(node)
        x = node
        y = node.right

        # When node is the root node, p is None, and the root node point should be updated after rotation
        if p is not None:
            if x == p.left:
                p.left = y
            else:
                p.right = y
        else:
            self.root = y

        x.parent, y.parent = y, p

        if y.left != self.black_leaf:
            y.left.parent = x

        x.right, y.left = y.left, x

    def rotate_r(self, node):
        """
        right hand
        :param node:
        :return:
        """
        if node is None:
            return

        if node.left is self.black_leaf:
            return
            # raise Exception('try rotate right , but the node "{}" has no left child'.format(node.val))

        p = self.parent(node)
        x = node
        y = node.left

        # Same as Left
        if p is not None:
            if x == p.left:
                p.left = y
            else:
                p.right = y
        else:
            self.root = y

        x.parent, y.parent = y, p

        if y.right is not None:
            y.right.parent = x

        x.left, y.right = y.right, x

    @staticmethod
    def bro(node):
        """
        get brother node
        :param node:
        :return:
        """
        if node is None or node.parent is None:
            return None
        else:
            p = node.parent
            if node == p.left:
                return p.right
            else:
                return p.left

    @staticmethod
    def parent(node):
        """
        get parent node
        :param node:
        :return:
        """
        if node is None:
            return None
        else:
            return node.parent

    def children_count(self, node):
        """
        Get the number of child nodes
        :param node:
        :return:
        """
        return 2 - [node.left, node.right].count(self.black_leaf)

    def draw_img(self, img_name='Red_Black_Tree.png'):
        """
        Drawing
        Draw nodes and arrows with pygraphviz
        The red and black arrows represent left and right respectively
        :param img_name:
        :return:
        """
        if self.root is None:
            return

        tree = pgv.AGraph(directed=True, strict=True)

        q = Queue()
        q.put(self.root)

        while not q.empty():
            n = q.get()
            if n != self.black_leaf:  # The connection of the black leaves is drawn by each node
                tree.add_node(n.val, color=n.color)
                #  Draw parent node arrow
                # if n.parent is not None:
                #     tree.add_edge(n.val, n.parent.val)

                for c in [n.left, n.right]:
                    q.put(c)
                    color = 'red' if c == n.left else 'black'
                    if c != self.black_leaf:
                        tree.add_edge(n.val, c.val, color=color)
                    else:
                        tree.add_edge(n.val, 'None', color=color)

        tree.graph_attr['epsilon'] = '0.01'
        tree.layout('dot')
        tree.draw(OUTPUT_PATH + img_name)
        return True


if __name__ == '__main__':
    rbt = RedBlackTree()

    # insert
    nums = list(range(1, 25))
    # random.shuffle(nums)
    for num in nums:
        rbt.insert(num)

    # search
    search_num = 23
    n = rbt.search(search_num)
    if n is not None:
        print(n)
    else:
        print('node {} not found'.format(search_num))

    # delete
    rbt.delete(4)

    # draw image
    rbt.draw_img('rbt.png')
