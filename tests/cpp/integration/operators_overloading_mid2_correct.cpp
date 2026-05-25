#include <iostream>
#include <numeric>      
#include <stdexcept>

class Fraction {
private:
    int num, den;
    void reduce() {
        if (den < 0) { num = -num; den = -den; }
        int g = std::gcd(abs(num), den);
        num /= g; den /= g;
    }
public:
    Fraction(int n = 0, int d = 1) : num(n), den(d) {
        if (d == 0) throw std::invalid_argument("Denominator cannot be zero");
        reduce();
    }

    Fraction operator+(const Fraction& o) const {
        return Fraction(num * o.den + o.num * den, den * o.den);
    }
    Fraction operator-(const Fraction& o) const {
        return Fraction(num * o.den - o.num * den, den * o.den);
    }
    Fraction operator*(const Fraction& o) const {
        return Fraction(num * o.num, den * o.den);
    }
    Fraction operator/(const Fraction& o) const {
        if (o.num == 0) throw std::invalid_argument("Division by zero");
        return Fraction(num * o.den, den * o.num);
    }

    bool operator==(const Fraction& o) const { return num == o.num && den == o.den; }
    bool operator!=(const Fraction& o) const { return !(*this == o); }
    bool operator<(const Fraction& o) const { return num * o.den < o.num * den; }
    bool operator>(const Fraction& o) const { return o < *this; }
    bool operator<=(const Fraction& o) const { return !(o < *this); }
    bool operator>=(const Fraction& o) const { return !(*this < o); }

    explicit operator double() const { return static_cast<double>(num) / den; }

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