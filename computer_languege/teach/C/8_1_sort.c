// 8_1_sort.c
#include <stdio.h>
#include <string.h>

void swap(int* p1, int* p2);
void show_array(int* a, int size);
void bubble_up(int *p, int size);
void bubble_sort(int* p, int size);
int max_pos(int *p, int size);
void insertion_sort(int* p, int size);
void show_names(const char* names[], int size);

void insertion_sort_names(const char* names[], int size);
int max_pos_names(const char* names[], int size);
void swap_names(const char** p1, const char** p2);

int main() {
    int ages[10] = {15, 90, 83, 34, 72, 51, 10, 22, 66, 45};

    // swap(&ages[0], &ages[1]);
    // swap(&*(ages+0), &*(ages+1));
    // swap(ages, ages+1);
    show_array(ages, 10);

    // bubble_sort(ages, 10);
    insertion_sort(ages, 10);
    show_array(ages, 10);

    // 퀴즈
    // 문자열 배열을 삽입 정렬로 정렬하는 함수를 만드세요
    // 문자열 교환 함수는 꼭 만들어 주세요
    // const char* names[] = {"kim", "lee", "han", "nam", "koo"};
    // show_names(names, 5);

    // insertion_sort_names(names, 5);
    // show_names(names, 5);
    return 0;
}

// 퀴즈
// 정수 2개를 교환하는 함수를 만드세요
void swap(int* p1, int* p2) {
    // int tmp = p1[0];
    int tmp = *p1;
    *p1 = *p2;
    *p2 = tmp;
}

void show_array(int* a, int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", a[i]);
    printf("\n");
}

void bubble_up(int *p, int size) {
    for (int i = 0; i < size-1; i++) {
        if (p[i] > p[i+1]) 
            swap(p+i, p+i+1);
    }
}

// 퀴즈
// bubble_up 함수를 사용해서 배열을 정렬하는 함수를 만드세요
void bubble_sort(int* p, int size) {
    // for (int i = 0; i < size; i++)
    //     bubble_up(p, size - i);

    for (int i = size; i > 1; i--)
        bubble_up(p, i);
}

// 퀴즈
// 배열에서 가장 큰 값의 인덱스를 알려주는 함수를 만드세요
int max_pos(int* p, int size) {
    int pos = 0;
    for (int i = 1; i < size; i++) {
        if (p[pos] < p[i])
            pos = i;
    }
    return pos;
}

// 퀴즈
// max_pos 함수를 사용해서 삽입 정렬 함수를 만드세요
void insertion_sort(int* p, int size) {
    int pos;
    for (int i = size; i > 1; i--) {
        pos = max_pos(p, i);
        swap(p+pos, p+i-1);
        show_array(p, size);
    }
}

void show_names(const char* names[], int size) {
    for (int i = 0; i < size; i++)
        printf("%s ", names[i]);
    printf("\n");
}

void insertion_sort_names(const char* names[], int size) {
    int pos;
    for (int i = size; i > 1; i--) {
        pos = max_pos_names(names, i);
        swap_names(names+pos, names+i-1);
    }
}

int max_pos_names(const char* names[], int size) {
    int pos = 0;
    for (int i = 1; i < size; i++) {
        if (strcmp(names[pos], names[i]) < 0)   // if (names[pos] < names[i])
            pos = i;
    }
    return pos;
}

void swap_names(const char** p1, const char** p2) {
    const char* tmp = *p1;
    *p1 = *p2;
    *p2 = tmp;
}
