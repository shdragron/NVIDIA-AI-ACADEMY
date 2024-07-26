// 7_3_1d_array.c
#include <stdio.h>

void show_array(int a[], int size);
void copy_array(int src[], int dst[], int size);
void copy_array_adv(int src[5][5], int dst[], int size);

int main() {
    int a[3] = {1, 3, 5};
    int b[5] = {2, 4, 6, 8, 0};

    // 퀴즈
    // 1차원 배열 a와 b를 출력할 수 있는 함수를 만드세요
    show_array(a, 3);
    show_array(b, 5);

    // 1 3 5 
    // 2 4 6 8 0
    // p size

    // char s[] = "hello";
    // show_array(s, 5);

    int grid[5][5] = {
        { 0,  1,  2,  3,  4},
        { 5,  6,  7,  8,  9},
        {10, 11, 12, 13, 14},
        {15, 16, 17, 18, 19},
        {20, 21, 22, 23, 24},
    };

    // 퀴즈
    // grid의 3번째 요소를 show_array 함수로 출력하세요
    show_array(grid[3], 5);
    show_array(grid[3], 10);
    show_array(grid[0], 25);

    int dst[25] = {0};
    show_array(dst, 25);

    // 퀴즈
    // 2차원 배열 grid를 1차원 배열 dst에 복사하는 함수를 만드세요

    // 퀴즈
    // copy_array 함수를 3가지 방법으로 호출하세요
    // copy_array(&grid[0][0], dst, 25);
    // copy_array(grid[0], dst, 25);
    // copy_array((int *) grid, dst, 25);
    // copy_array((int *) &grid, dst, 25);

    copy_array_adv(grid, dst, 25);
    show_array(dst, 25);

    return 0;
}

void show_array(int* a, int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", a[i]);
    printf("\n");
}

void copy_array(int src[], int dst[], int size) {
    for (int i = 0; i < size; i++)
        dst[i] = src[i];
}

void copy_array_adv(int src[][5], int dst[], int size) {
    // 1차원 -> 2차원
    // 7     -> (1, 2)
    // for (int i = 0; i < size; i++)
    //     dst[i] = src[i/5][i%5];

    //  2차원 -> 1차원
    // (1, 2) -> 7
    for (int i = 0; i < size/5; i++)
        for (int j = 0; j < 5; j++)
            dst[i*5+j] = src[i][j];
}
