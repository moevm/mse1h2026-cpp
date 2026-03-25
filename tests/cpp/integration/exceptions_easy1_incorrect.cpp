#include <iostream>
#include <string>
#include <stdexcept>

class Calculator {
public:
    Calculator() = default;

    double divide(double a, double b) const {
        if (b == 0.0) {
            // ОШИБКА: вместо throw просто возвращаем 0
            return 0.0;
        }
        return a / b;
    }

    double calculate(const std::string& operation, double a, double b) const {
        if (operation == "+") return a + b;
        if (operation == "-") return a - b;
        if (operation == "*") return a * b;
        if (operation == "/") return divide(a, b);

        // ОШИБКА: вместо исключения возвращаем 0 при неизвестной операции
        return 0.0;
    }
};

int main() {
    Calculator calc;
    std::string op;
    double a, b;

    while (std::cin >> op >> a >> b) {
        // Программа всегда будет выводить число, даже если операция неверна
        std::cout << calc.calculate(op, a, b) << std::endl;
    }
    return 0;
}