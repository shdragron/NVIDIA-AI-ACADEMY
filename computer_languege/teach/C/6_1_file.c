// 6_1_file.c
#include <stdio.h>
#include <string.h>

void read_file_1();
void read_file_2();
void write_file();

int main() {
    write_file();
    return 0;
}

void read_file_1() {
    // char file_path[] = ".\\data\\poem.txt";
    char file_path[] = "C:\\Users\\Harmony00\\Desktop\\C\\data\\poem.txt";
    char buffer[256];

    FILE* fp = fopen(file_path, "r");

    // 퀴즈
    // 개행문자를 1번만 출력하세요 (2가지 코드)
    // EOF: End Of File 
    // NULL 포인터: 주소가 0인 포인터
    // char *p = 0;
    while (fgets(buffer, sizeof(buffer), fp)) {
        if (buffer[strlen(buffer)-1] == '\n') 
            buffer[strlen(buffer)-1] = '\0';
        // buffer[0] = '\0';                // 버퍼 클리어
        puts(buffer);

        // 1번
        // printf("%s", buffer);
        // printf(buffer);
    }

    fclose(fp);
}

void read_file_2() {
    char file_path[] = "C:\\Users\\Harmony00\\Desktop\\C\\data\\poem.txt";
    int ch;

    FILE* fp = fopen(file_path, "r");

    while (1) {
        ch = fgetc(fp);

        if (ch == EOF)      // -1
            break;

        putchar(ch);
        // printf("%d\n", ch);
    }

    fclose(fp);
}

void write_file() {
    FILE* fp = fopen("C:\\Users\\Harmony00\\Desktop\\C\\data\\sample.txt", "w");

    if (fp == NULL)
        return;

    fputs("배드민턴은 재밌는 운동입니다", fp);

    // 퀴즈
    // fprintf 함수를 사용해서 새로운 문장을 추가하세요
    fprintf(fp, "나이 %d\n사는곳 %s\n취미 %s", 21, "성남", "독서");

    fclose(fp);
}
