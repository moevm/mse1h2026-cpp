#include <iostream>

class Rectangle {
private:
    double width;
    double height;

public:
    Rectangle(double w, double h) : width(w), height(h) {}

    double getWidth() const { return width; }
    double getHeight() const { return height; }

    void setWidth(double w) { width = w; }
    void setHeight(double h) { height = h; }

    double getArea() const { return width * height; }
    double getPerimeter() const { return 2 * (width + height); }
    bool isSquare() const { return width == height; }
};

int main() {
    double w, h, newW, newH, sqW, sqH;
    if (!(std::cin >> w >> h >> newW >> newH >> sqW >> sqH)) {
        return 0;
    }

    Rectangle r(w, h);
    std::cout << r.getArea() << "\n";
    std::cout << r.getPerimeter() << "\n";
    std::cout << r.isSquare() << "\n";

    r.setWidth(newW);
    r.setHeight(newH);
    std::cout << r.getWidth() << " " << r.getHeight() << "\n";
    std::cout << r.getArea() << "\n";

    Rectangle sq(sqW, sqH);
    std::cout << sq.isSquare() << "\n";
}
