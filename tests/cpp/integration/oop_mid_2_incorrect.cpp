#include <iostream>
#include <numeric>
#include <stdexcept>

class Fraction {
private:
    int numerator;
    int denominator;
    
    void simplify() {
        int gcd = std::gcd(numerator, denominator);
        numerator /= gcd;
        denominator /= gcd;
        
        if (denominator < 0) {
            denominator = -denominator;
        }
    }

public:
    Fraction(int num, int den) : numerator(num), denominator(den) {
        if (denominator == 0) {
            throw std::invalid_argument("Denominator cannot be zero");
        }
        simplify();
    }
    
    Fraction operator*(const Fraction& other) const {
        return Fraction(numerator * other.numerator, denominator * other.denominator);
    }
    
    Fraction operator+(const Fraction& other) const {
        return Fraction(numerator * other.denominator + other.numerator * denominator,
                       denominator * other.denominator);
    }
    
    friend std::ostream& operator<<(std::ostream& os, const Fraction& f) {
        os << f.numerator << "/" << f.denominator;
        return os;
    }
};

int main() {
    Fraction f1(2, -4);
    std::cout << f1 << "\n";
    
    Fraction f2(1, -2);
    Fraction f3(1, 3);
    Fraction sum = f2 + f3;
    Fraction product = f2 * f3;
    std::cout << "Sum: " << sum << "\n";
    std::cout << "Product: " << product << "\n";
}