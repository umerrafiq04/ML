#include<stdio.h>
int main(){
    int x=12;
    int *y=&x;
    int **z=&y;
    printf("%u",y);
    printf("%u",z);


}