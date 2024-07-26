// 5_2_array.c
#include <stdio.h>


void show_array(char a[], int size);
void reverse_array(char a[], int size);
void show_string(char a[], int size);

// 퀴즈
// 배열을 거꾸로 뒤집는 함수를 만드세요 (reverse_array)

int main() {
    char s[7] = {'A', 'B', 'C', 'D', 'E', 'F', 'G'};
    show_array(s, 7);

    reverse_array(s, 7);
    show_array(s, 7);
    show_string(s, 7);

    return 0;
}

void show_array(char a[], int size) {
    for (int i = 0; i < size; i++)
        putchar(a[i]);
    printf("\n");
}

void show_string(char a[], int size) {
    // 퀴즈
    // 배열 표현을 포인터 표현으로 수정하세요
    for (int i = 0; i < size; i++)
        putchar(*(a+i));
    printf("\n");

    // for (int i = 0; i < size; i++)
    //     putchar(*a++);
    // printf("\n");

    char *p = a + size;
    while (a < p)
        putchar(*a++);
    printf("\n");
}

void reverse_array(char a[], int size) {
    // for (int i = size-1; i >= 0; i--)
    //     putchar(a[i]);
    // putchar('\n');

    // 0 1 2 3 4 5 6
    // 6 5 4 3 2 1 0
    // 6 6 6 6 6 6 6
    // for (int i = 0; i < size; i++)
    //     putchar(a[size-1-i]);
    // putchar('\n');

    // char p[size];
    // for (int i = 0; i < size; i++)
    //     // p[i] = a[size-1-i];
    //     p[size-1-i] = a[i];

    // for (int i = 0; i < size; i++)
    //     a[i] = p[i];

    // 0 <-> 6
    // 1 <-> 5
    // 2 <-> 4
    // 3 <-> 3
    char t;
    // for (int i = 0; i < size / 2; i++) {
    //     t = a[i];
    //     a[i] = a[size-1-i];
    //     a[size-1-i] = t;
    // }

    // for (int i = 0; i < size / 2; i++) {
    //     t = *(a+i);
    //     *(a+i) = *(a+size-1-i);
    //     *(a+size-1-i) = t;
    // }

    char* p = a + size - 1;
    while (a < p) {
        t = *a;
        *a = *p;
        *p = t;
        a++, p--;
    }
}
