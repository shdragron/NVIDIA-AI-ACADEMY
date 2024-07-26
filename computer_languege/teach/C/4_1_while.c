// 4_1_while.c
#include <stdio.h>

void f_1();
void f_2();

int main() {
    // printf("%d\n", 0x7fffffff);     // 15 * 16 + 15 = 255
    // printf("%d\n", 0x7fffffff + 1);
    return 0;
}

void f_1() {
    // 퀴즈
    // -1을 입력할 때까지 정수를 입력 받아보세요 (scanf 사용)
    // -1을 입력할 때까지 입력한 정수 합계를 구하세요
    // int n = 0, s = 0;
    // while (n != -1) {
    //     scanf("%d", &n);
    //     s += n;
    // }
    // s += 1;

    int n, s = 0;
    while (1) {                     // 처음/마지막 탈출
        scanf("%d", &n);
        if (n == -1)
            break;                  // 중간 탈출

        s += n;
        printf("합계 : %d\n", s);
    }
}

// 퀴즈
// 0을 입력할 때까지의 정수 중에서 가장 큰 값을 알려주세요
void f_2() {
    // 가짜 코드
    // 반복
    //    1. 정수를 입력 받는다
    //    2. 0인지 확인한다
    //    3. 0이라면 종료한다
    //    4. 0이 아니면 가장 큰 값인지 확인한다

    // int n = 0, max = 0;
    // while (1) {
    //     scanf("%d", &n);
    //     if (n == 0)
    //         break;

    //     if (max < n)            
    //         max = n;

    //     printf("%d %d\n", n, max);
    // }

    // int n, max = 0;
    // do {
    //     scanf("%d", &n);
    //     if (n == 0)
    //         break;

    //     if (max < n)            
    //         max = n;
    // } while (n != 0);

    int n = 0, max = -2147483648;
    do {
        scanf("%d", &n);
        if (n == 0)
            break;

        if (max < n)            
            max = n;
    } while (n != 0);

    printf("최대값 : %d\n", max);
}

