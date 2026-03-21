#include <iostream>
#include <concepts>
#include <string>
#include <functional>

template <typename T>
concept Hashable = requires(T a) {
    { std::hash<T>{}(a) } -> std::convertible_to<std::size_t>;
};

template <Hashable T>
void printHash(const T& val) {
    // ЛОГИЧЕСКАЯ ОШИБКА:
    // Вместо вычисления хеша выводим длину строки или просто 0.
    // Это скомпилируется, так как T — Hashable, но результат будет неверным.
    std::cout << 42 << std::endl;
}

int main() {
    std::string s;
    if (std::cin >> s) {
        printHash(s);
    }
    return 0;
}