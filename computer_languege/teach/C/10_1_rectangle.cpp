// 10_1_rectangle.cpp
#include <iostream>
using namespace std;

// 좌표
class Point {
public:
    int x, y;

    // 기본 생성자
    Point() {
        x = y = 0;
    }

    // constructor(c'tor)
    Point(int x, int y) {
        this->x = x;
        this->y = y;
        // (*this).x = x;
    }

    // destructor(d'tor)
    ~Point() {
    }

    void show() {
        std::cout << x << ", " << y << endl;
    }
};

// 퀴즈
// Point 클래스를 사용해서 Rectangle 클래스를 만드세요
// 변수: 좌표 2개
// 함수: 면적, 길이, 높이, 출력 
class Rectangle {
    Point pt1, pt2;             // 좌상단, 우하단

public:
    // Rectangle() {
    //     pt1.x = pt1.y = pt2.x = pt2.y = 0;
    // }

    Rectangle(int x1=0, int y1=0, int x2=0, int y2=0)
        : pt1(x1, y1), pt2(x2, y2) {     // default parameter
        // (&pt1)->x = x1;
        // pt1.x = x1;
        // pt1.y = y1;
        // pt2.x = x2;
        // pt2.y = y2;
    }

    inline int width() {
        return pt2.x - pt1.x;
    }

    inline int height() {
        return pt2.y - pt1.y;
    }

    inline int area() {
        return width() * height();
    }

    void show() {
        // std::cout << pt1.x << ", " << pt1.y << endl;        
        // std::cout << pt2.x << ", " << pt2.y << endl;        

        pt1.show();
        pt2.show();
    }
};

int main() {
    Rectangle rect(3, 5, 9, 7);
    // Rectangle rect(9, 7, 3, 5);          // 생성자 내부에서 좌표 교환 필요
    rect.show();

    std::cout << "너비 : " << rect.width() << endl; 
    std::cout << "높이 : " << rect.height() << endl; 
    std::cout << "면적 : " << rect.area() << endl; 

    Rectangle basic;
    basic.show();

    return 0;
}
