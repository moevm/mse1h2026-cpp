#include <iomanip>
#include <iostream>
#include <limits>

int main() {
    int acc1, acc2;
    int factor, multValue;
    int threshold, filter1, filter2;
    int step;
    int max1, max2, max3;
    int avg1, avg2, avg3;

    if (!(std::cin >> acc1 >> acc2)) {
        return 0;
    }
    if (!(std::cin >> factor >> multValue)) {
        return 0;
    }
    if (!(std::cin >> threshold >> filter1 >> filter2)) {
        return 0;
    }
    if (!(std::cin >> step)) {
        return 0;
    }
    if (!(std::cin >> max1 >> max2 >> max3)) {
        return 0;
    }
    if (!(std::cin >> avg1 >> avg2 >> avg3)) {
        return 0;
    }

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

    auto multiplier = [factor](int x) { return x * factor; };
    auto filter = [threshold](int x) { return x >= threshold; };

    int stepCount = 0;
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
    std::cout << accumulator(acc1) << " " << accumulator(acc2) << "\n";
    std::cout << multiplier(multValue) << "\n";
    std::cout << filter(filter1) << " " << filter(filter2) << "\n";
    std::cout << stepCounter() << " " << stepCounter() << " " << stepCounter() << "\n";
    std::cout << maxTracker(max1) << " " << maxTracker(max2) << " " << maxTracker(max3) << "\n";
    std::cout << std::fixed << std::setprecision(2)
              << averageCalc(avg1) << " " << averageCalc(avg2) << " " << averageCalc(avg3) << "\n";
}
