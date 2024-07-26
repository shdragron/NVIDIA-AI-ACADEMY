// 10_4_static.cpp
#include <iostream>
#include <cstring>
using namespace std;

// int g_productCount = 0;

// 퀴즈
// Product 생성자와 데이터를 출력하는 show 함수를 만드세요
class Product {
private:
    static int count;           // 정적 멤버변수

public:
    char name[256];
    int price;

    Product(const char name[256], int price) {
        strcpy(this->name, name);
        this->price = price;

        // g_productCount++;
        count++;
    }

    void show() {
        std::cout << name << ", " << price << endl;
    }

    static void show_count() {
        // price = 200;                         // 에러
        std::cout << "갯수 : " << count << endl;
    }
};

int Product::count = 0;

// 퀴즈
// 프로그램 끝날 때까지 만든 Product 객체는 몇 개인지 알려주세요

int main() {
    Product p1("cup", 100);
    Product p2("mike", 200);
    Product p3("bottle", 300);

    p3.show();
    // std::cout << "갯수 : " << g_productCount << endl;

    // p1.show_count();
    // p2.show_count();
    // p3.show_count();
    
    Product::show_count();
    return 0;
}



