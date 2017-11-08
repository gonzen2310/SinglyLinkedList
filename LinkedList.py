#!/usr/bin/env python3

""" Implementation of Singly Linked List ADT
When a new LinkedList object is created, it is empty
The user should be able to:
- insert a new element at the head of the list in O(1) time
- insert a new element at the tail of the list in O(1) time
- insert a new element at any specified location within the
  list in O(n) time (where 'location' is similar to index:
  for head node, location = 0; for tail, location = length-1
- delete an element at the head of the list in O(1) time
- delete an element at any other location within the list
  in O(n) time
- get the current length of the list in O(1) time
- get the data item stored at the head or tail in O(1) time
- get the data item stored at any other location within the
  list in O(n) time
- search by data value: return the location (index) of an
  element containing the specified value, or -1 if no such
  element found within the list
- delete by data value: delete an element containing the
  specified value
- display contents of the entire list """


class LinkedList:
    # --------------------- nested _Node class ----------------------

    class _Node:
        """Nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):  # initialize node fields
            self._element = element  # ref to data object
            self._next = next  # reference to next node

    # -----------------------nested Empty class ----------------------

    class Empty(Exception):  # subclass of Python Exception class
        """Error attempting to access an element from an empty container."""
        pass

    def __init__(self):
        """ Initialize an empty linked list. """
        self._head = None  # reference to the head node
        self._tail = None  # reference to the head node
        self._length = 0  # number of list elements

    def __len__(self):
        """ Returns the number of items in the LinkedList. """
        return self._length

    def is_empty(self):
        """Return True if the list is empty."""
        if self._length == 0:
            return True
        return

    def first(self):
        """ Returns the data element stored at the head of the list
        Raises Empty exception if the list is empty."""
        if self.is_empty():
            raise Empty("List is empty")
        head_node = self._head._element
        return head_node

    def last(self):
        """ Returns the data element stored at the tail of the list
        Raises Empty exception if the list is empty."""
        if self.is_empty():
            raise Empty("List is empty")
        tail_node = self._tail
        return tail_node._element

    def _getNode(self, loc):
        """ Returns the _Node object at location loc.
        Raises an IndexError if loc is invalid location."""
        if self.is_empty():
            raise Empty("List is Empty")
        if loc > self._length - 1:
            raise IndexError("Out of Bounds")
        node = self._head
        for index in range(self._length):
            if index == loc:
                return node
            node = node._next

    def getData(self, loc):
        """ Returns the data element stored at location loc.
        Raises an IndexError if loc is invalid location."""
        if self.is_empty() or loc > self._length:
            raise Empty("Index out of bounds")
        node = self._getNode(loc)
        return node._element

    def append(self, e):
        """ Add the element e to the end of the list."""
        if self.is_empty():
            new_node = self._Node(e, None)
            self._head = new_node
            self._tail = new_node
        else:
            new_node = self._Node(e, None)
            self._tail._next = new_node
            self._tail = new_node
        self._length += 1

    def prepend(self, e):
        """ Add the element e to the beginning of the list. """
        if self.is_empty():
            new_node = self._Node(e, self._head)
            self._tail = new_node
            self._head = new_node
        else:
            new_node = self._Node(e, self._head)
            self._head = new_node
        self._length += 1

    def insert(self, e, loc):
        """ Inserts the element e at location loc.
        Raises an IndexError if the location loc is invalid.
        Two special cases, in which the error is not raised:
        if loc = -1, call on method prepend to add at the front;
        if loc = self.length, call on method append to add at end """
        if loc > self._length:
            raise IndexError("Out of Bounds")
        if loc == -1:
            self.prepend(e)
        if loc == self._length:
            self.append(e)
        new_node = self._Node(e, None)
        prev_node = self._Node(None, None)
        current_node = self._head
        for location in range(self._length):
            if location == loc:
                prev_node._next = new_node
                new_node._next = current_node
                self._length += 1
                break
            prev_node = current_node
            current_node = current_node._next

    def deleteFirst(self):
        """ Remove the element e at the head of the list; return e
        Raises Empty exception if the list is empty."""
        if self.is_empty():
            raise Empty("List is empty")
        del_head_node = self._head
        self._head = self._head._next
        self._length -= 1
        return del_head_node._element

    def deleteLast(self):
        """ Remove the element e at the tail of the list; return e
        Raises Empty exception if the list is empty."""
        if self.is_empty():
            raise Empty("List is empty")
        last_node_idx = self._length - 1
        new_last_node = self._getNode(last_node_idx - 1)
        new_last_node._next = None
        self._tail = new_last_node
        self._length -= 1
        return self.last()

    def delete(self, loc):
        """ Remove the element e at location loc; return e
        Raises an IndexError if loc is invalid location.
        Raises Empty exception if the list is empty."""
        if self.is_empty():
            raise Empty("List is empty")
        if loc > self._length:
            raise IndexError("Out of bounds")
        for location in range(self._length):
            if location == loc:
                current_node = self._getNode(location - 1)
                current_node._next = current_node._next._next
                self._length -= 1
                return self.getData(loc)

    def findElt(self, e):
        """ Returns location where element e is stored
        Raises Empty exception if the list is empty."""
        if self.is_empty():
            raise Empty("List is empty")
        for find in range(self._length):
            if self.getData(find) == e:
                return find
        print("Element not found")
        return -1

    def deleteElt(self, e):
        """ Finds the node where element e is stored and removes
        that node."""
        if self.is_empty():
            raise Empty("List is empty")
        idx_node = self.findElt(e)
        for location in range(self._length):
            if idx_node == 0:
                self.deleteFirst()
                break
            elif location == idx_node:
                current_node = self._getNode(location - 1)
                current_node._next = current_node._next._next
                self._length -= 1
                break
            pass

    def __str__(self):
        """ Return string representation of the linked list."""
        """ node = self._head
            string_list = ""
            while node:
                string_list = string_list + " " + str(node._element)
                node = node._next
            return string_list"""

        node = self._head
        string_list = ""
        while node:
            string_list += str(node._element) + ", "
            node = node._next
        string_list = string_list[:-2]
        return string_list


def main():
    print()


if __name__ == "__main__":
    main()
