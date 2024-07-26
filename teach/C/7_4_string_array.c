// 7_4_string_array.c
#include <stdio.h>
#include <string.h>

void show_words(char words[3][256]);
void show_colors(const char* colors[3], int size);

int main() {
    char words[3][256] = {"red", "green", "blue"};
    show_words(words);

    // 퀴즈
    // 문자열 배열에서 가장 큰 문자열은 누구인지 알려주세요 (strcmp)
    if (strcmp(words[0], words[1])) {
        printf("%s가 %s보다 크다\n", words[0], words[1]);
        if (strcmp(words[0], words[2])) {
            printf("%s가 %s보다 크다\n", words[0], words[2]);
        }
        else {
            printf("%s가 %s보다 작다\n", words[0], words[2]);
        }
    }
    else {
        printf("%s가 %s보다 작다\n", words[0], words[1]);
        if (strcmp(words[1], words[2])) {
            printf("%s가 %s보다 크다\n", words[1], words[2]);
        }
        else {
            printf("%s가 %s보다 작다\n", words[1], words[2]);
        }
    }

    int idx = -1;
    idx = strcmp(words[0], words[1]) > 0 ? 0 : 1;
    idx = strcmp(words[idx], words[2]) > 0 ? idx : 2;
    puts(words[idx]);

    // char s1[256] = "hello";
    // strcpy(s1, "hi");
    // char* s2 = "world";

    // 퀴즈
    // 아래와 같은 형태의 문자열 배열을 출력하는 함수를 만드세요
    const char* colors[3] = {"red", "green", "blue"};
    show_colors(colors, 3);
    // colors[0] = "purple";
    return 0;
}

// 퀴즈
// 문자열 배열을 출력하는 함수를 만드세요
// void show_words(char words[][256]) {
void show_words(char(* words)[256]) {
    for (int i = 0; i < 3; i++)
        puts(words[i]);
}

// 가지고 있다(요소가 뭐냐?)
// 가리킨다

// void show_colors(const char* colors[], int size) {
void show_colors(const char** colors, int size) {
    for (int i = 0; i < size; i++)
        puts(colors[i]);
}
