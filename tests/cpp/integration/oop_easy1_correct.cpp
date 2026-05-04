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
    double w1 = 0.0;
    double h1 = 0.0;
    if (!(std::cin >> w1 >> h1)) {
        return 0;
    }

    Rectangle r(w1, h1);
    std::cout << r.getArea() << "\n";
    std::cout << r.getPerimeter() << "\n";
    std::cout << r.isSquare() << "\n";

    double w2 = 0.0;
    double h2 = 0.0;
    std::cin >> w2 >> h2;
    r.setWidth(w2);
    r.setHeight(h2);
    std::cout << r.getWidth() << " " << r.getHeight() << "\n";
    std::cout << r.getArea() << "\n";

    double w3 = 0.0;
    double h3 = 0.0;
    std::cin >> w3 >> h3;
    Rectangle sq(w3, h3);
    std::cout << sq.isSquare() << "\n";
}
