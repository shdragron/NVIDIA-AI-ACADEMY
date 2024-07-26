// 3_1_function.c
#include <stdio.h>

int add(int a, int b);
int max_2(int a, int b);

// 전역 변수 : 내가 만들지 않았지만, 사용할 수 있는 변수
// 지역 변수 : 내가 만든 변수
int global = 123;

int main() {
    printf("%d\n", add(3, 7));

    int a = 3, b = 7;
    int c = add(a, b);
    printf("%d\n", a);

    if (a % 2) {
        int k = 9;
        k += 9;
    }

    global += 99;

    printf("max : %d\n", max_2(3, 7));
    printf("max : %d\n", max_2(7, 3));
    printf("max : %d\n", max_2(7, 7));
    return 0;
}

// 퀴즈
// 두 개의 정수 중에서 큰 숫자를 찾는 함수를 만드세요
int add(int a, int b) {
    a = 99;
    return a + b;
}

int max_2(int a, int b) {
    // 그냥
    // if (a > b)
    //     return a;
    // else
    //     return b;

    // 그냥
    // if (a > b)
    //     return a;

    // return b;

    // 고수
    if (a > b)
        b = a;

    return b;
}





