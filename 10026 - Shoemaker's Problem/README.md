# 10026 - Shoemaker's Problem

Shoemaker has *N* jobs (orders from customers) which he must make. Shoemaker can work on only
one job in each day. For each *i*-th job, it is known the integer *T<sub>i</sub>* (1 ≤ *T<sub>i</sub>* ≤ 1000), 
the time in days it takes the shoemaker to finish the job. For each day of delay before starting to work 
for the *i*-th job, shoemaker must pay a fine of *S<sub>i</sub>* (1 ≤ *S<sub>i</sub>* ≤ 10000) cents. 
	Your task is to help the shoemaker, writing a programm to find the sequence of jobs with minimal total fine.

## Input

**The input begins with a single positive integer on a line by itself indicating the number
of the cases following, each of them as described below. This line is followed by a blank
line, and there is also a blank line between two consecutive inputs.**
First line of input contains an integer *N* (1 ≤ *N* ≤ 1000). The next *N* lines each contain two
numbers: the time and fine of each task in order.


## Output

**For each test case, the output must follow the description below. The outputs of two
consecutive cases will be separated by a blank line.**
You programm should print the sequence of jobs with minimal fine. Each job should be represented
by its number in input. All integers should be placed on only one output line and separated by one
space. If multiple solutions are possible, print the first lexicographically.


## Sample Input

```bash
1

4
3 4
1 1000
2 2
5 5
```


## Sample Output

```bash
2 1 3 4
```
