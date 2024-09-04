#include<stdio.h>

int main(void)
{
    int num [] = {20,13,5,1,23,60,40,56,78,12,45,23,56};

    int n = 13;
    for (int i=0; i<13; i++)
    {
        if (num[i]==n)
        {
            printf("found\n");
            return 0;
        }
    }
    printf("Not found\n");
    return 1;

}