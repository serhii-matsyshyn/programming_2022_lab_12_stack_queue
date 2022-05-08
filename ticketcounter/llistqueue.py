"""Implementation of the Queue ADT using a linked list"""


class Queue:
    """A queue is a first-in-first-out (FIFO) data structure
    that maintains the order of elements inserted into the queue."""

    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._count = 0

    def isEmpty(self):
        """ Returns true if the queue is empty """
        return self._qhead is None

    def __len__(self):
        """ Returns the number of items in the queue """
        return self._count

    def enqueue(self, item):
        """ Adds the item to the queue """
        node = _QueueNode(item)
        if self.isEmpty():
            self._qhead = node
        else:
            self._qtail.next = node

        self._qtail = node
        self._count += 1

    def dequeue(self):
        """ Removes and returns the first item """
        assert not self.isEmpty(), "Can not be empty"
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None
        self._qhead = self._qhead.next
        self._count -= 1
        return node.item


class _QueueNode:
    """ A node in the queue """

    def __init__(self, item):
        self.item = item
        self.next = None
