#include <iostream>
#include <concepts>

// Шаблонная функция с использованием концепта std::totally_ordered
template <typename T>
requires std::totally_ordered<T>
T safe_clamp(T val, T min_val, T max_val) {
    if (val < min_val) return min_val;
    if (val > max_val) return max_val;
    return val;
}

int main() {
    // Важно: типы должны совпадать, чтобы сработал шаблон
    double v, lo, hi;
    if (std::cin >> v >> lo >> hi) {
        std::cout << safe_clamp(v, lo, hi) << std::endl;
    }
    return 0;
}