#include <iostream>
#include <concepts>

// Шаблонная функция с использованием концепта integral
template <std::integral T>
T add(T a, T b) {
    return a + b;
}

int main() {
    int x, y;
    if (std::cin >> x >> y) {
        std::cout << add(x, y) << std::endl;
    }
    return 0;
}