from ....base_module import BaseTaskClass, TestItem
import random


class OperatorsOverloadingMid2Test(BaseTaskClass):
    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(compile_name="program", seed=seed, **kwargs)

    def generate_task(self) -> str:
        return """Задание
Дан класс Fraction для работы с обыкновенными дробями. Дробь хранится в виде числителя и знаменателя, всегда сокращенной. Класс уже содержит конструктор, метод сокращения и метод вывода. Вам необходимо дописать класс Fraction, добавив в него перегрузку операторов:

Арифметические операторы: +, -, *, / - для выполнения соответствующих операций с дробями. (возвращает новый объект класса)
Операторы сравнения: ==, !=, <, >, <=, >= - для сравнения дробей. (возвращает true и false)
Оператор преобразования в double - для преобразования дроби в число с плавающей точкой.

Исходный код
#include <iostream>

class Fraction {
private:
    int numerator;
    int denominator;
    
    // Сокращение дроби
    void reduce() {
        if (denominator < 0) {
            numerator = -numerator;
            denominator = -denominator;
        }
        int gcd = std::gcd(abs(numerator), denominator);
        numerator /= gcd;
        denominator /= gcd;
    }
    
public:
    Fraction(int num = 0, int den = 1) : numerator(num), denominator(den) {
        if (den == 0) {
            throw std::invalid_argument("Знаменатель не может быть нулем");
        }
        reduce();
    }
    
    void print() const {
        std::cout << numerator;
        if (denominator != 1) {
            std::cout << "/" << denominator;
        }
    }
    
    // 1. Арифметические операторы: +, -, *, /
    
    // 2. Операторы сравнения: ==, !=, <, >, <=, >=
    
    // 3. Оператор преобразования в double
};
"""

    def _generate_tests(self):
        random.seed(self.seed)
        self.tests = []

        # STATIC TEST
        a, b, c, d = 1, 2, 2, 4  # equal fractions

        num = a * d + c * b
        den = b * d
        equal = 1

        expected = f"{num}/{den}\n{equal}"

        self.tests.append(
            TestItem(
                input_str=f"{a} {b} {c} {d}",
                showed_input="equal_fractions",
                expected=expected,
                compare_func=lambda x, y: x.strip() == y.strip(),
            )
        )

        # RANDOM TESTS
        for _ in range(4):
            a = random.randint(1, 5)
            b = random.randint(1, 5)
            c = random.randint(1, 5)
            d = random.randint(1, 5)

            num = a * d + c * b
            den = b * d

            equal = 1 if (a * d == c * b) else 0

            expected = f"{num}/{den}\n{equal}"

            self.tests.append(
                TestItem(
                    input_str=f"{a} {b} {c} {d}",
                    showed_input="fractions_random",
                    expected=expected,
                    compare_func=lambda x, y: x.strip() == y.strip(),
                )
            )