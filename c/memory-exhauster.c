#include <stdlib.h>

/**
 * memory exhauster
 */
int main(int argc, char** argv) {
  int* p = malloc(sizeof(long));
  *p = 1;
  while (1) {
    *p = *p + 1;
  }
  return 0;
}
