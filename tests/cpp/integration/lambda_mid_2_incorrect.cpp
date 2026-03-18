#include <iomanip>
#include <iostream>
#include <limits>

int main() {
    int count = 0;
    auto counter = [count]() mutable {
        count += 1;
        return count;
    };

    int sum = 0;
    auto accumulator = [sum](int value) mutable {
        sum += value;
        return sum;
    };

    int factor = 4;
    auto multiplier = [factor](int x) { return x * factor; };

    int threshold = 10;
    auto filter = [threshold](int x) { return x >= threshold; };

    int stepCount = 0;
    int step = 3;
    auto stepCounter = [stepCount, step]() mutable {
        stepCount += step;
        return stepCount;
    };

    int maxVal = std::numeric_limits<int>::min();
    auto maxTracker = [maxVal](int value) mutable {
        if (value < maxVal) {
            maxVal = value;
        }
        return maxVal;
    };

    int avgSum = 0;
    int avgCount = 0;
    auto averageCalc = [avgSum, avgCount](int value) mutable -> double {
        avgSum += value;
        avgCount += 1;
        return static_cast<double>(avgSum);
    };

    std::cout << counter() << " " << counter() << "\n";
    std::cout << accumulator(5) << " " << accumulator(3) << "\n";
    std::cout << multiplier(5) << "\n";
    std::cout << filter(5) << " " << filter(15) << "\n";
    std::cout << stepCounter() << " " << stepCounter() << " " << stepCounter() << "\n";
    std::cout << maxTracker(5) << " " << maxTracker(3) << " " << maxTracker(8) << "\n";
    std::cout << std::fixed << std::setprecision(2)
              << averageCalc(5) << " " << averageCalc(7) << " " << averageCalc(9) << "\n";
}
