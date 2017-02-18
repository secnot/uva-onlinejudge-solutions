from sys import stdin
from collections import Counter

CATEGORIES = 13


#   IO Functions (read cases on stdin)
#############################################

def readnum():
    return list(map(int, stdin.readline().split()))

def readgame():
    return [readnum() for _ in range(13)]



# Dice rating functions: A bunch of boilerplate
# to precompute all possible scores for each game
#################################################

def ones(dices): 
    # 0 -> Sum of all ones thrown
    return sum(d for d in dices if d == 1)

def twos(dices): 
    #1 -> Sum of all twos thrown
    return sum(d for d in dices if d == 2)

def threes(dices): 
    #2 -> Sum of all Threes
    return sum(d for d in dices if d == 3)

def fours(dices):
    #3 -> sum of all fours
    return sum(d for d in dices if d == 4)

def fives(dices): 
    #4 -> sum of all fives
    return sum(d for d in dices if d == 5)

def sixes(dices): 
    #5 - > sum of all sixes
    return sum(d for d in dices if d == 6)

def chance(dices): 
    #6 -> sum of all dices
    return sum(dices)

def three_kind(dices): 
    #7 ->  sum of all dice, provided at least three have same value
    count = Counter(dices)
    if max(count.values())>=3:
        return sum(dices)
    else:
        return 0

def four_kind(dices): 
    #8 ->  sum of all dice, provided at least four have same value
    count = Counter(dices)
    if max(count.values())>=4:
        return sum(dices)
    else:
        return 0

def five_kind(dices): 
    #9 ->  sum of all dice, provided at least five have same value
    #if dices[0]==dices[1]==dices[2]==dices[3]==dices[4]:
    count = Counter(dices)
    if max(count.values())>=5:
        return 50
    else:
        return 0

def short_straight(dices): 
    #10 -> 25 points, provided four of the dice form a sequence 
    #(that is, 1,2,3,4 or 2,3,4,5 or 3,4,5,6)
    count = Counter(dices)

    if len(count) == 5:
        return 25
    if len(count) >= 4 and (3 in count and 4 in count):
        if  (1 in count and 2 in count) or\
            (2 in count and 5 in count) or\
            (5 in count and 6 in count): 
            return 25
    
    return 0

def long_straight(dices): 
    #11 -> 35 points, provided all dice form a sequence (1,2,3,4,5 or 2,3,4,5,6)
    count = Counter(dices)
    if len(count)==5 and 2 in count and 3 in count and 4 in count and 5 in count:
        if 1 in count or 6 in count:
            return 35
        
    return 0

def full_house(dices): 
    #12 -> - 40 points, provided three of the dices are equal and the other 
    #two dices are also equal. (for example, 2,2,5,5,5)
    count = Counter(dices)
    if (len(count) == 2 and max(count.values())==3) or len(count)==1:
        return 40
    else:
        return 0


RATE_FUNCS = [ones, twos, threes, fours, fives, sixes, chance, three_kind, 
        four_kind, five_kind, short_straight, long_straight, full_house]

def build_score_table(game):
    """Build a table with the score for all the categories for each round"""
    # Generate point table for all categories for each round
    return [[func(round) for func in RATE_FUNCS] for round in game]




# Search Functions
# 
# Find best score using Dynamic Programming, in this case recursion + memoization
#
# MaxScore(round0, None) = max(
#       rating_cat0 in round0 + MaxScore(round1, except cat0),
#       rating_cat1 in round0 + MaxScore(round1, except cat1),
#       .....
#       rating_cat12 in round0 + MaxScore(round1, except cat12))
#################################################################################

def MaxScore(round, free_cat, prev6score, mem, score_table):
    """
    Arguments:
        round (int): Current round (from 0 to 13)
        free_cat (list): List of booleans (length 13), if free_cat[i]=True 
            the category i hasn't been used yet.
        prev6score: sum of the first 6 categories scores (used until this round) 
        mem (dict): Memoization dictionary
        score_table(2d array): Precomputed table with all possible round scores

    Returns:
        int: bestscore
        int: first_ 6 categories score
        int: next category

    """
    if round==13:
        return 0, 0, 0

    # Return stored value if available.
    try:
        return mem[round, tuple(free_cat)]
    except KeyError:
        pass

    # Find best score for the round using the free categories remainig.
    scores = []
    for cat, free in enumerate(free_cat):
        if not free:
            continue

        # Score for the category used this round
        cat_score = score_table[round][cat]

        # Sum of the scores for the 6 first categories used until now
        current6score = prev6score+cat_score if cat<6 else prev6score

        # Best score and category for the remaining categories in the next round
        free_cat[cat]=False 
        rest_score, rest6score, _ = MaxScore(round+1, free_cat, current6score, mem, score_table) 
        free_cat[cat]=True
       
        fullscore = cat_score+rest_score        # full score for this category
        full6score = current6score+rest6score   # Full score for first 6 categories

        # Need to add 35 bonus to the score??
        bonus = 35 if full6score>=63 else 0
        scores.append((fullscore+bonus, fullscore, full6score-prev6score, cat))
    
    # Memoize result
    _, bestscore, best6score, cat = max(scores)
    mem[(round, tuple(free_cat))] = (bestscore, best6score, cat)
    return (bestscore, best6score, cat)


def find_best_score(game):

    # precompute all possible scores
    score_table = build_score_table(game)
    
    # Find best score
    mem = {}
    total_score, first6score, first_cat = MaxScore(0, [True]*CATEGORIES, 0, mem, score_table)
    bonus = 35 if first6score>=63 else 0
  
    # Reconstruct category list
    score = []
    cat_free = [True]*CATEGORIES

    while len(score)<13:
        best_score, first6score, cat = mem[(len(score), tuple(cat_free))]
        cat_free[cat]=False
        score.append((cat, score_table[len(score)][cat]))
        

    score = [value for cat, value in sorted(score)]
    return score, bonus, total_score+bonus


if __name__ == '__main__':

    while True:
        game = readgame()
        if len(game[0]) == 0:
            break
        score, bonus, total = find_best_score(game)
        print(" ".join(map(str, score)), bonus, total)
