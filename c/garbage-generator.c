#include <stdlib.h>

/**
 * garbage generator 
 */
int main() 
{
	int i,j;
	char *garbage;
	for(i=0;i<10;i++)
	{
		garbage = calloc(1,10);
		for(j=0;j<10;j++)
		{
			garbage[j] = 'a'+rand()%26;
		}
		free(garbage);
	}
}
