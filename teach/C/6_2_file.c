// 6_2_file.c
#include <stdio.h>

#define TRUE 1
#define FALSE 0

int main() {
    FILE* fp = fopen("C:/Users/Harmony00/Desktop/C/data/numbers.csv", "r");
    char buffer[256];
    int a;
    float b;
    int c;

    // while (fgets(buffer, sizeof(buffer), fp)) {
    //     printf("%s\n", buffer);
    // }

    while (fscanf(fp, "%d,%f,%d", &a, &b, &c) != EOF) {
        printf("%d, %f, %d\n", a, b, c);
    }

    fclose(fp);
    return 0;
}
