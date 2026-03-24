#include <iostream>

class Rectangle {
private:
    double width;
    double height;

public:
    Rectangle(double w, double h) : width(w < 0 ? 0.0 : w), height(h < 0 ? 0.0 : h) {}

    double getWidth() const { return width; }
    double getHeight() const { return height; }

    void setWidth(double w) { width = w < 0 ? 0.0 : w; }
    void setHeight(double h) { height = h < 0 ? 0.0 : h; }

    double getArea() const { return width * height; }
    double getPerimeter() const { return 2 * (width + height); }
    bool isSquare() const { return width == height; }
};

int main() {
    Rectangle r(3, 4);
    std::cout << static_cast<int>(r.getArea()) << "\n";
    std::cout << static_cast<int>(r.getPerimeter()) << "\n";
    std::cout << r.isSquare() << "\n";

    r.setWidth(-2);
    r.setHeight(5);
    std::cout << static_cast<int>(r.getWidth()) << " " << static_cast<int>(r.getHeight()) << "\n";
    std::cout << static_cast<int>(r.getArea()) << "\n";

    Rectangle sq(7, 7);
    std::cout << sq.isSquare() << "\n";
}
