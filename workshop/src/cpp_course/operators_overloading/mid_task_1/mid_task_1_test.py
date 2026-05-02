from ....base_module import BaseTaskClass, TestItem
import random


class OperatorsOverloadingMid1Test(BaseTaskClass):

    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(compile_name="program", seed=seed, **kwargs)

    def generate_task(self):
        return """# Operators Overloading Mid 1

Реализуйте класс SafeArray:
- operator[] для доступа к элементам
- operator+ для поэлементного сложения
- operator= для копирования

Ввод:
n
массив A (n чисел)
массив B (n чисел)

Вывод:
результат поэлементного сложения A+B
"""

    def _generate_tests(self):
        random.seed(self.seed)
        self.tests = []

        for _ in range(5):
            n = random.randint(3, 5)
            a = [random.randint(-10, 10) for _ in range(n)]
            b = [random.randint(-10, 10) for _ in range(n)]

            result = [a[i] + b[i] for i in range(n)]
            expected = " ".join(map(str, result))

            self.tests.append(TestItem(
                input_str=f"{n}\n{' '.join(map(str,a))}\n{' '.join(map(str,b))}",
                showed_input=f"n={n}, A={a}, B={b}",
                expected=expected,
                compare_func=lambda x, y: x.strip() == y.strip()
            ))