#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int fac(int n)
{
    if (n < 2)
        return 1;
    return n * fac(n-1);
}

int main()
{
    printf("4! = %d\n", fac(4));
}