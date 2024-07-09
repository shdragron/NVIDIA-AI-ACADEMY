#include <stdio.h>

// 배열을 채우는 함수
void fillArray(int arr[], int size) {
    for(int i = 0; i < size; i++) {
        arr[i] = i * i;
    }
}

int main() {
    int arr[5];
    fillArray(arr, 5);
    for(int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}
