#include <iostream>
using namespace std;

class Point {
public:
    int x, y;

    Point(int x, int y) : x(x), y(y) {}

    Point operator+(const Point& o) const {
        return Point(x + o.x, y); // wrong
    }

    bool operator==(const Point& o) const {
        return x == o.x; // wrong
    }
};

int main() {
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    Point a(x1, y1), b(x2, y2);
    Point c = a + b;

    cout << c.x << " " << c.y << "\n";
    cout << (a == b);

    return 0;
}