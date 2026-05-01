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
};
```

Вам необходимо реализовать следующие лямбда выражения:

**1) Фильтрация по возрасту**
**Требования к лямбде:**
- Сохранить лямбду в переменную `isOlderThan30`
- Принимать `const Person&`
- Возвращать `true`, если возраст человека больше 30
- Захват: пустой

**2) Увеличение зарплаты**
**Требования к лямбде:**
- Сохранить лямбду в переменную `increaseSalary`
- Принимать `Person&` (по ссылке)
- Умножать `salary` на 1.1
- Захват: пустой

**3) Многоуровневая сортировка**
**Требования к лямбде:**
- Сохранить лямбду в переменную `compare`
- Принимать двух `const Person&` (a и b)
- Возвращать `true`, если a должен идти перед b
- Логика: сначала сравнить возраст, если он разный - вернуть a.age < b.age
- Если возраст одинаковый - вернуть a.name < b.name
- Захват: пустой

**4) Подсчет среднего возраста**
**Требования к лямбде:**
- Сохранить лямбду в переменную `calculateAverageAge`
- Захватить вектор `people` по ссылке (`[&people]`)
- Не принимать параметров (`()`)
- В теле лямбды:
    - Инициализировать переменную `sum = 0.0`
    - Пробежаться по всем элементам вектора `people`
    - Накопить сумму возрастов
    - Вернуть результат деления `sum / people.size()`
- Возвращаемый тип: `double`

### Формат ввода
В первой строке целое число `N` — количество людей. Далее `N` строк формата:
`name age salary`, где `name` — одно слово, `age` — целое число, `salary` — число с плавающей точкой.

### Формат вывода
1. Количество людей старше 30 лет.
2. Зарплата первого человека после повышения и сортировки.
3. Имена людей после сортировки (через пробел).
4. Средний возраст (с двумя знаками после запятой).
"""

    def _generate_tests(self):
        random.seed(self.seed)
        self.tests = []
        tests_count = min(self.tests_num, 6)
        name_pool = ["Anna", "Boris", "Ivan", "Daria", "Egor", "Fedor", "Gleb"]

        for _ in range(tests_count):
            n = random.randint(3, 5)
            names = random.sample(name_pool, n)
            ages = [random.randint(18, 45) for _ in range(n)]
            if n >= 2:
                ages[-1] = ages[-2]
            if max(ages) <= 30:
                ages[0] = 31
            salaries = [random.randint(5, 25) * 10 for _ in range(n)]

            people = list(zip(names, ages, salaries))
            older_count = sum(1 for _, age, _ in people if age > 30)

            updated_people = [
                {"name": name, "age": age, "salary": salary * 1.1}
                for name, age, salary in people
            ]
            sorted_people = sorted(
                updated_people,
                key=lambda p: (p["age"], p["name"])
            )
            first_salary = sorted_people[0]["salary"]
            names_line = " ".join(p["name"] for p in sorted_people)
            average_age = sum(ages) / len(ages)

            input_lines = [str(n)]
            input_lines += [
                f"{name} {age} {salary}"
                for name, age, salary in people
            ]

            expected = (
                f"{older_count}\n"
                f"{first_salary:.2f}\n"
                f"{names_line}\n"
                f"{average_age:.2f}"
            )

            def make_compare(exp_count, exp_salary, exp_names, exp_avg):
                def _compare(obt: str, _exp: str) -> bool:
                    lines = [line.strip() for line in obt.strip().splitlines() if line.strip()]
                    if len(lines) != 4:
                        return False
                    try:
                        if int(lines[0]) != exp_count:
                            return False
                        if abs(float(lines[1]) - exp_salary) > 1e-2:
                            return False
                        if lines[2] != exp_names:
                            return False
                        if abs(float(lines[3]) - exp_avg) > 1e-2:
                            return False
                    except ValueError:
                        return False
                    return True

                return _compare

            self.tests.append(TestItem(
                input_str="\n".join(input_lines),
                showed_input=" | ".join(input_lines),
                expected=expected,
                compare_func=make_compare(older_count, first_salary, names_line, average_age)
            ))
