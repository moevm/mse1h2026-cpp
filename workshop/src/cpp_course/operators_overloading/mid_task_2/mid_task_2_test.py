from ....base_module import BaseTaskClass, TestItem
import random


class OperatorsOverloadingMid2Test(BaseTaskClass):

    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(compile_name="program", seed=seed, **kwargs)

    def generate_task(self):
        return """# Operators Overloading Mid 2

Реализуйте класс Fraction:
- operator+ для сложения дробей
- operator== для проверки равенства

Дробь задаётся двумя числами: числитель и знаменатель.

Ввод:
a b c d
(дроби a/b и c/d)

Вывод:
результат сложения дробей в формате num/den
"""

    def _generate_tests(self):
        random.seed(self.seed)
        self.tests = []

        for _ in range(5):
            a = random.randint(-5, 5)
            b = random.randint(1, 5)
            c = random.randint(-5, 5)
            d = random.randint(1, 5)

            num = a * d + c * b
            den = b * d

            expected = f"{num}/{den}"

            self.tests.append(TestItem(
                input_str=f"{a} {b} {c} {d}",
                showed_input=f"{a}/{b} + {c}/{d}",
                expected=expected,
                compare_func=lambda x, y: x.strip() == y.strip()
            ))