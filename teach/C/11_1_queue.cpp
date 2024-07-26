// 11_1_queue.cpp
#include <iostream>
using namespace std;

// 큐 : 선입선출(FIFO, First-In First-Out)
// 줄서기

// 6 - 1 3 5
//     F
//   R

class Queue {
public:
    static const int size = 128;

private:
    int buf[size] = {1, 3, 5, 7, 9};
    int front, rear;

public:
    Queue() : front(0), rear(0) {
        // this->front = this->rear = 0;
    }

    // 퀴즈
    // 데이터를 추가하는 함수를 만드세요 (enqueue)
    void enqueue(int n) {
        this->buf[this->rear] = n;
        this->rear = (this->rear + 1) % Queue::size;
    }

    // 퀴즈
    // 데이터를 꺼내는 함수를 만드세요 (dequeue)
    int dequeue() {
        int n = this->buf[this->front];
        this->front = (this->front+1) % Queue::size;
        return n;
    }

    // 비어있는지 알려주는 함수를 만드세요 (is_empty)
    bool is_empty() {
        return this->front == this->rear;
    }

    // 퀴즈
    // 큐를 출력하는 함수를 만드세요
    void show() {
        for (int i = this->front; i != this->rear; i = (i+1) % Queue::size)
            std::cout << this->buf[i] << ' ';
        std::cout << endl;

        // if (this->front <= this->rear) {
        //     for (int i = front; i < rear; i++)
        //         std::cout << this->buf[i] << ' ';
        //     std::cout << endl;
        // }
        // else {
        //     for (int i = front; i < Queue::size; i++)
        //         std::cout << this->buf[i] << ' ';

        //     for (int i = 0; i < rear; i++)
        //         std::cout << this->buf[i] << ' ';
        //     std::cout << endl;
        // }
    }
};

int main() {
    Queue q;

    q.enqueue(11);
    q.enqueue(22);
    q.enqueue(33);
    q.show();
    printf("%d\n", q.dequeue());
    printf("%d\n", q.dequeue());

    q.enqueue(44);
    q.enqueue(55);
    q.enqueue(66);
    q.show();
    printf("%d\n", q.dequeue());
    printf("%d\n", q.dequeue());

    q.enqueue(77);
    q.enqueue(88);
    q.show();

    while (q.is_empty() == false)
        printf("%d\n", q.dequeue());
    std::cout << "---------------------" << endl;

    // 퀴즈
    // 43명이 둥글게 앉아있을 때,
    // 2명이 남을 때까지 3번째 사람을 제거한다면
    // 마지막에 남는 두 사람은 몇 번째 사람일까요?
    for (int i = 1; i <= 43; i++)
        q.enqueue(i);

    // 5 ... 43 1 2 4 
    for (int i = 0; i < 41; i++) {
        q.enqueue(q.dequeue());
        q.enqueue(q.dequeue());
        q.dequeue();
    }

    std::cout << q.dequeue() << ", " << q.dequeue() << endl;

    return 0;
}



