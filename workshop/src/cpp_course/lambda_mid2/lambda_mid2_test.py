import random

from ...base_module import BaseTaskClass, TestItem


class LambdaMid2Test(BaseTaskClass):
    """Lambda functions -- Mid_difficulty_task_2"""

    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(
            compile_name="program",
            seed=seed,
            **kwargs
        )

    def generate_task(self) -> str:
        return """
# Задание

Необходимо реализовать лямбда выражения согласно условиям:

**1) Счетчик**
Создать лямбду `counter`, которая считает количество вызовов.

**Требования:**
- Захватить переменную `count` по значению с возможностью изменения (`mutable`)
- Не принимать параметров
- При каждом вызове увеличивать `count` на 1 и возвращать новое значение

**2) Накопитель (сумматор)**
Создать лямбду `accumulator`, которая накапливает сумму переданных чисел.

**Требования:**
- Захватить переменную `sum` по значению с возможностью изменения (`mutable`)
- Принимать один целочисленный параметр `value`
- При каждом вызове добавлять `value` к накопленной сумме
- Возвращать текущее значение суммы

**3) Множитель с коэффициентом**
Создать лямбду `multiplier`, которая умножает переданное число на заданный коэффициент.

**Требования:**
- Захватить переменную `factor` по значению
- Принимать один целочисленный параметр `x`
- Возвращать результат умножения `x * factor`

**4) Фильтр по порогу**
Создать лямбду `filter`, которая проверяет, превышает ли число заданный порог.

**Требования:**
- Захватить переменную `threshold` по значению
- Принимать один целочисленный параметр `x`
- Возвращать `true`, если `x > threshold`, иначе `false`

**5) Счетчик с шагом**
Создать лямбду `stepCounter`, которая увеличивает счетчик на заданный шаг.

**Требования:**
- Захватить переменные `count` и `step` по значению с возможностью изменения (`mutable`)
- Не принимать параметров
- При каждом вызове увеличивать `count` на `step` и возвращать новое значение

**6) Трекер максимума**
Создать лямбду `maxTracker`, которая отслеживает максимальное переданное значение.

**Требования:**
- Захватить переменную `maxVal` по значению с возможностью изменения (`mutable`)
- Принимать один целочисленный параметр `value`
- Если `value > maxVal`, обновлять `maxVal`
- Возвращать текущее значение максимума

**7) Калькулятор среднего**
Создать лямбду `averageCalc`, которая вычисляет среднее арифметическое всех переданных чисел.

**Требования:**
- Захватить переменные `sum` и `count` по значению с возможностью изменения (`mutable`)
- Принимать один целочисленный параметр `value`
- Добавлять `value` к сумме, увеличивать счетчик на 1
- Возвращать текущее среднее значение (`sum / count`) как `double`

### Формат ввода
Вводятся числа в следующем порядке:
1. `acc1 acc2` — значения для `accumulator`.
2. `factor multValue` — коэффициент и число для `multiplier`.
3. `threshold filter1 filter2` — порог и два значения для `filter`.
4. `step` — шаг для `stepCounter`.
5. `max1 max2 max3` — значения для `maxTracker`.
6. `avg1 avg2 avg3` — значения для `averageCalc`.

### Формат вывода
Выведите по строкам:
1. Результаты двух вызовов `counter`.
2. Результаты двух вызовов `accumulator`.
3. Результат `multiplier(multValue)`.
4. Результаты `filter(filter1)` и `filter(filter2)` (0 или 1).
5. Результаты трех вызовов `stepCounter`.
6. Результаты `maxTracker(max1)`, `maxTracker(max2)`, `maxTracker(max3)`.
7. Результаты `averageCalc` для трех значений (с двумя знаками после запятой).
"""

    def _generate_tests(self):
        random.seed(self.seed)
        self.tests = []
        tests_count = min(self.tests_num, 6)

        for _ in range(tests_count):
            acc1 = random.randint(-10, 10)
            acc2 = random.randint(-10, 10)
            factor = random.randint(2, 6)
            mult_value = random.randint(-5, 5)
            threshold = random.randint(-5, 5)
            filter1 = threshold
            filter2 = threshold + random.randint(1, 3)
            step = random.randint(1, 5)
            max_vals = [random.randint(-10, 10) for _ in range(3)]
            if max_vals[0] == max(max_vals):
                max_vals[2] = max_vals[0] + random.randint(1, 4)
            avg_vals = [random.randint(-10, 10) for _ in range(3)]

            counter_line = "1 2"
            accumulator_line = f"{acc1} {acc1 + acc2}"
            multiplier_line = str(factor * mult_value)
            filter_line = f"{int(filter1 > threshold)} {int(filter2 > threshold)}"
            step_line = f"{step} {step * 2} {step * 3}"

            running_max = []
            current_max = None
            for value in max_vals:
                current_max = value if current_max is None else max(current_max, value)
                running_max.append(current_max)
            max_line = " ".join(str(v) for v in running_max)

            avg_line_vals = []
            total = 0
            count = 0
            for value in avg_vals:
                total += value
                count += 1
                avg_line_vals.append(total / count)
            avg_line = " ".join(f"{v:.2f}" for v in avg_line_vals)

            input_lines = [
                f"{acc1} {acc2}",
                f"{factor} {mult_value}",
                f"{threshold} {filter1} {filter2}",
                f"{step}",
                f"{max_vals[0]} {max_vals[1]} {max_vals[2]}",
                f"{avg_vals[0]} {avg_vals[1]} {avg_vals[2]}",
            ]

            expected_lines = [
                counter_line,
                accumulator_line,
                multiplier_line,
                filter_line,
                step_line,
                max_line,
                avg_line,
            ]

            def make_compare(exp_lines, exp_avg):
                def _compare(obt: str, _exp: str) -> bool:
                    lines = [line.strip() for line in obt.strip().splitlines() if line.strip()]
                    if len(lines) != 7:
                        return False
                    if lines[:6] != list(exp_lines[:6]):
                        return False
                    try:
                        avg_values = [float(v) for v in lines[6].split()]
                    except ValueError:
                        return False
                    if len(avg_values) != len(exp_avg):
                        return False
                    for got, exp in zip(avg_values, exp_avg):
                        if abs(got - exp) > 1e-2:
                            return False
                    return True

                return _compare

            self.tests.append(TestItem(
                input_str="\n".join(input_lines),
                showed_input=" | ".join(input_lines),
                expected="\n".join(expected_lines),
                compare_func=make_compare(tuple(expected_lines), tuple(avg_line_vals))
            ))
