import random
from ...base_module import BaseTaskClass, TestItem


class LambdaMid1Test(BaseTaskClass):
    """Lambda functions -- Mid_difficulty_task_1"""

    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(
            compile_name="program",
            seed=seed,
            **kwargs
        )

    def generate_task(self) -> str:
        return """# Задание

Вам дана структура `Person`, описывающая человека с именем, возрастом и зарплатой. Люди хранятся в векторе `std::vector<Person>`.
```cpp
struct Person
{
    std::string name;
    int age;
    double salary;

    Person(std::string n, int a, double s) : name(n), age(a), salary(s) {}
};
```

Вам необходимо реализовать следующие лямбда выражения:

**1) Фильтрация по возрасту**
**Требования к лямбде:**
- Сохранить лямбду в переменную `isOlderThan30`
- Принимать `const Person&`
- Возвращать `true`, если возраст человека больше 30
- Захват: пустой

**2) Увеличение зарплаты**
**Требования к лямбде:**
- Сохранить лямбду в переменную `increaseSalary`
- Принимать `Person&` (по ссылке)
- Умножать `salary` на 1.1
- Захват: пустой

**3) Многоуровневая сортировка**
**Требования к лямбде:**
- Сохранить лямбду в переменную `compare`
- Принимать двух `const Person&` (a и b)
- Возвращать `true`, если a должен идти перед b
- Логика: сначала сравнить возраст, если он разный - вернуть a.age < b.age
- Если возраст одинаковый - вернуть a.name < b.name
- Захват: пустой

**4) Подсчет среднего возраста**
**Требования к лямбде:**
- Сохранить лямбду в переменную `calculateAverageAge`
- Захватить вектор `people` по ссылке (`[&people]`)
- Не принимать параметров (`()`)
- В теле лямбды:
    - Инициализировать переменную `sum = 0.0`
    - Пробежаться по всем элементам вектора `people`
    - Накопить сумму возрастов
    - Вернуть результат деления `sum / people.size()`
- Возвращаемый тип: `double`

### Формат ввода
Первая строка: целое число `N` — количество людей.  
Далее `N` строк: `name age salary` (имя без пробелов, возраст — целое, зарплата — число).  
Последняя строка: `k` — номер человека (1-based), чью зарплату нужно увеличить.

### Формат вывода
1. Количество людей старше 30.  
2. Новая зарплата выбранного человека (с двумя знаками после запятой).  
3. Имена людей после сортировки по возрасту и имени.  
4. Средний возраст (с двумя знаками после запятой).
"""

    def _generate_tests(self):
        random.seed(self.seed)
        self.tests = []
        name_pool = [
            "Anna", "Boris", "Ivan", "Maria", "Olga", "Pavel",
            "Daria", "Nikita", "Sergey", "Elena"
        ]

        for _ in range(5):
            n = random.randint(3, 6)
            names = random.sample(name_pool, n)
            ages = [random.randint(18, 60) for _ in range(n)]
            if n >= 2:
                ages[0] = ages[1]
            salaries = [random.randint(30, 120) * 10 for _ in range(n)]
            k = random.randint(1, n)

            people = [
                {"name": names[i], "age": ages[i], "salary": float(salaries[i])}
                for i in range(n)
            ]

            input_lines = [str(n)]
            input_lines += [
                f"{people[i]['name']} {people[i]['age']} {salaries[i]}"
                for i in range(n)
            ]
            input_lines.append(str(k))

            older_count = sum(1 for p in people if p["age"] > 30)
            people[k - 1]["salary"] *= 1.1
            sorted_people = sorted(people, key=lambda p: (p["age"], p["name"]))
            avg_age = sum(p["age"] for p in people) / n

            expected_lines = [
                str(older_count),
                f"{people[k - 1]['salary']:.2f}",
                " ".join(p["name"] for p in sorted_people),
                f"{avg_age:.2f}",
            ]
            expected_output = "\n".join(expected_lines)

            def make_compare(expected_count, expected_salary, expected_names, expected_avg):
                def _compare(obt, _exp):
                    lines = [line.strip() for line in obt.strip().splitlines() if line.strip()]
                    if len(lines) != 4:
                        return False
                    try:
                        count_val = int(lines[0])
                        salary_val = float(lines[1])
                        names_val = lines[2].split()
                        avg_val = float(lines[3])
                    except ValueError:
                        return False
                    if count_val != expected_count:
                        return False
                    if abs(salary_val - expected_salary) > 1e-2:
                        return False
                    if names_val != expected_names:
                        return False
                    return abs(avg_val - expected_avg) <= 1e-2

                return _compare

            self.tests.append(TestItem(
                input_str="\n".join(input_lines),
                showed_input="\n".join(input_lines),
                expected=expected_output,
                compare_func=make_compare(
                    older_count,
                    people[k - 1]["salary"],
                    [p["name"] for p in sorted_people],
                    avg_age,
                )
            ))
