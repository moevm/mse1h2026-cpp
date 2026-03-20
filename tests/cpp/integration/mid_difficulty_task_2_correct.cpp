#include <iostream>
#include <numeric>
#include <stdexcept>

class Fraction {
private:
    int n, d;

    void reduce() {
        int g = std::gcd(abs(n), d);
        n /= g;
        d /= g;
        if (d < 0) {
            n = -n;
            d = -d;
        }
    }

public:
    Fraction(int num = 0, int den = 1) : n(num), d(den) {
        if (den == 0) throw std::invalid_argument("0");
        reduce();
    }

    Fraction operator+(const Fraction& o) const {
        return Fraction(n * o.d + o.n * d, d * o.d);
    }

    Fraction operator-(const Fraction& o) const {
        return Fraction(n * o.d - o.n * d, d * o.d);
    }

    Fraction operator*(const Fraction& o) const {
        return Fraction(n * o.n, d * o.d);
    }

    Fraction operator/(const Fraction& o) const {
        return Fraction(n * o.d, d * o.n);
    }

    bool operator==(const Fraction& o) const {
        return n == o.n && d == o.d;
    }

    bool operator!=(const Fraction& o) const { return !(*this == o); }
    bool operator<(const Fraction& o) const { return n * o.d < o.n * d; }
    bool operator>(const Fraction& o) const { return o < *this; }
    bool operator<=(const Fraction& o) const { return !(*this > o); }
    bool operator>=(const Fraction& o) const { return !(*this < o); }

    operator double() const {
        return (double)n / d;
    }
};

int main() {
    Fraction a(1,2), b(1,3);
    Fraction c = a + b;

    if (!(c == Fraction(5,6))) return 1;

    double x = (double)a;
    if (x < 0.49 || x > 0.51) return 1;

    return 0;
}