#include <stdio.h>
void f_2();

int main() {
    f_2();
}

void f_1() {
    // //관계 : > >= < <= == !=
    // printf("%d\n", 7>3); //1(TRUE)
    // printf("%d\n", 7<3); //0(FALSE)

    // //퀴즈
    // //나이를 입역 받아서 10대인지 알려주세요.(without 비트 연산)
    // int a;
    // scanf("%d",&a);
    // printf("%d\n", ((int)(10<= a) + (int)(a < 20))/2);
    // //printf("%d\n", ((10<= a) * (a < 20)));
}

#define TRUE 1
#define FALSE 0

// void f_3(){
//     printf("%d %d\n", TRUE, FALSE); // 1,0
//     printf("%d\n",TRUE && TRUE); // 1
//     printf("%d\n",TRUE && FALSE);//0
//     printf("%d\n",FALSE && TRUE);//0
//     printf("%d\n",FALSE && FALSE);//0
// }

void f_4(){
    int a = 7;
    if(a % 2){ // a % 2 == 1 과 동일.
        printf("odd\n");
    }
    else{
        printf("Even\n");
    }
}

//퀴즈
//어떤 정수가 양수인지 음수인지 0인지 알려주세요.

void f_2(){
    int a;
    scanf("%d", &a);
    if(a >= 0){
        if(a>0){
            printf("양수\n");
        }
        else{
            printf("0\n");
        }
    }
    else{
        printf("음수\n");
    }
}