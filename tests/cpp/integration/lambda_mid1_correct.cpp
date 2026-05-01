#include <algorithm>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

struct Person {
    std::string name;
    int age;
    double salary;
};

int main() {
    int n = 0;
    if (!(std::cin >> n)) {
        return 0;
    }
    std::vector<Person> people;
    people.reserve(n);
    for (int i = 0; i < n; ++i) {
        Person p;
        std::cin >> p.name >> p.age >> p.salary;
        people.push_back(p);
    }

    auto isOlderThan30 = [](const Person& p) { return p.age > 30; };
    auto increaseSalary = [](Person& p) { p.salary *= 1.1; };
    auto compare = [](const Person& a, const Person& b) {
        if (a.age != b.age) {
            return a.age < b.age;
        }
        return a.name < b.name;
    };
    auto calculateAverageAge = [&people]() -> double {
        double sum = 0.0;
        for (const auto& p : people) {
            sum += p.age;
        }
        return sum / people.size();
    };

    int olderCount = 0;
    for (const auto& p : people) {
        if (isOlderThan30(p)) {
            ++olderCount;
        }
    }

    for (auto& p : people) {
        increaseSalary(p);
    }
    std::sort(people.begin(), people.end(), compare);

    std::cout << olderCount << "\n";
    std::cout << std::fixed << std::setprecision(2) << people.front().salary << "\n";
    for (size_t i = 0; i < people.size(); ++i) {
        if (i > 0) {
            std::cout << " ";
        }
        std::cout << people[i].name;
    }
    std::cout << "\n";
    std::cout << std::fixed << std::setprecision(2) << calculateAverageAge() << "\n";
}
