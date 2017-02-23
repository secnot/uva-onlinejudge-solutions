# 10157 - Expressions

Let X be the set of correctly built parenthesis expressions. The elements of X are strings consisting only
of the characters ‘(’ and ‘)’. The set X is defined as follows:

- an empty string belongs to X
- if A belongs to X, then (A) belongs to X
- if both A and B belong to X, then the concatenation AB belongs to X.

For example, the following strings are correctly built parenthesis expressions (and therefore belong
to the set X):

```
()(())()
(()(()))
```

The expressions below are not correctly built parenthesis expressions (and are thus not in X):

```
(()))(()
())(()
```

Let E be a correctly built parenthesis expression (therefore E is a string belonging to X).
The length of E is the number of single parenthesis (characters) in E.
The depth D(E) of E is defined as follows:

```
       | 0 if E is empty
D(E) = | D(A) + 1 if E = (A), and A is in X
       | max(D(A), D(B)) if E = AB, and A, B are in X
```

For example, the length of “()(())()” is 8, and its depth is 2. What is the number of correctly
built parenthesis expressions of length n and depth d, for given positive integers n and d?
Write a program which
- reads two integers n and d
- computes the number of correctly built parenthesis expressions of length n and depth d;

## Input

Input consists of lines of pairs of two integers - n and d, at most one pair on line, 2 ≤ *n* ≤ 300,
1 ≤ *d* ≤ 150.  
The number of lines in the input file is at most 20, the input may contain empty lines, which you
don’t need to consider.


## Output

For every pair of integers in the input write single integer on one line - the number of correctly built
parenthesis expressions of length n and depth d.
Note: There are exactly three correctly built parenthesis expressions of length 6 and depth 2:
(())()
()(())
(()())


## Sample Input

```
6 2
300 150
```


## Sample Output

```
3
1
```

[\[pdf\]](https://uva.onlinejudge.org/external/101/10157.pdf)
