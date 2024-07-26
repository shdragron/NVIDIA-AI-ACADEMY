// 11_5_linked_list.cpp

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
};

int main() {
    SingleList list;

    list.add_head(11);
    list.add_head(22);
    list.add_head(33);

    list.show_all();

    return 0;
}


