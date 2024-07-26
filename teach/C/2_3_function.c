// 2_3_function.c
#include <stdio.h>

void f_1();
void f_2(int a);
int f_3();
int twice(int a);

// 교수 학생
// 교수 -> 데이터 -> 학생 : 매개변수
// 교수 <- 데이터 <- 학생 : 반환값

int main() {
    printf("before\n");
    f_1();
    printf("after\n");

    f_2(7);

    f_3();
    int c = f_3();
    printf("반환 : %d\n", c);
    printf("반환 : %d\n", f_3());

    printf("%d\n", twice(3));
    printf("%d\n", 3 * 2);      // 값을 2배로 증폭

    int a = twice(7);
    printf("%d\n", a);
    return 0;
}

// 매개변수 없고, 반환값 없고.
void f_1() {
    printf("f_1\n");
}

// 매개변수 있고, 반환값 없고.
void f_2(int a) {
    printf("f_2 : %d\n", a);
}

// 매개변수 없고, 반환값 있고.
int f_3() {
    printf("f_3\n");
    return 3;
}

// 매개변수 있고, 반환값 있고.
// 퀴즈
// 정수의 값을 2배로 만들어주는 함수를 만드세요
int twice(int a) {
    return a * 2;
}







