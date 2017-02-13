# Data Structures


## Linked Lists

- [Wikipedia: Linked list](https://en.wikipedia.org/wiki/Linked_list)
- [Wikipedia: Doubly liked list](https://en.wikipedia.org/wiki/Doubly_linked_list)
- [A python implementation of a double linked list (code)](code/llist.py)
- [Coursera: Singly-Linked List (video)](https://www.coursera.org/learn/data-structures/lecture/kHhgK/singly-linked-lists)
- [Coursera: Doubly-Linked List (video)](https://www.coursera.org/learn/data-structures/lecture/jpGKD/doubly-linked-lists)
- [Python: Singly Linked Lists (video)](https://www.youtube.com/watch?v=Ast5sKQXxEU)


## Stacks (LIFO)

[What is a Stack (video)](https://www.youtube.com/watch?v=FNZ5o9S9prU)
[Stacks and Queues](https://en.wikibooks.org/wiki/Data_Structures/Stacks_and_Queues)


In python stacks can be easily implemente using lists:

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

# Queues (FIFO)

For Queues python has [deque](https://docs.python.org/2/library/collections.html#collections.deque) 
from **collections** module:

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


## Priority Queue


## Videos

- [ ] [UC Berkeley 61B (Spring 2014): Data Structures (25 videos)](https://www.youtube.com/watch?v=mFPmKGIrQs4&list=PL-XXv-cvA_iAlnI-BQr9hjqADPBtujFJd)



## Problems


[10010 - Where's Whaldorf?]  
[10038 - Jolly Jumpers]  
[843 - Crypt Kicker]  
[850 - Crypt Kicker II]  
