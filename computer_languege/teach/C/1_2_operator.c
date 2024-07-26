// 1_2_operator.c
#include <stdio.h>

void f_1();
void f_2();
void f_3();
void f_4();
void f_5();

int main() {
    f_5();
    return 0;
}

// 연산 : 산술, 관계, 논리, 비트
// 산술 : +  -  *  /  %

void f_1() {
    int a = 7, b = 3;
    printf("%d\n", a + b);
    printf("%d\n", a - b);
    printf("%d\n", a * b);
    // printf("%d\n", a / b);
    // printf("%d\n", a % b);

    // 퀴즈
    // 추가 변수를 사용하지 말고 a와 b의 값을 바꾸세요
    a = a + b;      // a = 10, b = 3
    b = a - b;      // a = 10, b = 7
    a = a - b;      // a = 3, b = 7

    printf("%d %d\n", a, b);

    a += b;
    b = a - b;
    a -= b;

    printf("%d %d\n", a, b);
}

void f_2() {
    printf("%d\n", 7 / 3);          // 정수 나눗셈(몫)
    printf("%f\n", 7.0 / 3.0);      // 실수 나눗셈
    printf("%f\n", 7 / 3.0);

    int a = 7, b = 3;
    printf("%d\n", a / b);
    printf("%f\n", a / (float) b);
    printf("%lf\n", a / (double) b);

    printf("%d\n", 7 % 3);          // 1

    //     2        // 몫
    //   +---
    // 3 | 7
    //     6
    //    ---
    //     1        // 나머지
}

void f_3() {
    double f = 0.5;
    // scanf("%lf", &f);
    // printf("%lf\n", f);

    // 퀴즈
    // 정수와 실수 변수를 각각 만들어서 scanf 한번만 써서 값을 입력 받으세요
    int a = 12;
    scanf("%d %lf", &a, &f);
    printf("%d %lf\n", a, f);
}

void f_4() {
    // 퀴즈
    // 실수를 입력 받아서 소숫점 이하만 남기는 코드를 만드세요
    double f = 3.5; // 0.5
    // printf("실수를 입력하세요 : ");
    // scanf("%lf", &f);
    printf("%lf %d %lf\n", f, (int) f, f - (int) f);

    // 퀴즈
    // 2자리 양수를 거꾸로 뒤집어 주세요
    int a = 37;     // 37 = 3 * 10 + 7
    int b = a / 10 + a % 10 * 10;
    printf("%d\n", b);

    // 퀴즈
    // 3자리 양수를 거꾸로 뒤집어 주세요 (2가지 코드)
    int c = 369;    // 963

    int d0 = 0, d1 = 0, d2 = 0;
    d0 = c / 100;
    // d1 = c / 10 % 10;
    d1 = c % 100 / 10;
    d2 = c % 10;

    printf("%d %d %d\n", d0, d1, d2);
    printf("%d\n", d0 + d1 * 10 + d2 * 100);
}

void f_5() {
    // 퀴즈
    // a를 b로 나눈 나머지를 % 연산자 없이 구하세요
    int a = 7, b = 3;

    int d0 = a / b;     // 2
    int d1 = d0 * b;    // 6
    int d2 = a - d1;    // 1
    printf("%d\n", d2);
    printf("%d\n", a - a / b * b);
}
