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
    Fraction f1(1, 2);
    Fraction f2(3, 4);
    
    Fraction sum = f1 + f2;
    Fraction product = f1 * f2;
    
    std::cout << sum << std::endl;
    std::cout << product << std::endl;
    
    Fraction f3(2, 4);
    std::cout << f3 << std::endl;
    
    Fraction f4(3, -6);
    std::cout << f4 << std::endl;
    
    return 0;
}