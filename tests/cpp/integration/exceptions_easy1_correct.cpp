#include <iostream>
#include <string>
#include <stdexcept>

class Calculator {
public:
    Calculator() = default;

    double divide(double a, double b) const {
        if (b == 0.0) {
            throw std::runtime_error("Деление на ноль невозможно");
        }
        return a / b;
    }

    double calculate(const std::string& operation, double a, double b) const {
        if (operation == "+") return a + b;
        if (operation == "-") return a - b;
        if (operation == "*") return a * b;
        if (operation == "/") return divide(a, b);
        throw std::invalid_argument("Неизвестная операция");
    }
};

int main() {
    Calculator calc;
    std::string op;
    double a, b;

    while (std::cin >> op >> a >> b) {
        try {
            std::cout << calc.calculate(op, a, b) << std::endl;
        } catch (const std::runtime_error& e) {
            std::cout << "Runtime Error: " << e.what() << std::endl;
        } catch (const std::invalid_argument& e) {
            std::cout << "Invalid Argument: " << e.what() << std::endl;
        }
    }
    return 0;
}