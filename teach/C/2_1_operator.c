// 2_1_operator.c
#include <stdio.h>

void f_1();
void f_2();

int main() {
    f_2();
    return 0;
}

void f_1() {
    // 관계 : >  >=  <  <=  ==  !=
    printf("%d\n", 7 > 3);      // 1(TRUE)
    printf("%d\n", 7 < 3);      // 0(FALSE)
    printf("%d\n", 7 >= 3);
    printf("%d\n", 7 <= 3);
    printf("%d\n", 7 == 3);
    printf("%d\n", 7 != 3);

    // 퀴즈
    // 나이를 입력 받아서 10대인지 알려주세요(논리 연산자 사용 금지)
    int a = 15;
    printf("%d\n", 10 <= a <= 19);
    printf("%d\n", 10 <= a && a <= 19);
    printf("%d\n", (10 <= a) * (a <= 19));
    printf("%d\n", ((10 <= a) + (a <= 19)) / 2);
    printf("%d\n", (10 <= a) == (a <= 19));

    // a >= 10  a <= 19
    // 0   +     0 = 0 / 2 = 0
    // 0   +     1 = 1 / 2 = 0
    // 1   +     0 = 1 / 2 = 0
    // 1   +     1 = 2 / 2 = 1
}

// 연산 : 산술  관계  논리  비트
// 논리 : &&  ||  !
#define TRUE 1
#define FALSE 0

void f_2() {
    printf("%d %d\n", TRUE, FALSE);

    printf("%d\n", TRUE && TRUE);
    printf("%d\n", TRUE && FALSE);
    printf("%d\n", FALSE && TRUE);
    printf("%d\n", FALSE && FALSE);
}

