// 11_5_enum.cpp

#include <iostream>
using namespace std;

// �߻� �Լ��� ��� �޴� Ŭ�������� �ݵ�� �����ؾ� �Ѵ�.
class Shape {
    virtual void draw() = 0;
};

class Rectangle : public Shape {
public:
    int width, height;
    void draw(){
        std::cout << "�簢��" << std::endl;
    };

};



class Circle : public Shape {
    public:
    int radius;
    void draw(){
        std::cout << "��" << std::endl;
    };
};



// enum�� ����� ������ ������ �� ����Ѵ�.
enum Color { RED, GREEN, BLUE};
        //    0     1     2


int main() {
    Rectangle r;
    r.draw();
    Color c = Color::GREEN;
    switch (c) {
        case RED:
            std::cout << "RED" << std::endl;
            break;
        case GREEN:
            std::cout << "GREEN" << std::endl;
            break;
        case BLUE:
            std::cout << "BLUE" << std::endl;
            break;
    }
    return 0;
}