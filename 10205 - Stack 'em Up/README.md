# 10205 - Stack 'em Up

A standard playing card deck contains 52 cards, 13 values in each of four suits. The 
values are named *2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace*. The suits are named
*Clubs, Diamonds, Hearts, Spades*. A particular card in the deck can be uniquely identified 
by its value and suit, typically denoted < *value* > of < *suit* >. For example, “9 of Hearts”
or “King of Spades”. Traditionally a new deck is ordered first alphabetically by suit, then 
by value in the order given above.  

The Big City has many Casinos. In one such casino the dealer is a bit crooked. She has perfected
several shuffles; each shuffle rearranges the cards in exactly the same way whenever it is used. A very
simple example is the “bottom card” shuffle which removes the bottom card and places it at the top.
By using various combinations of these known shuffles, the crooked dealer can arrange to stack the
cards in just about any particular order.  

You have been retained by the security manager to track this dealer. You are given a list of all the
shuffles performed by the dealer, along with visual cues that allow you to determine which shuffle she
uses at any particular time. Your job is to predict the order of the cards after a sequence of shuffles.


## Input

The input begins with a single positive integer on a line by itself indicating the number of the cases
following, each of them as described below. This line is followed by a blank line, and there is also a
blank line between two consecutive inputs.  

Input consists of an integer *n* ≤ 100, the number of shuffles that the dealer knows. 52*n* integers
follow. Each consecutive 52 integers will comprise all the integers from 1 to 52 in some order. Within
each set of 52 integers, *i* in position *j* means that the shuffle moves the *i*-th card in the deck 
to position *j*.  

Several lines follow; each containing an integer k between 1 and n indicating that you have observed
the dealer applying the *k*-th shuffle given in the input.


## Output

For each test case, the output must follow the description below. The outputs of two consecutive cases
will be separated by a blank line.  
Assume the dealer starts with a new deck ordered as described above. After all the shuffles had
been performed, give the names of the cards in the deck, in the new order.


## Sample Input

```
1

2
2 1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 
28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 52 51
52 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 
28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 1
1
2
```


## Sample Output

```
King of Spades
2 of Clubs
4 of Clubs
5 of Clubs
6 of Clubs
7 of Clubs
8 of Clubs
9 of Clubs
10 of Clubs
Jack of Clubs
Queen of Clubs
King of Clubs
Ace of Clubs
2 of Diamonds
3 of Diamonds
4 of Diamonds
5 of Diamonds
6 of Diamonds
7 of Diamonds
8 of Diamonds
9 of Diamonds
10 of Diamonds
Jack of Diamonds
Queen of Diamonds
King of Diamonds
Ace of Diamonds
2 of Hearts
3 of Hearts
4 of Hearts
5 of Hearts
6 of Hearts
7 of Hearts
8 of Hearts
9 of Hearts
10 of Hearts
Jack of Hearts
Queen of Hearts
King of Hearts
Ace of Hearts
2 of Spades
3 of Spades
4 of Spades
5 of Spades
6 of Spades
7 of Spades
8 of Spades
9 of Spades
10 of Spades
Jack of Spades
Queen of Spades
Ace of Spades
3 of Clubs
```

[\[pdf\]](https://uva.onlinejudge.org/external/102/10205.pdf)
