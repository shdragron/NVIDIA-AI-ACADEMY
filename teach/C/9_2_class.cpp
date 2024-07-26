// 9_2_class.cpp
#include <iostream>
// #include <cstdio>
using namespace std;

class Point {
public:
    int x, y;

    // 기본 생성자
    Point() {
        std::cout << "기본 생성자 호출" << endl;
        x = y = 0;
    }

    // constructor(c'tor)
    Point(int x, int y) {
        std::cout << "생성자 호출" << endl;
        this->x = x;
        this->y = y;
        // (*this).x = x;
    }

    // destructor(d'tor)
    ~Point() {
        std::cout << "소멸자 호출" << endl;
    }

    void show() {
        std::cout << x << ", " << y << endl;
    }
};

int main() {
    std::cout << "hello, c++!!" << ' ' << 1234 << endl; 
    std::cout << true << false << endl;                         // Boolean

    Point pt2;
    Point pt(3, 7);
    Point *p = new Point(5, 9);         // 동적 할당(malloc, free)

    // pt.x = 10;
    // pt.y = 20;

    pt2.show();
    pt.show();
    (*p).show();
    // 퀴즈
    // 포인터 변수 p에 값을 넣고 show 함수를 호출하세요
    p->x = 11;
    p->y = 22;
    p->show();

    delete p;
    p = NULL;

    return 0;
}
