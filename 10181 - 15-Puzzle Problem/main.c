#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>

#define MIN(a,b) (((a)<(b))?(a):(b))

#define PUZZLE_SIZE 16
#define MAX_MOVES 100

short puzzle[PUZZLE_SIZE];
char moves[MAX_MOVES];

static short MANHATTAN_DST[PUZZLE_SIZE][PUZZLE_SIZE] = {
    {0, 0, 1, 2, 3, 1, 2, 3, 4, 2, 3, 4, 5, 3, 4, 5},
    {0, 1, 0, 1, 2, 2, 1, 2, 3, 3, 2, 3, 4, 4, 3, 4},
    {0, 2, 1, 0, 1, 3, 2, 1, 2, 4, 3, 2, 3, 5, 4, 3},
    {0, 3, 2, 1, 0, 4, 3, 2, 1, 5, 4, 3, 2, 6, 5, 4},
    
    {0, 1, 2, 3, 4, 0, 1, 2, 3, 1, 2, 3, 4, 2, 3, 4},
    {0, 2, 1, 2, 3, 1, 0, 1, 2, 2, 1, 2, 3, 3, 2, 3},
    {0, 3, 2, 1, 2, 2, 1, 0, 1, 3, 2, 1, 2, 4, 3, 2},
    {0, 4, 3, 2, 1, 3, 2, 1, 0, 4, 3, 2, 1, 5, 4, 3},

    {0, 2, 3, 4, 5, 1, 2, 3, 4, 0, 1, 2, 3, 1, 2, 3},
    {0, 3, 2, 3, 4, 2, 1, 2, 3, 1, 0, 1, 2, 2, 1, 2},
    {0, 4, 3, 2, 3, 3, 2, 1, 2, 2, 1, 0, 1, 3, 2, 1},
    {0, 5, 4, 3, 2, 4, 3, 2, 1, 3, 2, 1, 0, 4, 3, 2},

    {0, 3, 4, 5, 6, 2, 3, 4, 5, 1, 2, 3, 4, 0, 1, 2},
    {0, 4, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3, 1, 0, 1},
    {0, 5, 4, 3, 4, 4, 3, 2, 3, 3, 2, 1, 2, 2, 1, 0},
    {0, 6, 5, 4, 3, 5, 4, 3, 2, 4, 3, 2, 1, 3, 2, 1}};



short manhattan_dist(short *puzzle) {
	/* Manhattan distance heuristic */
	short i=0, sum=0;
	for (i=0; i<PUZZLE_SIZE; i++) {
		sum += MANHATTAN_DST[i][puzzle[i]];	
	}
	return sum;
}

/* Find moving tile positon*/
short find_pos(short *puzzle) {
	short i;
	for (i=0; i<PUZZLE_SIZE; i++)
		if (puzzle[i]==0)
			return i;
} 
void move_up(short *puzzle) {
	short temp, pos = find_pos(puzzle);
	temp = puzzle[pos];
	puzzle[pos] = puzzle[pos-4];
	puzzle[pos-4] = temp;
}
void move_down(short *puzzle) {	
	short temp, pos = find_pos(puzzle);
	temp = puzzle[pos];
	puzzle[pos] = puzzle[pos+4];
	puzzle[pos+4] = temp;
}
void move_left(short *puzzle) {
	short temp, pos = find_pos(puzzle);
	temp = puzzle[pos];
	puzzle[pos] = puzzle[pos-1];
	puzzle[pos-1] = temp;
}
void move_right(short *puzzle) {
	short temp, pos = find_pos(puzzle);
	temp = puzzle[pos];
	puzzle[pos] = puzzle[pos+1];
	puzzle[pos+1] = temp;
}


short num_inversions(short *puzzle) {
   	short i, j;
	short result = 0;

    for (i=0; i<PUZZLE_SIZE; i++) {
        for (j=i+1;  j<PUZZLE_SIZE; j++) {
            if (puzzle[i] == 0 || puzzle[j] == 0)
                continue;

            if (puzzle[i] > puzzle[j])
                result += 1;
		}
	}
    return result;
}


short is_solvable(short *puzzle) {
    short pos = find_pos(puzzle);
   	short count = num_inversions(puzzle);

    if ((4 - pos/4) % 2 == 0)
        return count % 2 == 1;
    else
        return count % 2 == 0;
}


short is_solved(short *puzzle) {
	return manhattan_dist(puzzle)==0;
}


/* Load puzzle from stdin*/
void load_puzzle(short *puzzle) {
	int i;
	for (i=0; i<PUZZLE_SIZE; i++)
		scanf("%d", puzzle+i);
}


short dfs(short *puzzle, short limit, short nmoves, char prev_move) {

	short pos = find_pos(puzzle);
	short heuristic, mov;

	heuristic = manhattan_dist(puzzle);
	if (heuristic == 0)
		return nmoves;

	if (heuristic+nmoves+1 >= limit)
		return -1;

	/* Up */
	if (prev_move != 'D' && pos/4!=0) {
		move_up(puzzle);
		moves[nmoves] = 'U';
		mov = dfs(puzzle, limit, nmoves+1, 'U');
		if (mov >= 0)
			return mov;
		move_down(puzzle);
	}

	/* Down */	
	if (prev_move != 'U' && pos/4!=3) {
		move_down(puzzle);
		moves[nmoves] = 'D';
		mov = dfs(puzzle, limit, nmoves+1, 'D');
		if (mov >= 0)
			return mov;
		move_up(puzzle);
	}
	
	/* Left */
	if (prev_move != 'R' && pos%4!=0) {
		move_left(puzzle);
		moves[nmoves] = 'L';
		mov = dfs(puzzle, limit, nmoves+1, 'L');
		if (mov >= 0)
			return mov;
		move_right(puzzle);
	}

	/* Right */
	if (prev_move != 'L' && pos%4!=3) {
		move_right(puzzle);
		moves[nmoves] = 'R';
		mov = dfs(puzzle, limit, nmoves+1, 'R');
		if (mov >= 0)
			return mov;
		move_left(puzzle);
	}

	/* Failed */	
	return -1;
}

short solve_puzzle(short *puzzle, short limit) {
	short max_cost, moves;
	short puzzle_copy[PUZZLE_SIZE];

	memcpy(puzzle_copy, puzzle, sizeof(puzzle_copy));

	/* Check it can be solved and hasn't been solved */
	if (is_solved(puzzle))
		return 0;

	if (!is_solvable(puzzle))
		return -1;
	
	/* Keep raising search depth until solution is found or limit reached. */
	max_cost = manhattan_dist(puzzle);

	while (max_cost <= limit) {
			memcpy(puzzle_copy, puzzle, sizeof(puzzle_copy));
			
            moves = dfs(puzzle_copy, max_cost, 0, ' ');

            if (moves<0)
				if (max_cost == limit)
					break;
				else
					max_cost = MIN(limit, max_cost+5);
            else
                return moves;
	}

	return -1;
}


int main(int argc, char *argv[]){
	short ncases, c;
	short sol_moves = 0;
	int i;

	scanf("%d", &ncases);

	for (c=0; c<ncases; c++) {
		load_puzzle(puzzle);
		sol_moves = solve_puzzle(puzzle, 50);
		if (sol_moves<0)
            printf("This puzzle is not solvable.\n");
		else {
			moves[sol_moves]=0;
			printf("%s\n", moves);
		}
	}
	return;
}
