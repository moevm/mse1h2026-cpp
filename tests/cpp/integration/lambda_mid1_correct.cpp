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

    std::vector<Person> people(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> people[i].name >> people[i].age >> people[i].salary;
    }
    int k = 0;
    std::cin >> k;

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

    increaseSalary(people[k - 1]);
    double updatedSalary = people[k - 1].salary;
    std::sort(people.begin(), people.end(), compare);

    std::cout << olderCount << "\n";
    std::cout << std::fixed << std::setprecision(2) << updatedSalary << "\n";
    for (int i = 0; i < n; ++i) {
        if (i > 0) {
            std::cout << " ";
        }
        std::cout << people[i].name;
    }
    std::cout << "\n";
    std::cout << std::fixed << std::setprecision(2) << calculateAverageAge() << "\n";
}
