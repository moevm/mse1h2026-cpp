import random
from ...base_module import BaseTaskClass, TestItem


class LambdaEasy1Test(BaseTaskClass):
    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(
            compile_name="program",
            seed=seed,
            **kwargs
        )


    def generate_task(self) -> str:
        return """# Задание: Четыре лика лямбда-выражений

Реализуйте программу, демонстрирующую различные способы работы с лямбдами в C++.

### Требования:
1. **Immediate Invocation**: Вызовите лямбду без параметров сразу (IIFE), которая выводит `Hello, Lambda!`.
2. **Параметры**: Создайте переменную `sum`, хранящую лямбду, принимающую два `int` и возвращающую их сумму.
3. **Захват по значению**: Создайте переменную `multiplier` (считайте её из ввода). Напишите лямбду, захватывающую её по значению, которая умножает свой аргумент на этот множитель.
4. **Захват по ссылке**: Создайте переменную `counter = 0`. Напишите лямбду, захватывающую её по ссылке, которая при каждом вызове инкрементирует `counter`.

### Формат вывода в main:
1. Вывод первой лямбды (строка).
2. Считайте `a, b, mult, val`.
3. Выведите результат `sum(a, b)`.
4. Выведите результат лямбды-множителя для `val`.
5. Вызовите лямбду-счетчик дважды и выведите итоговое значение `counter`.
"""

    def _generate_tests(self):
        random.seed(self.seed)
        self.tests = []

        for _ in range(5):
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            mult = random.randint(2, 10)
            val = random.randint(1, 50)

            expected_sum = a + b
            expected_mult = val * mult
            expected_counter = 2

            expected_output = (
                f"Hello, Lambda!\n"
                f"{expected_sum}\n"
                f"{expected_mult}\n"
                f"{expected_counter}"
            )

            self.tests.append(TestItem(
                input_str=f"{a} {b} {mult} {val}",
                showed_input=f"a={a}, b={b}, mult={mult}, val={val}",
                expected=expected_output,
                compare_func=lambda obt, exp: obt.strip() == exp.strip()
            ))