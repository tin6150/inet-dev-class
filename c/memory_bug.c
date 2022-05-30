#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv){
  int i;
  int x =0;
  int a[10];

  // ubuntu gcc 5.4 produced a.out complain of memory smashing and abort
  //for (i = 0; i < 11; i++)
  for (i = 0; i < 10; i++) {
    //printf("i is %d , a[i] has value\n", i);
    a[i] = i;
    printf("i is %d , a[i] has value %d\n", i, a[i]);
    // when a[10] is accessed, it is out of bound array.  x getting 10 likely old implementation bug
  }
  printf("======\n" );
  printf("x is %d\n", x);
  return 0;
}

// http://pages.cs.wisc.edu/~bart/537/valgrind.html
// said x will be 10, intead of expecting to be zero, and this kind of static memory error won't be detected by valgrind
// which only check for dynamic alloc by malloc()

