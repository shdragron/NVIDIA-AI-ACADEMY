// 3_2_while.c
#include <stdio.h>

void f_1();
void f_2();

int main() {
    f_2();
    return 0;
}

void f_1() {
    // 0 1 2 3 4        0, 5, 1         [0, 5)
    // 0 2 4 6 8        0, 10, 2
    // 4 3 2 1 0        5-1, -1, -1

    // 퀴즈
    // 0, 1, 2, 3, 4를 한 줄에 하나씩 5번에 걸쳐 출력하세요 (2가지 코드)
    // printf("%d\n", 0);
    // printf("%d\n", 1);
    // printf("%d\n", 2);
    // printf("%d\n", 3);
    // printf("%d\n", 4);

    int a = 0;
    if (a < 5) {
        printf("%d\n", a);
        a += 1;
    }
    if (a < 5) {
        printf("%d\n", a);
        a += 1;
    }
    if (a < 5) {
        printf("%d\n", a);
        a += 1;
    }
    if (a < 5) {
        printf("%d\n", a);
        a += 1;
    }
    if (a < 5) {
        printf("%d\n", a);
        a += 1;
    }
    if (a < 5) {
        printf("%d\n", a);
        a += 1;
    }


    a = 0;                      // 시작
    while (a < 5) {             // 종료
        printf("%d ", a);
        a += 1;                 // 증감
    }
    printf("\n");

    // 퀴즈
    // 반복문을 사용해서 0 2 4 6 8을 출력하세요
    // 반복문을 사용해서 4 3 2 1 0을 출력하세요
    a = 0;
    while (a < 10) {
        printf("%d ", a);
        a += 2;
    }
    printf("\n");

    a = 4;
    while (a >= 0) {
        printf("%d ", a);
        a -= 1;
    }
    printf("\n");
}

void f_2() {
    char c = 'A';
    printf("%c %d\n", 'A', 'A');
    printf("%c %d\n", 65, 65);
    printf("%c %d\n", 'a', 'a');

    // 퀴즈
    // 대문자 전체를 출력하세요
    int i = 0;
    while (i < 26) {
        printf("%c", 'A'+i);
        i += 1;
    }
    printf("\n");

    i = 65;
    while (i < 65+26) {
        printf("%c", i);
        i += 1;
    }
    printf("\n");

    i = 'A';
    while (i <= 'Z') {
        printf("%c", i);
        i += 1;
    }
    printf("\n");

    // 퀴즈
    // 소문자 전체를 거꾸로 출력하세요
    i = 'z';
    while (i >= 'a') {
        printf("%c", i);
        i -= 1;
    }
    printf("\n");

    // 퀴즈
    // 소문자 전체를 거꾸로 출력하세요 (반복은 a부터 z까지로 합니다)
    i = 'a';
    while (i <= 'z') {
        printf("%c", 'z' - i + 'a');
        i += 1;
    }
    printf("\n");

    // 퀴즈
    // 소문자와 대문자 전체를 번갈아 출력하세요 (2가지 코드)
    i = 0;
    while (i < 26) {
        printf("%c %c ", 'a' + i, 'A' + i);
        i++;
    }
    printf("\n");

    c = 'a';
    while (c <= 'z') {
        printf("%c %c ", c, c - 32);
        c++;
    }
    printf("\n");
}


