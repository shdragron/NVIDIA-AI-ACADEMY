// 5_4_string.c
#include <stdio.h>
#include <string.h>

// 퀴즈
// 문자열의 길이를 계산하는 함수를 만드세요 (string_length)
int string_length(const char* s);

// 퀴즈
// 문자열을 복사하는 함수를 만드세요 (string_copy)
void string_copy(char* dst, const char* src);

// 퀴즈
// 문자열에 포함된 문자를 찾는 함수를 만드세요 (string_char)
int string_char(const char* s, char ch);

int main() {
    char s[256] = "hello";
    printf("길이 : %d\n", string_length(s));
    printf("길이 : %d\n", strlen(s));           // C언어 제공

    char buffer[256] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    // string_copy(buffer, s);
    strcpy(buffer, s);
    printf("복사 : %s\n", buffer);

    char t[256] = "abcdabcdabcd";
    int pos = string_char(t, 'b');
    char* p = strchr(t, 'b');
    printf("%d %c\n", pos, t[pos]);
    printf("%p %c %c\n", p, p[0], *p);
    return 0;
}

int string_length(const char* s) {
    int i;
    for (i = 0; s[i]; i++)
        ;

    return i;
}

void string_copy(char* dst, const char* src) {
    // int i;
    // for (i = 0; src[i]; i++)
    //     dst[i] = src[i];
    // dst[i] = '\0';

    for (int i = 0; dst[i] = src[i]; i++)
        ;

    // while (*dst++ = *src++)
    //     ;
}

int string_char(const char* s, char ch) {
    for (int i = 0; s[i]; i++) {
        if (s[i] == ch)
            return i;
    }
    return -1;

    // int pos = -1;
    // for (int i = 0; s[i]; i++) {
    //     if (s[i] == ch) {
    //         pos = i;
    //         break;
    //     }
    // }
    // return pos;
}

