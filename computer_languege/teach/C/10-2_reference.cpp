// 10-2_reference.cpp
#include <iostream>
using namespace std;

void swap(int& a, int& b);

int main() {
    int value = 13;
    int& ref = value;

    ref = 99;
    std::cout << ref << endl;
    std::cout << value << endl;

    int a = 3, b = 7;
    std::cout << a << ", " << b << endl;

    swap(a, b);
    std::cout << a << ", " << b << endl;

    return 0;
}

// 퀴즈
// 레퍼런스를 이용해서 a와 b를 교환하는 함수를 만드세요
void swap(int& a, int& b) {
    int t = a;
    a = b;
    b = t;
}



