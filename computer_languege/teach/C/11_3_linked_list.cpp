// 11_3_linked_list.cpp
#include <iostream>
using namespace std;

struct NODE {
    int data;
    NODE* next;

    NODE(int n) : data(n) { 
        next = NULL;
    }
};

void show_all(NODE* head);

int main() {
    NODE n0(0);
    NODE n1(1);
    NODE n2(2);

    NODE* head = NULL;
    head = &n0;
    n0.next = &n1;
    n1.next = &n2;

    std::cout << n0.data << endl;
    std::cout << n0.next->data << endl;
    std::cout << n0.next->next->data << endl;

    std::cout << head->data << endl;
    std::cout << head->next->data << endl;
    std::cout << head->next->next->data << endl;
    std::cout << "------------------" << endl;

    // std::cout << head->data << endl;
    // head = head->next;
    // std::cout << head->data << endl;
    // head = head->next;
    // std::cout << head->data << endl;
    // head = head->next;
    // std::cout << "------------------" << endl;

    show_all(head);
    return 0;
}

// 퀴즈
// NODE 전체를 출력하는 함수를 만드세요 (반복문 사용)
void show_all(NODE* head) {
    while (head != NULL) {
        std::cout << head->data << ", ";
        head = head->next;
    }
    std::cout << endl;
}

