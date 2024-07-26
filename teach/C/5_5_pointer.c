// 5_5_pointer.c
#include <stdio.h>


// 퀴즈
// 변수 2개의 값을 교환하는 함수를 만드세요 (swap)
void swap(int* p1, int* p2);

int main() {
    int a = 7, b = 3;
    printf("%d %d\n", a, b);

    swap(&a, &b);
    printf("%d %d\n", a, b);

    return 0;
}

void swap(int* p1, int* p2) {
    // int t = p1[0];
    // p1[0] = p2[0];
    // p2[0] = t;

    int t = *p1;
    *p1 = *p2;
    *p2 = t;
}


