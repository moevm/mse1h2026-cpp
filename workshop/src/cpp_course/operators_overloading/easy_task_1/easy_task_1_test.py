from ....base_module import BaseTaskClass, TestItem
import random


class OperatorsOverloadingEasy1Test(BaseTaskClass):

    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(compile_name="program", seed=seed, **kwargs)

    def generate_task(self):
        return """# Operators Overloading Easy

Реализовать класс Point:
- operator+
- operator==

В main:
считать 4 числа: x1 y1 x2 y2
вывести:
(x1+x2) (y1+y2)
и затем 1 если равны, иначе 0
"""

    def _generate_tests(self):
        random.seed(self.seed)
        self.tests = []

        for _ in range(5):
            x1, y1 = random.randint(-10, 10), random.randint(-10, 10)
            x2, y2 = random.randint(-10, 10), random.randint(-10, 10)

            sx = x1 + x2
            sy = y1 + y2

            eq = 1 if (x1 == x2 and y1 == y2) else 0

            expected = f"{sx} {sy}\n{eq}"

            self.tests.append(TestItem(
                input_str=f"{x1} {y1} {x2} {y2}",
                showed_input=f"{x1},{y1} + {x2},{y2}",
                expected=expected,
                compare_func=lambda x, y: x.strip() == y.strip()
            ))