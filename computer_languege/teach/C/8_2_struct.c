// 8_2_struct.c
#include <stdio.h>

struct INFO {
    int age;
    double weight;
    char gender;
};

void show_info(struct INFO me);
void show_info_adv(struct INFO* p);
void show_info_array(struct INFO us[], int size);

int main() {
    struct INFO me = {21, 75.0, 'M'};

    printf("크기 : %d\n", sizeof(me));

    // printf("나이 : %d\n", me.age);
    // printf("체중 : %.1f\n", me.weight);

    show_info(me);
    show_info_adv(&me);

    struct INFO us[] = {
        {20, 50.0, 'F'},
        {50, 60.0, 'M'},
        {30, 80.0, 'M'},
    };

    show_info_array(us, 3);
    return 0;
}

// int, char*, double, boolean ==> collection, struct(object)

// 퀴즈
// INFO 구조체를 출력하는 함수를 만드세요
void show_info(struct INFO me) {
    printf("나이 : %d\n", me.age);
    printf("체중 : %.1f\n", me.weight);
    printf("성별 : %s\n", me.gender == 'M' ? "남자" : "여자");
}

// 퀴즈
// INFO 구조체를 출력하는 함수를 만드세요 (포인터 버전)
void show_info_adv(struct INFO* p) {
    printf("나이 : %d\n", (*p).age);
    printf("체중 : %.1f\n", p->weight);
    printf("성별 : %s\n", (*p).gender == 'M' ? "남자" : "여자");
}

// 퀴즈
// 구조체 배열을 출력하는 함수를 만드세요
void show_info_array(struct INFO us[], int size) {
    for (int i = 0; i < size; i++) {
        // show_info_adv(&us[i]);
        // show_info_adv(&*(us+i));
        show_info_adv(us+i);
    }
}
