#include <iostream>

class Point {
private:
    double x, y;

public:
    Point(double x = 0, double y = 0) : x(x), y(y) {}

    Point operator+(const Point& other) const {
        return Point(x + other.x, y + other.y);
    }

    bool operator==(const Point& other) const {
        return x == other.x && y == other.y;
    }
};

int main() {
    Point a(1, 2), b(3, 4);
    Point c = a + b;

    if (!(c == Point(4, 6))) return 1;

    return 0;
}