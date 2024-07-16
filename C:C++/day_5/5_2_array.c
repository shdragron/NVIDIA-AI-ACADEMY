// 5_2_array.c
#include <stdio.h>

char reverse(char c[], int size);
void show_arry(char a[], int size);

int main(){
    char s[7] = { 'A', 'B', 'C', 'D', 'E', 'F', 'G'};
    reverse(s, sizeof(s)/sizeof(s[0]));
    show_arry(s,sizeof(s)/sizeof(s[0]));
    return 0;
}
// 퀴즈 배열을 거꾸로 뒤집는 함수를 만드세요.

void show_arry(char a[], int size){
    int i = 0;
    for (i = 0; i < size; i++)
    {
        putchar(a[i]);
    }
    printf("\n");
}

char reverse(char c[], int size){
    
    int i = 0;
    char a[size];
    for (i = 0; i < size; i++)
    {
        a[i] = c[size - i - 1];

    }
    for (i = 0; i < size; i++)
    {
        c[i] = a[i];
    }
}