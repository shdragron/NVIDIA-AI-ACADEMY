#include <stdio.h>

// 배열을 채우는 함수
void fillArray(int arr[], int size) {
    // 배열의 각 요소를 인덱스의 제곱값으로 설정
    for(int i = 0; i < size; i++) {
        arr[i] = i * i;
    }
}

int main() {
    int arr[5];  // 크기 5의 배열 선언
    fillArray(arr, 5);  // 배열을 함수에 전달하여 채움
    // 배열의 내용을 출력
    for(int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}
