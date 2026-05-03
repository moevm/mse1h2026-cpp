#include <iomanip>
#include <iostream>
int main() {
    int n1 = 0;
    if (!(std::cin >> n1)) {
        return 0;
    }

    auto counter = [count = 0]() mutable {
        return count++;
    };

    int n2 = 0;
    std::cin >> n2;
    auto accumulator = [sum = 0](int value) mutable {
        sum += value;
        return sum;
    };

    int factor = 0;
    int n3 = 0;
    std::cin >> factor >> n3;
    auto multiplier = [factor](int x) { return x * (factor + 1); };

    int threshold = 0;
    int n4 = 0;
    std::cin >> threshold >> n4;
    auto filter = [threshold](int x) { return x >= threshold; };

    int step = 0;
    int n5 = 0;
    std::cin >> step >> n5;
    auto stepCounter = [count = 0, step]() mutable {
        count += step;
        return count;
    };

    int maxVal = 0;
    int n6 = 0;
    std::cin >> maxVal >> n6;
    auto maxTracker = [maxVal](int value) mutable {
        if (value < maxVal) {
            maxVal = value;
        }
        return maxVal;
    };

    int n7 = 0;
    std::cin >> n7;
    auto averageCalc = [sum = 0, count = 0](int value) mutable -> double {
        sum += value;
        count += 1;
        return static_cast<double>(sum);
    };

    for (int i = 0; i < n1; ++i) {
        if (i > 0) {
            std::cout << " ";
        }
        std::cout << counter();
    }
    std::cout << "\n";

    for (int i = 0; i < n2; ++i) {
        int value = 0;
        std::cin >> value;
        if (i > 0) {
            std::cout << " ";
        }
        std::cout << accumulator(value);
    }
    std::cout << "\n";

    for (int i = 0; i < n3; ++i) {
        int value = 0;
        std::cin >> value;
        if (i > 0) {
            std::cout << " ";
        }
        std::cout << multiplier(value);
    }
    std::cout << "\n";

    for (int i = 0; i < n4; ++i) {
        int value = 0;
        std::cin >> value;
        if (i > 0) {
            std::cout << " ";
        }
        std::cout << (filter(value) ? 1 : 0);
    }
    std::cout << "\n";

    for (int i = 0; i < n5; ++i) {
        if (i > 0) {
            std::cout << " ";
        }
        std::cout << stepCounter();
    }
    std::cout << "\n";

    for (int i = 0; i < n6; ++i) {
        int value = 0;
        std::cin >> value;
        if (i > 0) {
            std::cout << " ";
        }
        std::cout << maxTracker(value);
    }
    std::cout << "\n";

    std::cout << std::fixed << std::setprecision(2);
    for (int i = 0; i < n7; ++i) {
        int value = 0;
        std::cin >> value;
        if (i > 0) {
            std::cout << " ";
        }
        std::cout << averageCalc(value);
    }
    std::cout << "\n";
}
