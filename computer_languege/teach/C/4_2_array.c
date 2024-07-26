// 4_2_array.c
#include <stdio.h>
#include <stdlib.h>

// 퀴즈
// 배열을 출력하는 함수를 만드세요 (show_array)
void f_1();
void show_array(int a[], int size);
void make_randoms(int a[], int size);
int find_max(int a[], int size);
void copy_array(int src[], int dst[], int size);

// 퀴즈
// 100보다 작은 난수 10개가 들어있는 배열을 만드는 함수를 만드세요

// 퀴즈
// 배열에서 가장 큰 숫자를 찾는 함수를 만드세요

// 퀴즈
// 배열을 복사하는 함수를 만드세요 (copy_array)

int main() {
    // srand(23);                      // seed
    // for (int i = 0; i < 10; i++)
    //     printf("%d\n", rand());     // RAND_MAX

    int a[10] = {0,};
    printf("%d %d\n", sizeof(a), sizeof(a[0]));

    make_randoms(a, 10);
    show_array(a, sizeof(a) / sizeof(a[0]));

    printf("max : %d\n", find_max(a, 10));

    int b[10] = {0,};
    copy_array(a, b, 10);           // 깊은복사(deep copy)
    b[0] = 33;
    show_array(b, 10);

    int* c = a;                     // 얕은복사(shallow copy)
    c[0] = 99;
    show_array(c, 10);
    return 0;
}

void f_1() {
    int a[3] = {0, 2, 4};       // 같은 타입, 같은 공간
    a[0] = 99;
    printf("%d %d %d\n", a[0], a[1], a[2]);

    printf("크기 : %d\n", sizeof(a));
    printf("배열 : %p\n", a);           // p: pointer(address)
    printf("함수 : %p\n", printf);

    show_array(a, 3);

    int b[7] = {2, 3, 4, 5, 7, 8, 9};
    show_array(b, 7);
}

void show_array(int a[], int size) {       // int[] == int*
    // printf("크기 : %d\n", sizeof(a));
    // printf("배열 : %p\n", a);           // p: pointer(address)

    // int i = 0;
    // while (i < size) {
    //     printf("%d ", a[i]);
    //     i++;
    // }

    for (int i = 0; i < size; i++)
        printf("%d ", a[i]);
    printf("\n");
}

void make_randoms(int a[], int size) {
    for (int i = 0; i < size; i++) {
        a[i] = rand() % 100;
    }    
    // printf("%d %d\n", sizeof(a), sizeof(a[0]));
}

int find_max(int a[], int size) {
    int max = a[0];
    for (int i = 1; i < size; i++) {
        if (max < a[i])
            max = a[i];
    }

    return max;
}

void copy_array(int src[], int dst[], int size) {
    for (int i = 0; i < size; i++)
        dst[i] = src[i];
}

