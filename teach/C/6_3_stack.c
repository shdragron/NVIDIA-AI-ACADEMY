// 6_3_stack.c
#include <stdio.h>
#include <string.h>

// 자료구조(Data Structure)
// 스택(stack)
// 큐(queue)
// 연결리스트(linked list)

void push(int value);
int pop(); 
int is_empty();
void show_stack();

int g_buffer[256];
int g_top = 0;

int main() {
    // for (int i = 1; i < 10; i += 2) {
    //     push(i);
    // }

    // 퀴즈
    // 앞에서 넣은 데이터를 모두 출력해 주세요 (is_empty 사용)
    // while (!is_empty())
    //     printf("%d ", pop());

    // show_stack();

    // 퀴즈
    // 스택을 사용해서 ages 배열을 거꾸로 뒤집어 주세요
    int ages[5] = {12, 78, 45, 90, 34};
    for (int i = 0; i < 5; i++)
        push(ages[i]);

    for (int i = 0; i < 5; i++)
        ages[i] = pop();

    for (int i = 0; i < 5; i++)
        printf("%d ", ages[i]);

    const char* s1 = "hello";
    const char* s2 = "hi";

    printf("%d\n", strcmp(s1, s2));

    // 퀴즈
    // strchr 함수를 사용해서 특정 문자가 몇 개인지 알려주세요  
    const char* p = "strawberry is very sweet";

    printf("%s\n", strchr(p, 'r'));
    printf("%d\n", strchr(p, 'x'));

    const char* p1 = strchr(p, 'r');
    const char* p2 = strchr(&p1[1], 'r');
    const char* p3 = strchr(&p2[1], 'r');

    printf("%s\n", p1);
    printf("%s\n", p2);
    printf("%s\n", p3);

    // p = strchr(p, 'r');
    // printf("%s\n", p);

    // p = strchr(&p[1], 'r');
    // printf("%s\n", p);

    // p = strchr(&p[1], 'r');
    // printf("%s\n", p);

    printf("\n");
    // while (p != NULL) {
    //     p = strchr(p, 'r');

    //     if (p != NULL) {
    //         printf("%s\n", p);
    //         p = &p[1];
    //     }
    // }

    printf("\n");
    // while (1) {
    //     p = strchr(p, 'r');

    //     if (p == NULL) 
    //         break;

    //     printf("%s\n", p++);

    //     // printf("%s\n", p);
    //     // p = &*(p+1);    // &p[1];
    //     // p = p+1;    // &p[1];
    // }

    while (p = strchr(p, 'r'))
        printf("%s\n", p++);

    return 0;
}

void push(int value) {
    g_buffer[g_top++] = value;
}

int pop() {
    return g_buffer[--g_top];
}

int is_empty() {
    return g_top == 0;
}

void show_stack() {
    for (int i = g_top-1; i >= 0; i--)
        printf("%d ", g_buffer[i]);
    printf("\n");
}

