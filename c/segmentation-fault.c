#include <stdlib.h>

/**
 * segment fault
 */
int main() 
{
  while(++*(int *)0);
}
