#include <iostream>
#include <string>

int main() {
    // 1. Лямбда без параметров, вызываемая сразу
    []() {
        std::cout << "Hello, Lambda!" << std::endl;
    }();

    int a, b, multiplier, val;
    // Считываем ВСЕ параметры, которые подает тест
    if (!(std::cin >> a >> b >> multiplier >> val)) return 0;

    // 2. Лямбда с параметрами (сумма)
    auto sum = [](int x, int y) {
        return x + y;
    };
    std::cout << sum(a, b) << std::endl;

    // 3. Захват по значению (multiplier)
    // multiplier теперь берется из ввода, а не из константы
    auto multiply = [multiplier](int x) {
        return x * multiplier;
    };
    // Используем val для умножения, как того требует логика теста
    std::cout << multiply(val) << std::endl;

    // 4. Захват по ссылке (counter)
    int counter = 0;
    auto increment = [&counter]() {
        counter++;
    };

    increment();
    increment();
    std::cout << counter << std::endl;

    return 0;
}
