// 5_3_string.c
#include <stdio.h>
#include <string.h>

// 퀴즈
// 정수 배열의 앞쪽 절반만 출력하는 함수를 만드세요
// 정수 배열의 뒤쪽 절반만 출력하는 함수를 만드세요
void show_array(int a[], int size);

int main() {
    // int p[10] = {1, 3, 5, 7, 9, 2, 4, 6, 8, 0};
    // printf("%p\n", &p[5]);

    // show_array(p, 5);
    // show_array(&p[5], 5);
    // show_array(p+5, 5);

    // 문자열 : 커피 무지개 파인애플
    char s1[256] = "abc";
    char s2[256] = {'d', 'e', 'f'};
    char *s3 = "ghi";

    printf("%p %s\n", s1, s1);
    printf("%p %s\n", s3, s3);

    // s1 = s2;     // 주소가 상수(에러)
    // s3 = s2;     // 주소가 변수

    // s1[0] = 'A'; // 값은 변수
    // s3[0] = 'G'; // 값은 상수(에러)

    printf("%s %s %s\n", s1, s2, s3);
    return 0;

    // 퀴즈
    // 문자열을 반복문을 사용해서 한 문자씩 출력하세요
    for (int i = 0; i < strlen(s1); i++)
        printf("%c %c %c\n", s1[i], s2[i], s3[i]);
    putchar('\n');

    int j = 0;
    while (s1[j] != '\0') {
        printf("%c %c %c\n", s1[j], s2[j], s3[j]);
        j++;
    }
    putchar('\n');

    j = 0;
    while (s1[j] != '\0') {
        putchar(s1[j]);
        j++;
    }
    putchar('\n');

    j = 0;
    while (s1[j])          // a b c \0
        putchar(s1[j++]);
    putchar('\n');

    char *p = s1;
    while (*p)
        putchar(*p++);
    
    return 0;

    // 정답: 잘 모른다
    // j = 0;
    // printf("%d\n", j++ + ++j + j++ + ++j);
}

void show_array(int a[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", a[i]);
    printf("\n");
}



