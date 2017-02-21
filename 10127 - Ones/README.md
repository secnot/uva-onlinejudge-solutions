# 10127 - Ones

Given any integer 0 ≤ *n* ≤ 10000 not divisible by 2 or 5, some multiple of *n* 
is a number which in decimal notation is a sequence of 1’s. How many digits are 
in the smallest such a multiple of *n*?


## Input

A file of integers at one integer per line.


## Output

Each output line gives the smallest integer x > 0 such that 
p = $\sum_{i=0}^{x-1} t_i$ 1×10<sup>i</sup> = a×b, where a is the corresponding 
input integer, and b is an integer greater than zero.


## Sample Input

```
3
7
9901
```


## Sample Output

```
3
6
12
```

[\[pdf\]](https://uva.onlinejudge.org/external/101/10127.pdf)
