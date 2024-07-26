// 10_3_overloading.cpp
#include <iostream>
using namespace std;

class Point {
public:
    int x, y;

    Point() {
        x = y = 0;
        std::cout << "기본 생성자" << endl;
    }

    Point(int x, int y) {
        this->x = x;
        this->y = y;
        std::cout << "xy 생성자" << endl;
    }

    Point(const Point& other) {           // copy constructor
        this->x = other.x;
        this->y = other.y;
        std::cout << "복사 생성자" << endl;
    }

    ~Point() {
    }

    Point& operator =(const Point& other) {           // 얕은 복사
        this->x = other.x;
        this->y = other.y;
        std::cout << "대입 연산자" << endl;
        return *this;
    }

    Point add(const Point& rhs) {      // right hand side
        int x = this->x + rhs.x;
        int y = this->y + rhs.y;

        return Point(x, y);
    }

    // Point operator+(const Point& rhs) {      // right hand side
    //     int x = this->x + rhs.x;
    //     int y = this->y + rhs.y;

    //     return Point(x, y);
    // }

    friend Point operator+(const Point& lhs, const Point& rhs) {
        return Point(lhs.x+rhs.x, lhs.y+rhs.y);
    }

    void show() {
        std::cout << x << ", " << y << endl;
    }
};

Point add(const Point& lhs, const Point& rhs) {
    return Point(lhs.x+rhs.x, lhs.y+rhs.y);
}

int main() {
    Point pt1;
    Point pt2(3, 7);
    Point pt3 = pt2;
    Point pt4(pt2);

    pt3.show();
    pt4.show();

    pt1 = pt2 = pt3;
    pt1.show();

    // Point pt5 = pt1.add(pt2);
    // Point pt5 = pt1.operator+(pt2);      // 클래스 멤버 함수 호출 
    Point pt5 = pt1 + pt2;
    pt5.show();

    pt3 = add(pt1, pt2);
    Point pt6 = add(pt1, pt2);
    pt6.show();
    
    return 0;
}
