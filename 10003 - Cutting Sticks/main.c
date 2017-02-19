#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>

#define min(a,b) \
	({ __typeof__ (a) _a = (a); \
	 __typeof__ (b) _b = (b); \
	 _a < _b ? _a : _b; })

#define MAX_CUTS 50
#define MAX_LENGTH 1000

int mem[MAX_CUTS+2][MAX_CUTS+2];
int cuts[MAX_CUTS+2];
int ncuts = 0;

int load_stick(void){
	/* Load next stick problem */
	int length, i;
	
	scanf("%d", &length);
	if (length==0)
		return 0;

	scanf("%d", &ncuts);
	for(i=0; i<ncuts; i++)
		scanf("%d", &cuts[i+1]);
	cuts[ncuts+1]=length;
	cuts[0]=0;
	ncuts+=2;
	return 1;
}



int cost(s, e) {
	int i, best_cost=INT_MAX;

	if (mem[s][e] >= 0)
		return mem[s][e];

	for(i=s+1; i<e; i++)
		best_cost = min(cost(s,i)+cost(i,e), best_cost);

    return mem[s][e] = best_cost + cuts[e] - cuts[s];
}

int min_cost(void) {
	short i;

	/* Initialize array from last stick */
	memset(mem, -1, sizeof(mem));	
	for(i=0; i<ncuts; i++) 
	   mem[i][i+1] = 0;

	/* Find minimum cost */
	return cost(0, ncuts-1);
}



int main(int argc, char *argv[]) {
	while(load_stick())
		printf("The minimum cutting is %d.\n", min_cost());
}
