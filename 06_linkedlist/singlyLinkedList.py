# 1. Insert, delete and search operations of singly linked list;
# 2. The data type stored in the linked list is Int
#
# Author: Jeremie


class Node(object):
    """Node node of linked list structure"""

    def __init__(self, data, next_node=None):
        """Node node initialization method.
        parameter:
            data: stored data
            next: the reference address of the next Node node
        """
        self._data = data
        self._next = next_node

    @property
    def data(self):
        """Node node storage data acquisition.
        return:
            Data stored in the current Node node
        """
        return self._data

    @data.setter
    def data(self, data):
        """Node node storage data setting method.
        parameter:
            data: new stored data
        """
        self._data = data

    @property
    def next_node(self):
        """Get the next pointer value of the Node node.
        return:
            next pointer data
        """
        return self._next

    @next_node.setter
    def next_node(self, next_node):
        """Modification method of Node node next pointer.
        parameter:
            next: reference to the new next Node node
        """
        self._next = next_node


class SinglyLinkedList(object):
    """Singly linked list"""

    def __init__(self):
        """One-way list initialization method."""
        self._head = None

    def find_by_value(self, value):
        """Search in a one-way list according to the data value.
        parameter:
            value: searched data
        return:
            Node
        """
        node = self._head

        while (node is not None) and (node.data != value):
            node = node.next_node

        return

    def find_by_index(self, index):
        """Search in the list according to the index value.
        parameter:
            index: index value
        return:
            Node
        """
        node = self._head
        pos = 0
        while (node is not None) and (pos != index):
            node = node.next_node
            pos += 1
        return

    def insert_to_head(self, value):
        """ Insert a Node node that stores the value at the head of the linked list.
        parameter:
            value: the data to be stored
        """
        node = Node(value)
        node.next_node = self._head
        self._head = node

    def insert_after(self, node, value):
        """ Insert a Node node that stores value data after a specified Node node in the linked list.
        parameter:
            node: a specified Node node
            value: the data to be stored in the new Node node
        """
        if node is None:  # If you specify to insert a data node after an empty node, do nothing
            return

        new_node = Node(value)
        new_node.next_node = node.next
        node.next = new_node

    def insert_before(self, node, value):
        """ Insert a Node node that stores value data before a specified Node node in the linked list.
        parameter:
            node: a specified Node node
            value: the data to be stored in the new Node node
        """
        if (node is None) or (self._head is None):  # If you specify to insert a data node before an empty node or before an empty linked list, do nothing
            return

        if node == self._head:  # If you insert a data node before the head of the linked list, insert it directly
            self.insert_to_head(value)
            return

        new_node = Node(value)
        pro = self._head
        not_found = False  # If the specified inserted Node node is not found in the entire linked list, the mark amount is set to True
        while pro.next_node != node:  # Find a Node before the specified Node
            if pro.next_node is None:  # If the last node of the linked list has been reached, it indicates that the specified inserted Node node is not found in the linked list
                not_found = True
                break
            else:
                pro = pro.next_node
        if not not_found:
            pro.next_node = new_node
            new_node.next_node = node

    def delete_by_node(self, node):
        """Deletes the node of the specified Node in the linked list.
        parameter:
            node: the specified Node node
        """
        if self.__head is None:  # If the linked list is empty, do nothing
            return

        if node == self.__head:  # If the Node node specified to be deleted is the head node of the linked list
            self.__head = node.next_node
            return

        pro = self.__head
        not_found = False  # If the Node node specified to be deleted is not found in the entire linked list, the mark amount is set to True
        while pro.next_node != node:
            if pro.next_node is None:  # If the last node of the linked list has been reached, it indicates that the Node node specified to be deleted is not found in the linked list
                not_found = True
                break
            else:
                pro = pro.next_node
        if not not_found:
            pro.next_node = node.next_node

    def delete_by_value(self, value):
        """Deletes the Node node that stores data in the linked list.
        parameter:
            value: the specified storage data
        """
        if self.__head is None:  # If the linked list is empty, do nothing
            return

        if self.__head.data == value:  # If the head Node node of the linked list is the Node node designated to be deleted
            self.__head = self.__head.next_node

        pro = self.__head
        node = self.__head.next_node
        not_found = False
        while node.data != value:
            if node.next_node is None:  # If the last node of the linked list has been reached, it indicates that the Node node that executes the Value value is not found in the linked list
                not_found = True
                break
            else:
                pro = node
                node = node.next_node
        if not_found is False:
            pro.next_node = node.next_node

    def delete_last_n_node(self, n):
        """Delete the Nth node from the bottom of the linked list.
        Main idea:
            Set the fast and slow pointers, the fast pointer goes first, and the slow pointer does not move; when the fast pointer has crossed N steps, the fast and slow pointers move to the end of the linked list at the same time.
            When the fast pointer reaches the end of the linked list, the slow pointer points to the Nth node from the bottom of the linked list
        parameter:
            n: the last Nth ordinal number to be deleted
        """
        fast = self.__head
        slow = self.__head
        step = 0

        while step <= n:
            fast = fast.next_node
            step += 1

        while (fast.next_node is not None) and (fast is not None):
            fast = fast.next_node
            slow = slow.next_node
            if fast == slow:
                return True

        return False
