// 11_5_single_list.cpp

#include <iostream>
using namespace std;

struct NODE {
    int data;
    NODE* next;

    NODE(int n) : data(n) { 
        next = NULL;
    }
};

class SingleList {
private:
    NODE* head;

public:
    SingleList() : head(NULL) {}

    bool is_empty() { return head == NULL; }

    void show_all() {
        NODE* cur = head;
        while (cur != NULL) {
            std::cout << cur->data << ", ";
            cur = cur->next;
        }
        std::cout << endl;
    }

    void add_head(int value) {
        NODE* node = new NODE(value);
        node->next = head;
        head = node;
    }

    void add_tail(int value) {

        // NODE* node = new NODE(value);
        // if (head == NULL) {
        //     head = node;
        // } else {

        //     NODE* cur = head;
        //     while (cur->next != NULL) {
        //         cur = cur->next;
        //     }
        //     cur->next = node;
        // }

        NODE** cur = &head;
        while (*cur)
            cur = &(*cur)->next;
        *cur = new NODE(value);
    }
};

int main() {
    SingleList list;

    // list.add_head(11);
    // list.add_head(22);
    // list.add_head(33);
    // list.add_tail(44);
    list.add_tail(55);
    list.add_tail(66);

    list.show_all();

    return 0;
}


