#!/usr/bin/python3

 """ 	Implementation of Singly Linked List ADT
	When a new LinkedList object is created, it is empty
	The user should be able to
	- insert a new element at the head of the list in O(1) time
	- insert a new element at the tail of the list in O(1) time
	- insert a new element at any specified location within the 	  list in O(n) time (where 'location' is similar to index:
	  for head node, location = 0; for tail, location = length-1
	- delete an element at the head of the list in O(1) time
	- delete an element at any other location within the list 
	  in O(n) time
	- get the current length of the list in O(1) time 
	- get the data item stored at the head or tail in O(1) time
	- get the data item stored at any other location within the 	  list in O(n) time
	- search by data value: return the location (index) of an
	  element containing the specified value, or -1 if no such 
	  element found within the list
	- delete by data value: delete an element containing the 
	  specified value
	- display contents of the entire list 
  """

class LinkedList:

#--------------------- nested _Node class ----------------------
  class _Node:
    """Nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'     # streamline memory usage

    def __init__(self, element, next):  # initialize node fields
      self._element = element           # ref to data object
      self._next = next                 # reference to next node
#-----------------------nested Empty class ----------------------
  class Empty(Exception): 	  # sublass of Python Exception class
    """Error attempting to access an element from an empty 
	  container."""
	pass
#----------------------------------------------------------------
 
  def __init__(self):
    """ Initialize an empty linked list. """
	self._head = None 		# reference to the head node
	self._tail = None		# reference to the head node
	self._length = 0    		# number of list elements


  def __len__(self):
    """ Returns the number of items in the LinkedList. """

  def is_empty(self):
    """Return True if the list is empty."""

  def first(self):
    """ Returns the data element stored at the head of the list
        Raises Empty exception if the list is empty.
    """

  def last(self):
    """ Returns the data element stored at the tail of the list
        Raises Empty exception if the list is empty.
    """

  def _getNode(self, loc):
    """ Returns the _Node object at location loc.
        Raises an IndexError if loc is invalid location.
    """

  def getData(self, loc):
    """ Returns the data element stored at location loc.
        Raises an IndexError if loc is invalid location.
    """

  def append(self, e):
    """ Add the element e to the end of the list.      """

  def prepend(self, e):
    """ Add the element e to the beginning of the list. """

  def insert(self, e, loc):
    """ Inserts the element e at location loc.
        Raises an IndexError if the location loc is invalid.
	  Two special cases, in which the error is not raised: 
	  if loc = -1, call on method prepend to add at the front;
	  if loc = self.length, call on method append to add at end
    """

  def deleteFirst(self):
    """ Remove the element e at the head of the list; return e
	   Raises Empty exception if the list is empty.         
    """

  def deleteLast(self):
    """ Remove the element e at the tail of the list; return e
	   Raises Empty exception if the list is empty.         
    """

  def delete(self, loc):
    """ Remove the element e at location loc; return e 
	   Raises an IndexError if loc is invalid location.
	   Raises Empty exception if the list is empty.        
    """

  def findElt(self, e):
    """ Returns location where element e is stored
        Raises Empty exception if the list is empty.        
    """
  
  def deleteElt(self, e):
    """ Finds the node where element e is stored and removes 
	  that node.
    """

  def __str__(self):
    """ Return string representation of the linked list."""
	out=""
    	sep=", "
    	node=self._head
    	while node!=self._tail:
      	out=out + sep + str(node._element)
      	node=node._next
    	return out

if __name__ == "__main__":