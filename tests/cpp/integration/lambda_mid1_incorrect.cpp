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
    std::vector<Person> people = {
        {"Ivan", 35, 100.0},
        {"Anna", 28, 200.0},
        {"Boris", 28, 150.0},
    };

    auto isOlderThan30 = [](const Person& p) { return p.age >= 30; };
    auto increaseSalary = [](Person& p) { p.salary += 10; };
    auto compare = [](const Person& a, const Person& b) { return a.name < b.name; };
    auto calculateAverageAge = [&people]() -> double {
        double sum = 0.0;
        for (const auto& p : people) {
            sum += p.age;
        }
        return sum;
    };

    int olderCount = 0;
    for (const auto& p : people) {
        if (isOlderThan30(p)) {
            ++olderCount;
        }
    }

    increaseSalary(people[1]);
    std::sort(people.begin(), people.end(), compare);

    std::cout << olderCount << "\n";
    std::cout << static_cast<int>(people[0].salary) << "\n";
    std::cout << people[0].name << " " << people[1].name << " " << people[2].name << "\n";
    std::cout << std::fixed << std::setprecision(2) << calculateAverageAge() << "\n";
}
