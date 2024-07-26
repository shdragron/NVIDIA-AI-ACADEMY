// 11_5_enum.cpp
#include <iostream>
using namespace std;

class Shape {
    virtual void draw() = 0;
};

class Rectangle : public Shape {
public:    
    void draw() {
        std::cout << "사각형" << endl;
    }
};

class Circle : public Shape {
public:    
    void draw() {
        std::cout << "원" << endl;
    }
};

#define WHITE 9

//           0    5        6
enum Color { RED, GREEN=5, BLUE };

int main() {
    Rectangle r;
    r.draw();

    std::cout << RED << endl;

    Color c = GREEN;

    switch (c)
    {
    case RED:
        break;
    case GREEN:
        break;
    case BLUE:
        break;
    }

    return 0;
}

