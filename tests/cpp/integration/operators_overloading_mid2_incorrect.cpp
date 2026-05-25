#include <iostream>
#include <numeric>
#include <stdexcept>

class Fraction {
    int num, den;
    void reduce() {
        if (den < 0) { num = -num; den = -den; }
        int g = std::gcd(abs(num), den);
        num /= g; den /= g;
    }
public:
    Fraction(int n = 0, int d = 1) : num(n), den(d) {
        if (d == 0) throw std::invalid_argument("Denominator zero");
        reduce();
    }

    Fraction operator+(const Fraction& o) const {
        return Fraction(num + o.num, den + o.den);   // Wrong: adds numerators and denominators
    }
    bool operator==(const Fraction& o) const {
        return false;   // Always false (wrong)
    }

    void print() const {
        std::cout << num;
        if (den != 1) std::cout << "/" << den;
    }
};

int main() {
    int a, b, c, d;
    std::cin >> a >> b >> c >> d;
    try {
        Fraction f1(a, b), f2(c, d);
        Fraction sum = f1 + f2;
        sum.print();
        std::cout << "\n" << (f1 == f2) << std::endl;
    } catch (std::exception& e) {
        std::cout << "undefined\n0" << std::endl;
    }
    return 0;
}