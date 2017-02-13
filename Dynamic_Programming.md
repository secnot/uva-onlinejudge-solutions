# Dynamic Programming

Dynamic Programming is an algorithmic paradigm that solves a given complex problem 
by breaking it into subproblems and stores the results of subproblems to avoid computing 
the same results again.
[\[Algorithmist\]](http://www.algorithmist.com/index.php/Dynamic_Programming)
[\[GeeksforGeeks.\]](http://www.geeksforgeeks.org/dynamic-programming-set-1/)  


The classical example on a problem that's best solved using Dynamic Programming is 
Fibonnaci, this is the naive recursive implementation:

```python
def fibonacci(n):
	if n==0: return 0
	elif n==1: return 1
	else: return fibonacci(n-1)+fibonacci(n-2)

```

In my laptop **fibonacci(38)** took 42 seconds to compute. Now if we use Dynamic Programming and 
store the intermediate results we have:

```python
def fibonacci(n, mem={}):
    if n in m:
        return mem[n]
    
    if n==0: fib = 0
    elif n==1: fib = 1
    else: fib = fibonacci(n-1)+fibonacci(n-2)

    mem[n]=fib
    return fib

```

Which computed **fibonacci(38)** in 0.096 seconds more than fast enough in most cases, but sometimes
python's recursion depth limit makes an iterative solution the only alternative:

```python
def fibonacci(n):
	mem = [0 for _ in range(n+1)]
	mem[1] = 1
	for i in range(2, n+1):
		mem[i] = mem[i-1]+mem[i-2]

	return mem[n]
```

With this approach **fibonacci(30000)** took 0.190 seconds to compute.  


The only way to learn how to apply dynnamic progamming is to see how the process work with a few examples, 
and solve problems until it clicks. I recommend the videos below as a starting point.


- [ ] [Algorithms: Memoization and Dynamic Programming (video)](https://www.youtube.com/watch?v=P8Xa2BitN3I)  
- [ ] [MIT 6.006: 19. Dynamic Programming I: Fibonacci, Shortest Path (video)](https://www.youtube.com/watch?v=OQ5jsbhAv_M)  
- [ ] [MIT 6.006: 20. Dynamic Programming II: Text Justification, Blackjack (video)](https://www.youtube.com/watch?v=ENyox7kNKeY)  
- [ ] [MIT 6.006: 21. Dynamic Programming III: Parenthesization, Edit Distance, Knapsack (video)](https://www.youtube.com/watch?v=ocZMDMZwhCY)  
- [ ] [MIT 6.006: 22. Dynamic Programming IV: Guitar Fingering, Tetris, Super Mario Bros.(video)](https://www.youtube.com/watch?v=tp4_UXaVyx8)  
- [ ] [MIT 6.046: Dynamic Programming & Advanced DP (video)](https://www.youtube.com/watch?v=Tw1k46ywN6E&index=14&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)
- [ ] [MIT 6.046: Dynamic Programming: All-Pairs Shortest Paths (video)](https://www.youtube.com/watch?v=NzgFUwOaoIw&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=15)
- [ ] [MIT 6.046: Dynamic Programming (student recitation) (video)](https://www.youtube.com/watch?v=krZI60lKPek&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=12)


## Problems

### Longest Increasing Subsequence (LIS)

The Longest Increasing Subsequence problem is to find a subsequence of a given sequence 
in which all the subsequence's elements are in sorted order.
[\[Wikipedia\]](https://en.wikipedia.org/wiki/Longest_increasing_subsequence)
[\[Algorithmist\]](http://www.algorithmist.com/index.php/Longest_Increasing_Subsequence)
[\[GeeksforGeeks\]](http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/)  

[10154 - Weights and Measures](problems/10154%20-%20Weights%20and%20Measures)  
[10131 - Is Bigger Smarter?](problems/10131%20-%20Is%20Bigger%20Smarter%3F)  
[10261 - Ferry Loading](problems/10261%20-%20Ferry%20Loading)


### Find the longest path in a matrix with contrains

Given a *n×n* matrix where numbers all numbers are distinct and are distributed from range 1 to *n<sup>2</sup>*, 
find the maximum length path (starting from any cell) such that all cells along the path are 
increasing order with a difference of 1.
[\[GeeksforGeeks\]](http://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/)
[\[Youtube\]](https://www.youtube.com/watch?v=lBRtnuxg-gU)  

[116 - Unidirectional TSP](problems/116%20-%20Unidirectional%20TSP)


### Longest Common Subsequence

The longest common subsequence (LCS) problem is the problem of finding the longest subsequence common to all 
sequences in a set of sequences (often just two sequences). It differs from problems of finding common substrings: 
unlike substrings, subsequences are not required to occupy consecutive positions within the original sequences
[\[Algorithmist\]](http://www.algorithmist.com/index.php/Longest_Common_Subsequence)
[\[Wikipedia\]](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem)  

[10069 - Distinct Subsequences](problems/10069%20-%20Distinct%20Subsequences)  


### Recursion with Memoization

Memoization is a technique that is associated with Dynamic Programming. The concept is to cache the result 
of a function given its parameter so that the calculation will not be repeated; it is simply retrieved, 
or memo-ed. Most of the time a simple array is used for the cache table, but a hash table or map 
could also be employed. [\[Algorithmist\]](http://www.algorithmist.com/index.php/Memoization)  

[10003 - Cutting Sticks](problems/10003%20-%20Cutting Sticks) 



## More

- [Quorra: How can one start solving Dynamic Programming problems](https://www.quora.com/How-can-one-start-solving-Dynamic-Programming-problems)
- [GeeksforGeeks: Dynamic Programming](http://www.geeksforgeeks.org/fundamentals-of-algorithms/#DynamicProgramming)
- [StackOverflow; What is difference between memoization and dynamic programming?](http://stackoverflow.com/questions/6184869/what-is-difference-between-memoization-and-dynamic-programming)

