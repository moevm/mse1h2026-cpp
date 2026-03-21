#include <iostream>
#include <string>

int main() {
    // 1. Правильно
    []() {
        std::cout << "Hello, Lambda!" << std::endl;
    }();

    int a, b;
    if (!(std::cin >> a >> b)) return 0;

    // 2. ОШИБКА: Возвращаем разность вместо суммы
    auto sum = [](int x, int y) {
        return x - y;
    };
    std::cout << sum(a, b) << std::endl;

    // 3. Правильно
    int multiplier = 10;
    auto multiply = [multiplier](int x) {
        return x * multiplier;
    };
    std::cout << multiply(a) << std::endl;

    // 4. КРИТИЧЕСКАЯ ОШИБКА: Захват по значению [=] вместо [&]
    int counter = 0;
    // mutable нужен, чтобы разрешить менять копию внутри лямбды
    auto increment = [counter]() mutable {
        counter++;
    };

    increment();
    increment();
    // Выведет 0, так как внешняя переменная не изменилась
    std::cout << counter << std::endl;

    return 0;
}