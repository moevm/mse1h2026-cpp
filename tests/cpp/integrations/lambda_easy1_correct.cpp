#include <iostream>
#include <vector>
#include <functional>

int main() {
    // 1. Лямбда без параметров, вызываемая сразу
    []() {
        std::cout << "Hello, Lambda!" << std::endl;
    }();

    int a, b;
    if (!(std::cin >> a >> b)) return 0;

    // 2. Лямбда с параметрами (сумма)
    auto sum = [](int x, int y) {
        return x + y;
    };
    std::cout << sum(a, b) << std::endl;

    // 3. Захват по значению (multiplier)
    int multiplier = 10;
    auto multiply = [multiplier](int x) {
        return x * multiplier;
    };
    std::cout << multiply(a) << std::endl;

    // 4. Захват по ссылке (counter)
    int counter = 0;
    auto increment = [&counter]() {
        counter++;
    };

    increment();
    increment();
    std::cout << counter << std::endl; // Ожидаем 2

    return 0;
}