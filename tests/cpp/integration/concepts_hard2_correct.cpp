#include <iostream>
#include <concepts>
#include <string>
#include <functional>

// Определение собственного концепта Hashable
template <typename T>
concept Hashable = requires(T a) {
    { std::hash<T>{}(a) } -> std::convertible_to<std::size_t>;
};

// Функция, использующая наш концепт
template <Hashable T>
void printHash(const T& val) {
    std::cout << std::hash<T>{}(val) << std::endl;
}

int main() {
    std::string s;
    if (std::cin >> s) {
        printHash(s);
    }
    return 0;
}