#include <stdio.h>

void f_1();
void f_2();
void f_3();

int main() {
    f_3();
    return 0;
}

// 퀴즈
// "rainy day"를 3번 출력하세요 (3가지 코드)
void f_1() {
    printf("rainy day\n");
    printf("rainy day\n");
    printf("rainy day\n");

    printf("rainy day rainy day rainy day\n");

    printf("rainy day" "rainy day" "rainy day\n");

    printf("r");
    printf("a");
    printf("i");
    printf("n");
    printf("y");
}

void f_2() {
    // printf("%c %d %f %s\n", 'a', 12, 3.14);
    // printf("%c %d %f\n", 'a', 12, 3.14, "ace");

    // character, integer, floating point, string
    printf("%c %d %lf %s\n", 'a', 12, 3.14, "ace");

    // 퀴즈
    // 123을 출력할 수 있는 코드를 만드세요 (4가지)
    int a = 123;
    printf("123 %d %d %s %.0f\n", a, 123, "123", 123.0);

    // printf("printf : %p\n", printf);

    printf("43\n");
    printf("%d\n", printf("43"));
    // 1             2            3
    printf("%d\n", printf("%d", printf("43")));

    // 123 = 456;       // lvalue error
}

// 1: 0 1
// 2: 00 01 10 11
// 3: 000 001 010 011 100 101 110 111

void f_3() {
    int a = 3, b = 7;
    printf("%d %d\n", a, b);

    // 퀴즈
    // a와 b의 값을 바꾸세요
    int t = a;
    a = b;
    b = t;

    printf("%d %d\n", a, b);
}













