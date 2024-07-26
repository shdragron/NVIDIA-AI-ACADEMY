// 9_1_recursion.c
#include <stdio.h>

int sum(int n);
void show_char(const char* s);

int main() {
    printf("합계 : %d\n", sum(100));
    show_char("hello");
    return 0;
}

int sum(int n) {
    if (n <= 1)
        return 1;

    return sum(n-1) + n;    
}

// 퀴즈
// 문자열을 출력하는 재귀 함수를 만드세요 (한번에 한 글자씩 출력)
void show_char(const char* s) {
    if (*s == '\0')
        return;

    show_char(s+1);     // ello llo lo o '\0'
    putchar(*s);        // h    e   l  l o

    // if (*s != '\0') {
    //     putchar(*s);
    //     show_char(s+1);
    // }
}

// 퀴즈
// 문자열을 거꾸로 출력하는 재귀 함수를 만드세요 (한번에 한 글자씩 출력)

// sum(10) : 1부터 10까지의 합계
// sum(10) : sum(9) + 10
// sum( 9) : sum(8) + 9
// sum( 8) : sum(7) + 8
// ...
// sum( 3) : sum(2) + 3
// sum( 2) : sum(1) + 2
// sum( 1) : 1

// show("hello") : 'h' + show("ello")
// show("ello")  : 'e' + show("llo")
// show("llo")   : 'l' + show("lo")
// show("lo")    : 'l' + show("o")
// show("o")     : 'o' + show("")
// show("")      : '\0'
