// 5_1_switch.c
#include <stdio.h>

void f_1();
int* backup();
char score_to_grade(int score);

int main() {
    // int* t = backup();
    // printf("%d %d\n", t[0], t[4]);

    // int a[3] = {0, 2, 4};        // 주소, 값
    // int* p = a;
    // int* q = (int*) 0x000000000061FDFC;
    // printf("%p %p %p\n", a, p, q);

    // for (int i = 0; i < 3; i++)
    //     printf("%d %d %d\n", a[i], p[i], q[i]);

    // printf("%p\n", f_1);
    // typedef void (* f_t)();
    // f_t f = (f_t) 0x000000000040162B;
    // f();

    printf("%c\n", score_to_grade(95));
    printf("%c\n", score_to_grade(80));
    printf("%c\n", score_to_grade(60));
    printf("%c\n", score_to_grade(15));
    return 0;
}

int* backup() {
    int a[5] = {3, 5, 7, 9, 1};
    return a;
}

void f_1() {
    int n = 0;
    int* p = &n;
    printf("양수 입력 : ");
    scanf("%d", p);

    // 입력한 양수를 3으로 나눈 나머지를 알려주세요
    printf("%d\n", n % 3);

    if (n % 3 == 0) {
    }
    else if (n % 3 == 1) {
    }
    else {
    }

    switch (n % 3) {
    case 0:
        printf("나머지가 0\n");
        break;
    case 1:
        printf("나머지가 1\n");
        break;
    default:
        printf("나머지가 2\n");
    }
}

// *  *=  /* */  int*

// 퀴즈
// 점수를 학점으로 바꿔주는 함수를 만드세요 (switch 사용)
// 90 ~ 100  A
// 80 ~  89  B
// 70 ~  79  C
// 60 ~  69  D
//  0 ~  59  F
char score_to_grade(int score) {
    if (score < 0 || score > 100)
        return 'X';

    char grade = 'F';
    switch (score / 10)
    {
    case 10:
    case 9:  grade = 'A';  break;
    case 8:  grade = 'B';  break;
    case 7:  grade = 'C';  break;
    case 6:  grade = 'D';  break;
    }

    return grade;
}
