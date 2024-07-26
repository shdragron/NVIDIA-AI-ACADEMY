// 7_1_for_for.c
#include <stdio.h>

int main() {
    // 퀴즈
    // 아래처럼 출력하세요
    //   01234
    // 0 *   *
    // 1  * *
    // 2   *
    // 3  * *
    // 4 *   *
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (i == j || i + j == 5-1)
                printf("*");
            else
                printf("-");
        }
        printf("\n");
    }
    printf("\n");

    // 퀴즈
    // 아래처럼 출력하세요
    //   01234
    // 0 *****
    // 1 *   *
    // 2 *   *
    // 3 *   *
    // 4 *****
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            // if (i == 0 || i == 4 || j == 0 || j == 4)
            if (i % 4 == 0 || j % 4 == 0)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }

    return 0;
}



