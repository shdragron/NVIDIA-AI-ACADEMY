// 7_2_2d_array.c
#include <stdio.h>

void show_grid(int grid[4][5]);
void show_triangle(int grid[5][5]);
void show_column(int grid[5][5], int col);

int main() {
    int grid[5][5] = {
        { 0,  1,  2,  3,  4},
        { 5,  6,  7,  8,  9},
        {10, 11, 12, 13, 14},
        {15, 16, 17, 18, 19},
        {20, 21, 22, 23, 24},
    };

    printf("%d, %d\n", grid[0][0], grid[3][4]);

    // 퀴즈
    // 2차원 배열 전체를 출력하세요
    //      0   1   2   3   4
    // 0    0   1   2   3   4 
    // 1    5   6   7
    // 2
    // 3

    show_grid(grid);

    // 퀴즈
    // 아래처럼 배열 요소를 출력하세요 (별이 있는 위치의 값만 출력합니다. 함수로 만드세요)
    // 1번
    // *---
    // **--
    // ***-
    // ****

    // # 2번
    // ****
    // ***
    // **
    // *

    // # 3번
    //    *
    //   **
    //  ***
    // ****

    // 4번
    // ****
    //  ***
    //   **
    //    *
    show_triangle(grid);

    // 퀴즈
    // 2차원 배열로부터 특정한 열을 출력하는 함수를 만드세요
    show_column(grid, 1);

    return 0;
}

void show_grid(int grid[][5]) {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 5; j++) {
            printf("%d ", grid[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

void show_triangle(int grid[5][5]) {
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (i >= j)
                printf("%2d ", grid[i][j]);
        }
        printf("\n");
    }
    printf("\n");

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (i + j < 5)
                printf("%2d ", grid[i][j]);
        }
        printf("\n");
    }
    printf("\n");

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (i + j >= 5-1)
                printf("%2d ", grid[i][j]);
            else
                printf("   ");
        }
        printf("\n");
    }
    printf("\n");

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (i <= j)
                printf("%2d ", grid[i][j]);
            else
                printf("   ");
        }
        printf("\n");
    }
    printf("\n");
}

void show_column(int grid[5][5], int col) {
    // for (int i = 0; i < 5; i++) {
    //     for (int j = 0; j < 5; j++) {
    //         if (j == col)
    //             printf("%d ", grid[i][j]);
    //     }
    // }

    for (int i = 0; i < 5; i++) {
        printf("%d ", grid[i][col]);    // (0, 1) (1, 1) (2, 1) (3, 1) (4, 1)
    }
    printf("\n");
}
