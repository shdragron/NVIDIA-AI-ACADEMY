// 9_3_stack.cpp
#include <iostream>
using namespace std;

class Stack {
private:    
    int buffer[256];
    int top;

public:
    Stack() {
        top = 0;
    }

    void push(int value) {
        buffer[top++] = value;
    }

    int pop() {
        return buffer[--top];
    }

    int is_empty() {
        return top == 0;
    }

    void show_stack() {
        for (int i = top-1; i >= 0; i--)
            std::cout << buffer[i] << ' ';
        std::cout << endl;
    }

    // 퀴즈
    // 스택을 초기화하는 clear 함수를 만드세요
    void clear() {
        top = 0;
    }
};

int main() {
    // 퀴즈
    // 앞에서 만든 스택을 클래스 버전으로 업그레이드 하세요 
    Stack s;

    s.push(3);
    s.push(7);
    s.show_stack();
    s.clear();

    // 퀴즈
    // 스택을 사용해서 ages 배열을 거꾸로 뒤집어 주세요
    int ages[5] = {12, 78, 45, 90, 34};

    for (int i = 0; i < 5; i++)
        s.push(ages[i]);

    for (int i = 0; s.is_empty() == false; i++)
        ages[i] = s.pop();

    for (int i = 0; i < 5; i++)
        std::cout << ages[i] << ' ';
    std::cout << endl;

    return 0;
}

