# 10249 - The Grand Dinner

Each team participating in this year’s **ACM World Finals** contest is expected to join the grand dinner
to be arranged after the prize giving ceremony ends. In order to maximize the interaction among the
members of different teams, it is expected that no two members of the same team sit at the same table.

Now, given the number of members in each team (including contestants, coaches, reserves, guests
etc.) and the seating capacity of each available table, you are to determine whether it is possible for
the teams to sit as described in the previous paragraph. If such an arrangement is possible you must
also output one possible seating arrangement. If there are multiple possible arrangements, any one is
acceptable.


## Input

The input file may contain multiple test cases. The first line of each test case contains two integers
*M* (1 ≤ *M* ≤ 70) and *N* (1 ≤ *N* ≤ 50) denoting the number of teams and the number of tables
respectively. The second line of the test case contains *M* integers where the *i*-th (1 ≤ *i* ≤ *M*) integer
mi (1 ≤ *m<sub>i</sub>* ≤ 100) indicates the number of members of team *i*. The third line contains *N* integers
where the *j*-th (1 ≤ *j* ≤ N) integer *n<sub>j</sub>* (2 ≤ *n<sub>j</sub>* ≤ 100) indicates the seating capacity of table *j*.
A test case containing two zeros for *M* and *N* terminates the input.


## Output

For each test case in the input print a line containing either 1 or 0 depending on whether or not there
exists a valid seating arrangement of the team members. In case of a successful arrangement print M
additional lines where the *i*-th (1 ≤ *i* ≤ *M*) of these lines contains a table number (an integer from 1
to *N*) for each of the members of team *i*.


## Sample Input

```
4 5
4 5 3 5
3 5 2 6 4
4 5
4 5 3 5
3 5 2 6 3
0 0
```


## Sample Output

```
1
1 2 4 5
1 2 3 4 5
2 4 5
1 2 3 4 5
0
```
