# 10037 - Bridge

*n* people wish to cross a bridge at night. A group of at most two people may cross at any time, and
each group must have a flashlight. Only one flashlight is available among the n people, so some sort of
shuttle arrangement must be arranged in order to return the flashlight so that more people may cross.

Each person has a different crossing speed; the speed of a group is determined by the speed of the
slower member. Your job is to determine a strategy that gets all n people across the bridge in the
minimum time.


## Input

The input begins with a single positive integer on a line by itself indicating the number of the cases
following, each of them as described below. This line is followed by a blank line, and there is also a
blank line between two consecutive inputs.

The first line of input contains *n*, followed by n lines giving the crossing times for each of the people.
There are not more than 1000 people and nobody takes more than 100 seconds to cross the bridge.


## Output

For each test case, the output must follow the description below. The outputs of two consecutive cases
will be separated by a blank line.

The first line of output must contain the total number of seconds required for all *n* people to cross
the bridge. The following lines give a strategy for achieving this time. Each line contains either one or
two integers, indicating which person or people form the next group to cross. (Each person is indicated
by the crossing time specified in the input. Although many people may have the same crossing time
the ambiguity is of no consequence.)

Note that the crossings alternate directions, as it is necessary to return the flashlight so that more
may cross. If more than one strategy yields the minimal time, any one will do.


## Sample Input

```bash
1
4
1
2
5
10
```


## Sample Output

```bash
17
1 2
1
5 10
2
1 2
```

[\[pdf\]](https://uva.onlinejudge.org/external/100/10037.pdf)  
