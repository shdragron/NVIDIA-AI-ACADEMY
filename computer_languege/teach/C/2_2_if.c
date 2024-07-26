// 2_2_if.c
#include <stdio.h>

void f_1();
char score_to_grade(int score);

int main() {
    printf("80 : %c\n", score_to_grade(80));
    printf("65 : %c\n", score_to_grade(65));
    printf("99 : %c\n", score_to_grade(99));
    return 0;
}

void f_1() {
    int a = 72;

    if (a % 2 == 1) {
        printf("홀수\n");
    }
    else {
        printf("짝수\n");
    }

    if (a % 2)
        printf("홀수\n");
    else
        printf("짝수\n");

    a = 0;
    if (a)
        printf("홀수\n");
    else
        printf("짝수\n");

    if (a)
        printf("홀수\n");

    // 퀴즈
    // 어떤 정수가 양수인지 음수인지 0인지 알려주세요
    a = 0;
    if (a > 0) {
        printf("양수\n");
    }
    else {
        if (a < 0) {
            printf("음수\n");
        }
        else {
            printf("제로\n");
        }
    }

    printf("end of if\n");

    if (a > 0)
        printf("양수\n");
    else if (a < 0)
        printf("음수\n");
    else
        printf("제로\n");

    printf("end of if\n");

    if (a > 0)
        printf("양수\n");       
    if (a < 0)
        printf("음수\n");
    if (a == 0)
        printf("제로\n");
}

// 퀴즈
// 어제 만든 f_2 함수를 제대로 바꿔주세요
char score_to_grade(int score) {
    // 퀴즈
    // 점수를 학점으로 바꿔주세요
    // 90 ~ 100  A
    // 80 ~  89  B
    // 70 ~  79  C
    // 60 ~  69  D
    //  0 ~  59  F
    // char grade;

    // if (score >= 90 && score <= 100)
    //     grade = 'A';
    // else if (score >= 80 && score <= 89)
    //     grade = 'B';
    // else if (score >= 70 && score <= 79)
    //     grade = 'C';
    // else if (score >= 60 && score <= 69)
    //     grade = 'D';
    // else if (score >= 0 && score <= 59)
    //     grade = 'F';
    // else 
    //     grade = 'X';

    if (score < 0 || score > 100)
        return 'X';
    
    char grade = 'F';
    if (score >= 90)        grade = 'A';
    else if (score >= 80)   grade = 'B';
    else if (score >= 70)   grade = 'C';
    else if (score >= 60)   grade = 'D';

    return grade;
}


