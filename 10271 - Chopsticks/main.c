#include <stdio.h>
#include <math.h>
#include <limits.h>
#define INFINITE INT_MAX

#ifndef SWAP
	#define SWAP(type, a, b) \
	{ \
		type temp = a; \
		a = b; \
		b = temp; \
	}
#endif
#define MIN(a,b) (((a) < (b))?(a):(b))
#define MAX(a,b) (((a) > (b))?(a):(b))


int DP[1010][5001], L[5001], bad[5001];


void reverse(int *array, const size_t length) {
	int i;
   	for (i = 0; i < length/2; ++i)
		SWAP(int, array[i], array[length - i - 1]);
}


int find_best(const int k, const int n) {	
	int i, j;	

	reverse(L+1, n);
	for(i = 2; i <= n; i++)
		bad[i] = (L[i]-L[i-1])*(L[i]-L[i-1]);

	for(i = 0; i<=n; i++)
		DP[0][i] = 0;
	
	for(i = 1; i <= k; i++){
        DP[i][3*i-1] = INFINITE;
		for(j = 3*i; j <= n-abs(i-k)*2+1; j++)
			DP[i][j] = MIN(DP[i][j-1], DP[i-1][j-2]+bad[j]);
	}

	return DP[k][n];
}


int main() {
	int ncases, n, k, i;
	
	scanf("%d", &ncases);

	while(ncases--) {
		scanf("%d %d", &k, &n);
		for(i = 1; i <= n; i++)
			scanf("%d", &L[i]);

		k += 8;
		printf("%d\n", find_best(k, n));
	}
    return 0;
} 
