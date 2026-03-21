#include <iostream>
#include <concepts>

template <typename T>
requires std::totally_ordered<T>
T safe_clamp(T val, T min_val, T max_val) {
    // ЛОГИЧЕСКАЯ ОШИБКА:
    // Если значение меньше минимума, мы ошибочно возвращаем максимум.
    // Если значение больше максимума, мы ошибочно возвращаем минимум.
    if (val < min_val) return max_val;
    if (val > max_val) return min_val;
    return val;
}

int main() {
    double v, lo, hi;
    if (std::cin >> v >> lo >> hi) {
        std::cout << safe_clamp(v, lo, hi) << std::endl;
    }
    return 0;
}