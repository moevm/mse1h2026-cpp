from ....base_module import BaseTaskClass, TestItem
import random
import math


class OperatorsOverloadingMid2Test(BaseTaskClass):
    """Operators overloading -- Mid_difficulty_task_2 (Fraction)"""

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
#include <numeric>   // для std::gcd
#include <stdexcept>

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

        # Helper to compute expected output for (a/b + c/d) and equality check
        def expected_sum_eq(a, b, c, d):
            if b == 0 or d == 0:
                return "undefined\n0"
            num = a * d + c * b
            den = b * d
            g = math.gcd(num, den)
            num //= g
            den //= g
            if den < 0:
                num = -num
                den = -den
            eq = 1 if a * d == c * b else 0
            if den == 1:
                return f"{num}\n{eq}"
            return f"{num}/{den}\n{eq}"

        # --- Edge cases ---

        self.tests.append(TestItem(
            input_str="1 0 2 3",
            showed_input="zero_denominator",
            expected="undefined\n0",
            compare_func=lambda x, y: x.strip() == y.strip()
        ))

        # Both fractions equal (reduction check)
        self.tests.append(TestItem(
            input_str="1 2 2 4",
            showed_input="equal_fractions",
            expected=expected_sum_eq(1, 2, 2, 4),
            compare_func=lambda x, y: x.strip() == y.strip()
        ))

        # Negative denominator
        self.tests.append(TestItem(
            input_str="1 -2 1 3",
            showed_input="negative_denominator",
            expected=expected_sum_eq(1, -2, 1, 3),
            compare_func=lambda x, y: x.strip() == y.strip()
        ))

        # Whole numbers (denominator 1)
        self.tests.append(TestItem(
            input_str="3 1 5 1",
            showed_input="whole_numbers",
            expected="8\n0",
            compare_func=lambda x, y: x.strip() == y.strip()
        ))

        # Result reduces to integer
        self.tests.append(TestItem(
            input_str="1 3 2 3",
            showed_input="sum_to_integer",
            expected="1\n0",
            compare_func=lambda x, y: x.strip() == y.strip()
        ))

        # Zero numerator
        self.tests.append(TestItem(
            input_str="0 5 1 3",
            showed_input="zero_numerator",
            expected=expected_sum_eq(0, 5, 1, 3),
            compare_func=lambda x, y: x.strip() == y.strip()
        ))

        # --- Random tests (4) ---
        for _ in range(4):
            a = random.randint(-5, 5)
            b = random.randint(1, 5)  # avoid zero
            c = random.randint(-5, 5)
            d = random.randint(1, 5)
            expected = expected_sum_eq(a, b, c, d)
            self.tests.append(TestItem(
                input_str=f"{a} {b} {c} {d}",
                showed_input="random",
                expected=expected,
                compare_func=lambda x, y: x.strip() == y.strip()
            ))