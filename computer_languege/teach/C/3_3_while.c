// 3_3_while.c
#include <stdio.h>

void f_1();
int sumation(int start, int end);

int main() {
    printf("%d\n", sumation(3, 7));
    printf("%d\n", sumation(7, 3));
    return 0;
}

void f_1() {
    // 퀴즈
    // 1부터 10까지의 합계를 구하세요
    int s = 0;
    int i = 1;
    while (i <= 10) {
        s += i;
        printf("합계 : %d\n", s);
        i++;
    }    
}

// 퀴즈
// 정수 범위에 대해 합계를 구하는 함수를 만드세요 (3 ~ 8)
// 1. 함수를 만든다
// 2. 정상 범위의 합계를 구한다(0 ~ 10)
// 3. 거꾸로 범위의 합계도 구한다
int sumation(int start, int end) {
    int s = 0;
    // 그냥
    // if (start <= end) {
    //     int i = start;
    //     while (i <= end) {
    //         s += i;
    //         i++;
    //     }    
    // }
    // else {
    //     int i = end;
    //     while (i <= start) {
    //         s += i;
    //         i++;
    //     }    
    // }

    if (start > end) {
        int t = start;
        start = end;
        end = t;
    }

    int i = start;
    while (i <= end) {
        s += i;
        i++;
    }    

    return s;
}

