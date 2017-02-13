"""
    Linked list implementation of a Stack
    -------------------------------------

    >>> s = Stack()
    >>> s.push(12)
    >>> s.push(16)
    >>> s.push(2)
    >>> s.pop()
    2
    >>> s.pop()
    16
    >>> s.pop()
    12
    >>> s = Stack([5, 6,7])
    >>> s.pop()
    7
    >>> s[1]
    5
    >>> s[0]
    6
    >>> list(s)
    [6, 5]
    >>> s[-1]
    5
    >>> s[-2]
    6
"""


class Node(object):
    __slots__ = ('data', 'nxt')
    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt


class Stack(object):
    def __init__(self, lst=None):
        self._head = None
        self._length = 0
        self._index = None

        if lst:
            for d in lst:
                self.push(d)

    def push(self, data):
        node = Node(data, nxt=self._head)
        self._head = node
        self._length += 1
        return

    def pop(self):
        if self._length == 0:
            raise IndexError("pop from empty stack")
       
        if self._index == self._head:
            self._index = self._head.nxt

        data = self._head.data
        self._head = self._head.nxt
        self._length -= 1
        return data

    def __getitem__(self, key):
        if key >= self._length or key < -self._length:
            raise IndexError("index out of range")

        if key < 0:
            key = self._length + key

        current = self._head
        
        for _ in range(key):
            current = current.nxt

        return current.data

    def __iter__(self):
        self._index = self._head
        return self

    def __next__(self):
        if not self._index:
            raise StopIteration

        data = self._index.data
        self._index = self._index.nxt
        return data

    def __len__(self):
        return self._length



if __name__ == '__main__':
    import doctest
    doctest.testmod()
