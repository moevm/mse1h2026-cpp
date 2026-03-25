#include <iostream>

class Fraction {
private:
    int n, d;

public:
    Fraction(int num = 0, int den = 1) : n(num), d(den) {}

    Fraction operator+(const Fraction& o) const {
        return Fraction(n + o.n, d);
    }

    bool operator==(const Fraction& o) const {
        return n == o.n;
    }

    operator double() const {
        return n / d;
    }
};

int main() {
    Fraction a(1,2), b(1,3);
    Fraction c = a + b;

    if (!(c == Fraction(5,6))) return 1; 

    return 0;
}