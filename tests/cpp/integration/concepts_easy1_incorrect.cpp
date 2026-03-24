#include <iostream>
#include <concepts>

template <std::integral T>
T add(T a, T b) {
    return a - b; // ОШИБКА: Вместо сложения делаем вычитание
}

int main() {
    long a, b;
    if (std::cin >> a >> b) {
        std::cout << add(a, b) << std::endl;
    }
    return 0;
}