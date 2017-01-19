#include <stdio.h>
#include <math.h>

#define MAX_NUMBERS 10000
#define MAX_DIVISOR 100
int num[MAX_NUMBERS];
int rem[MAX_NUMBERS][MAX_DIVISOR];


void load_case(int *n, int *k) {
	int i, j;
	scanf("%d %d", n, k);

	/* Initialize arrays */
	for (i=0; i<*n; i++)
		for (j=0; j<*k; j++)
			rem[i][j] = 0;

	/* Load case numbers */
	for (i=0; i<*n; i++) {
		scanf("%d", &num[i]);	
		num[i] = abs(num[i]);
	}
}


int is_divisible(int n, int k) {
	int i, j;

	rem[0][num[0]%k] = 1;
	for (i=1; i<n; i++)
		for (j=0; j<k; j++)
			if (rem[i-1][j]) {
				rem[i][(j+num[i])%k]=1;
				rem[i][(j+k-num[i])%k]=1;
			}

	return rem[n-1][0];
}


int main(int argc, char *argv[]) {

	int cases, c;
	int n, k;
	scanf("%d",&cases);
	
	for(c=0; c<cases; c++) {
		load_case(&n, &k);
		if(is_divisible(n, k))
			printf("Divisible\n");
		else
			printf("Not divisible\n");
	}
}
