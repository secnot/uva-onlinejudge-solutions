# 10069 - Distinct Subsequences

A subsequence of a given sequence is just the given sequence with some elements (possibly none) left
out. Formally, given a sequence X = *x<sub>1</sub>x<sub>2</sub> . . . x<sub>m</sub>*, another sequence 
Z = *z<sub>1</sub>z<sub>2 . . . z<sub>k</sub>* is a subsequence of X if there exists a strictly 
increasing sequence < *i<sub>1</sub>, i<sub>2</sub>, . . . , i<sub>k</sub>* > of indices of X such 
that for all j = 1, 2, . . . , *k*, we have *x<sub>ij</sub> = z<sub>j</sub>* . For example, 
Z = bcdb is a subsequence of X = abcbdab with corresponding index sequence < 2, 3, 5, 7 >.  

In this problem your job is to write a program that counts the number of occurrences of Z in X as
a subsequence such that each has a distinct index sequence.


## Input

The first line of the input contains an integer N indicating the number of test cases to follow. The
first line of each test case contains a string X, composed entirely of lowercase alphabetic characters
and having length no greater than 10,000. The second line contains another string Z having length no
greater than 100 and also composed of only lowercase alphabetic characters. Be assured that neither
Z nor any prefix or suffix of Z will have more than 10100 distinct occurrences in X as a subsequence.


## Output

For each test case in the input output the number of distinct occurrences of Z in X as a subsequence.
Output for each input set must be on a separate line.


## Sample Input

```
2
babgbag
bag
rabbbit
rabbit
```

## Sample Output

```
5
3
```

[\[pdf\]](https://uva.onlinejudge.org/external/100/10069.pdf)
