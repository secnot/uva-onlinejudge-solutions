# Data Structures

- [ ] [Wikibook: Data Structures ](https://en.wikibooks.org/wiki/Data_Structures)
- [ ] [Data structures course (43 videos)](https://www.youtube.com/playlist?list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P) (C code)
- [ ] [UC Berkeley 61B (Spring 2014): Data Structures (25 videos)](https://www.youtube.com/watch?v=mFPmKGIrQs4&list=PL-XXv-cvA_iAlnI-BQr9hjqADPBtujFJd) (Java)



## Arrays/Lists

- [Data Structures: List as abstract data type (video)](https://www.youtube.com/watch?v=HdFG8L1sajw&)

#### Problems

[10038 - Jolly Jumpers](problems/10038%20-%20Jolly%20Jumpers)
[10050 - Hartals](problems/10050%20-%20Hartals)


## Linked Lists

- [Wikipedia: Linked list](https://en.wikipedia.org/wiki/Linked_list)
- [Wikipedia: Doubly liked list](https://en.wikipedia.org/wiki/Doubly_linked_list)
- [Coursera: Singly-Linked List (video)](https://www.coursera.org/learn/data-structures/lecture/kHhgK/singly-linked-lists)
- [Coursera: Doubly-Linked List (video)](https://www.coursera.org/learn/data-structures/lecture/jpGKD/doubly-linked-lists)
- [Python: Singly Linked Lists (video)](https://www.youtube.com/watch?v=Ast5sKQXxEU)
- [A python implementation of a doubly linked list (code)](code/llist.py)


## Stacks (LIFO)

- [What is a Stack (video)](https://www.youtube.com/watch?v=FNZ5o9S9prU)
- [Stacks and Queues](https://en.wikibooks.org/wiki/Data_Structures/Stacks_and_Queues)


In python stacks can be implemented using lists:

```python
stack = []

# Push elements into the stack
stack.append(6)
stack.append(2)
stack.append(3)

# Return the value of the last item pushed into the stack
stack[-1] # returns 3

# Remove and returns the last element pushed onto the stack
stack.pop() # returns 3
stack.pop() # returns 2
stack.pop() # returns 6
```

Much easier than with singly linked lists. [(code)](code/stack.py)


## Queues (FIFO)

- [Data Structures: Array Implementation of a Queue (video)](https://www.youtube.com/watch?v=okr-XE8yTO8)
- [Data Structures: Linked List implementation of a Queue (video)] (https://www.youtube.com/watch?v=A5_XdiK4J8A)
 
You can implement your own Queues using one of the methods above, but python standard library already has 
[deque](https://docs.python.org/3/library/collections.html#collections.deque):

```python
from collections import deque

q = deque()

# Equeue item at the end of the queue
q.append(3)
q.append(7)
q.append(6)
q.append(1)

# dequeue item from the front of the queue
q.popleft() # returns 3
q.popleft() # returns 7
```

## Dictionaries

- [Introduction to Hash Tables (video)](https://www.youtube.com/watch?v=MfhjkfocRR0)
- [MIT 6.006: 8. Hashing with Chaining (video)](https://www.youtube.com/watch?v=0M_kIqhwbFo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=8)
- [MIT 6.006: 9. Table Doubling, Karp-Rabin (video)](https://www.youtube.com/watch?v=BRO7mVIFt08&index=9&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)

Dictionaries are a built-in python type but it has two less known subclases that sometimes ares useful:

- [OrderedDict](https://pymotw.com/3/collections/ordereddict.html) is a dictionary subclass that remembers the order in which its contents are added.
[(docs)](https://docs.python.org/3/library/collections.html#collections.OrderedDict)
- [defaultdict](https://pymotw.com/3/collections/defaultdict.html) lets the caller specify the default up front when the container is initialized.
[(docs)](https://docs.python.org/3/library/collections.html#collections.defaultdict)


## Priority Queue


## Videos

- [ ] [UC Berkeley 61B (Spring 2014): Data Structures (25 videos)](https://www.youtube.com/watch?v=mFPmKGIrQs4&list=PL-XXv-cvA_iAlnI-BQr9hjqADPBtujFJd)



## Problems

[10315 - Poker Hands](problems/10315%20-%20Poker%20Hands)
[10010 - Where's Whaldorf?]  
[843 - Crypt Kicker]  
[850 - Crypt Kicker II]  
