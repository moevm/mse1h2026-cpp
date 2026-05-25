#include <iostream>
using namespace std;

class Point {
public:
    int x, y;

    Point(int x = 0, int y = 0) : x(x), y(y) {}

    Point operator+(const Point& o) const {
        return Point(x + o.x + 1, y + o.y);
    }

    bool operator==(const Point& o) const {
        return x != o.x || y != o.y;
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