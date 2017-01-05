# 10152 - ShellSort

*He made each turtle stand on another one’s back
And he piled them all up in a nine-turtle stack.
And then Yertle climbed up. He sat down on the pile.
What a wonderful view! He could see ’most a mile!*

King Yertle wishes to rearrange his turtle throne to place his highest-ranking nobles and closest
advisors nearer to the top. A single operation is available to change the order of the turtles in the
stack: a turtle can crawl out of its position in the stack and climb up over the other turtles to sit on
the top.
Given an original ordering of a turtle stack and a required ordering for the same turtle stack, your
job is to determine a minimal sequence of operations that rearranges the original stack into the required
stack.


## Input

The first line of the input consists of a single integer *K* giving the number of test cases. Each test
case consist on an integer n giving the number of turtles in the stack. The next *n* lines specify the
original ordering of the turtle stack. Each of the lines contains the name of a turtle, starting with the
turtle on the top of the stack and working down to the turtle at the bottom of the stack. Turtles have
unique names, each of which is a string of no more than eighty characters drawn from a character set
consisting of the alphanumeric characters, the space character and the period (‘.’). The next n lines
in the input gives the desired ordering of the stack, once again by naming turtles from top to bottom.
Each test case consists of exactly *2n + 1* lines in total. The number of turtles (*n*) will be less than or
equal to two hundred.


## Output

For each test case, the output consists of a sequence of turtle names, one per line, indicating the order in
which turtles are to leave their positions in the stack and crawl to the top. This sequence of operations
should transform the original stack into the required stack and should be as short as possible. If more
than one solution of shortest length is possible, any of the solutions may be reported.
Print a blank line after each test case.


## Sample Input

```bash
2
3
Yertle
Duke of Earl
Sir Lancelot
Duke of Earl
Yertle
Sir Lancelot
9
Yertle
Duke of Earl
Sir Lancelot
Elizabeth Windsor
Michael Eisner
Richard M. Nixon
Mr. Rogers
Ford Perfect
Mack
Yertle
Richard M. Nixon
Sir Lancelot
Duke of Earl
Elizabeth Windsor
Michael Eisner
Mr. Rogers
Ford Perfect
Mack
```

## Sample Output

```bash
Duke of Earl

Sir Lancelot
Richard M. Nixon
Yertle
```
