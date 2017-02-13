"""
    Doubly Linked List
    ------------------
    A doubly linked list implementation with iteration and indexing support

    >>> l = LinkedList()
    >>> l.add_last(7)
    >>> l.add_first(3)
    >>> l.first
    3
    >>> l.last
    7
    >>> l[0]
    3
    >>> list(l)
    [3, 7]
    >>> l.remove_first()
    3
    >>> len(l)
    1
    >>> l[0]
    7
    >>> l = LinkedList([4, 8, 12])
    >>> list(l)
    [4, 8, 12]
"""


class Node(object):

    __slots__ = ('data', 'nxt', 'prev')

    def __init__(self, data, nxt=None, prev=None):
        self.data = data
        self.nxt = nxt
        self.prev = prev


class LinkedList(object):

    def __init__(self, initial=None):
        self._head = None
        self._tail = None
        self._length = 0
        self._index = None

        if initial:
            for d in initial:
                self.add_last(d)

    @property
    def first(self):
        return self[0]
    
    @property
    def last(self):
        return self[-1]

    def add_last(self, data):
        """Add element at the end of the list"""
        node = Node(data, prev=self._tail)

        if not self._head:
            self._head = node
            self._tail = node
        else:
            self._tail.nxt = node
            self._tail = node

        self._length += 1
    
    def add_first(self, data):
        """Add element at the start of the list"""
        node = Node(data, nxt=self._head)

        if not self._head:
            self._head = node
            self._tail = node
        else:
            self._head.prev = node
            self._head = node

        self._length += 1

    def remove_last(self):
        """Remove last element from linked list and return value"""
        if self._length == 0:
            raise IndexError("Tried to remove from an empty LinkedList")
        
        # Fix iteration index if it is pointing to the last node
        if self._tail == self._index:
            self._index = None

        # Remove tail
        data = self._tail.data
        self._tail = self._tail.prev

        if self._length == 1:
            self._head = None
        else:
            self._tail.nxt = None
            
        self._length -= 1
        return data

    def remove_first(self):
        """Remove first element from linked list and return value"""
        if self._length == 0:
            raise IndexError("Tried to Remove from an empty LinkedList")

        # Fix iteration index if it is pointing to first node
        if self._head == self._index:
            self._index = self._head.nxt

        # Remove head
        data = self._head.data
        self._head = self._head.nxt

        if self._length == 1:
            self._tail = None
        else:
            self._head.prev = None

        self._length -= 1
        return data

    def remove(self, data):
        """Remove all data ocurrences from the linked list"""
        if self._length == 0:
            return
 
        current = self._head

        while current:
            if current.data != data:
                current = current.nxt
                continue

            # Try to recover gracefully from removing current iter index
            if self._index == current:
                self._index = current.nxt

            if current.nxt:
                current.nxt.prev = current.prev
            if current.prev:
                current.prev.nxt = current.nxt
            
            if self._head == current:
                self._head = current.nxt
            if self._tail == current:
                self._tail = current.prev
            
            current = current.nxt
            self._length -= 1

    def __getitem__(self, key):
        """return value of the node in 'key' position"""
        if self._length == 0 or key >= self._length or key < -self._length:
            raise IndexError("index out of range")

        if key < 0:
            key = self._length+key

        # Start from head or tail depending of which one is the closest to key
        if key//2 <= self._length:
            pt = self._head
            for _ in range(key):
                pt = pt.nxt
        else:
            pt = self._tail
            for _ in range(self._length-key-1):
                pt = pt.prev
            
        return pt.data

    def __iter__(self):
        self._index = self._head
        return self

    def __next__(self):
        if not self._index:
            raise StopIteration

        data = self._index.data
        self._index = self._index.nxt
        return data

    def __contains__(self, data):
        pt = self._head

        while pt:
            if pt.data == data:
                return True
            pt = pt.nxt

        return False

    def __len__(self):
        return self._length




# Run some more Tests
if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Some tests
    l = LinkedList()

    # Adding and indexing data
    l.add_last(33)

    assert len(l) == 1
    assert l[0] == 33
    assert l[-1] == 33

    l.add_last(55)
    l.add_first(22)

    assert len(l) == 3
    assert l.first == 22
    assert l.last == 55
    assert l[0] == 22
    assert l[1] == 33
    assert l[2] == 55
    assert l[-1] == 55
    assert l[-2] == 33
    assert l[-3] == 22

    # Test removing data
    assert l.remove_first() ==22

    assert len(l) == 2
    assert l[0] == 33
    assert l[1] == 55
    assert l[-1] == 55
    assert l[-2] == 33

    assert l.remove_last() == 55
    assert len(l) == 1
    assert l[0] == 33
    assert l[-1] == 33

    assert l.remove_first() == 33
    assert len(l) == 0

    # Test contains
    l.add_first(444)
    assert len(l) == 1
    assert l[0] == 444
    assert l[-1] == 444

    assert 444 in l
    assert 33 not in l

    l.add_last(33)
    assert 444 in l
    assert 33 in l

    l.remove_last()
    l.remove_last()
    assert 444 not in l
    assert 33 not in l

    # Test remove
    l.add_last(12)
    l.add_last(33)
    l.add_last(12)
    l.add_last(44)
    l.add_last(12)
    
    assert len(l) == 5
    
    l.remove(12)
    assert len(l) == 2
    assert l[0] == 33
    assert l[1] == 44

    l.remove(44)
    assert len(l) == 1
    assert l[-1] == 33

    l.remove(33)
    assert len(l) == 0

    # Test iteration
    l.add_last(1)
    l.add_last(3)
    l.add_last(5)
    assert list(iter(l)) == [1, 3, 5]

    # Remove while iterating
    iter(l)
    assert next(l) == 1
    l.remove(3) 
    assert next(l) == 5
    assert list(iter(l)) == [1, 5]

    # Remove first element iterations
    l = LinkedList()
    l.add_last(1)
    l.add_last(3)
    l.add_last(5)
    
    iter(l)
    l.remove_first()
    assert next(l) == 3
    assert next(l) == 5

    # Remove last element while iterating
    l = LinkedList()
    l.add_last(1)
    l.add_last(3)
    l.add_last(5)
    
    iter(l)
    assert next(l) == 1
    assert next(l) == 3
    l.remove_last()
    assert list(l) == [1, 3]
