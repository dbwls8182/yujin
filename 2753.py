#include<studio.h>

int main(void)
{
    int year;
    scanf("%d", &year);

    bool r;
    r = ((year % 4 ==0 && year % 100) || year % 400==0) ? 1 : 0 
    printf("%d\n", r);
    return 0;
}