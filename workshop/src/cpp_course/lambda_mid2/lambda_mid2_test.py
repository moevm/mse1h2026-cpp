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
        return """# Задание

Необходимо реализовать лямбда выражения согласно условиям:

**1) Счетчик**
Создать лямбду `counter`, которая считает количество вызовов.

**Требования:**
- Захватить переменную `count` по значению с возможностью изменения (`mutable`)
- Не принимать параметров
- При каждом вызове увеличивать `count` на 1 и возвращать новое значение

**Пример работы:**
```cpp
counter(); // 1
counter(); // 2
counter(); // 3
```


**2) Накопитель (сумматор)**
Создать лямбду `accumulator`, которая накапливает сумму переданных чисел.

**Требования:**
- Захватить переменную `sum` по значению с возможностью изменения (`mutable`)
- Принимать один целочисленный параметр `value`
- При каждом вызове добавлять `value` к накопленной сумме
- Возвращать текущее значение суммы

**Пример работы:**
```cpp
accumulator(5);  // 5
accumulator(3);  // 8
accumulator(10); // 18
```

**3) Множитель с коэффициентом**
Создать лямбду `multiplier`, которая умножает переданное число на заданный коэффициент.

**Требования:**
- Захватить переменную `factor` по значению
- Принимать один целочисленный параметр `x`
- Возвращать результат умножения `x * factor`

**Пример работы:**
```cpp
multiplier(5); // 15 (если factor = 3)
multiplier(5); // 15 (повторный вызов - состояние не меняется)
```

**4) Фильтр по порогу**
Создать лямбду `filter`, которая проверяет, превышает ли число заданный порог.

**Требования:**
- Захватить переменную `threshold` по значению
- Принимать один целочисленный параметр `x`
- Возвращать `true`, если `x > threshold`, иначе `false`

**Пример работы:**
```cpp
filter(5);  // false (threshold = 10)
filter(15); // true
```

**5) Счетчик с шагом**
Создать лямбду `stepCounter`, которая увеличивает счетчик на заданный шаг.

**Требования:**
- Захватить переменные `count` и `step` по значению с возможностью изменения (`mutable`)
- Не принимать параметров
- При каждом вызове увеличивать `count` на `step` и возвращать новое значение

**Пример работы:**
```cpp
stepCounter(); // 2 (если step = 2)
stepCounter(); // 4
stepCounter(); // 6
```

**6) Трекер максимума**
Создать лямбду `maxTracker`, которая отслеживает максимальное переданное значение.

**Требования:**
- Захватить переменную `maxVal` по значению с возможностью изменения (`mutable`)
- Принимать один целочисленный параметр `value`
- Если `value > maxVal`, обновлять `maxVal`
- Возвращать текущее значение максимума

**Пример работы:**
```cpp
maxTracker(5);  // 5
maxTracker(3);  // 5
maxTracker(8);  // 8
maxTracker(2);  // 8
```

**7) Калькулятор среднего**
Создать лямбду `averageCalc`, которая вычисляет среднее арифметическое всех переданных чисел.

**Требования:**
- Захватить переменные `sum` и `count` по значению с возможностью изменения (`mutable`)
- Принимать один целочисленный параметр `value`
- Добавлять `value` к сумме, увеличивать счетчик на 1
- Возвращать текущее среднее значение (`sum / count`) как `double`

**Пример работы:**
```cpp
averageCalc(5);  // 5.0
averageCalc(7);  // 6.0
averageCalc(9);  // 7.0
averageCalc(11); // 8.0
```

### Формат ввода
1. `n1` — количество вызовов `counter`.  
2. `n2` и далее `n2` чисел для `accumulator`.  
3. `factor`, `n3` и далее `n3` чисел для `multiplier`.  
4. `threshold`, `n4` и далее `n4` чисел для `filter`.  
5. `step`, `n5` — количество вызовов `stepCounter`.  
6. `maxVal`, `n6` и далее `n6` чисел для `maxTracker`.  
7. `n7` и далее `n7` чисел для `averageCalc`.

### Формат вывода
Выведите 7 строк:
1. Результаты вызовов `counter`.  
2. Результаты вызовов `accumulator`.  
3. Результаты вызовов `multiplier`.  
4. Результаты вызовов `filter` (0 или 1).  
5. Результаты вызовов `stepCounter`.  
6. Результаты вызовов `maxTracker`.  
7. Результаты вызовов `averageCalc` (с двумя знаками после запятой).
"""

    def _generate_tests(self):
        random.seed(self.seed)
        self.tests = []

        for _ in range(5):
            n1 = random.randint(2, 5)
            n2 = random.randint(2, 5)
            acc_values = [random.randint(-10, 10) for _ in range(n2)]

            factor = random.randint(-5, 5)
            n3 = random.randint(2, 5)
            mult_values = [random.randint(-10, 10) for _ in range(n3)]

            threshold = random.randint(-5, 10)
            n4 = random.randint(2, 5)
            filter_values = [random.randint(-10, 10) for _ in range(n4)]

            step = random.choice([-5, -3, -2, -1, 1, 2, 3, 5])
            n5 = random.randint(2, 5)

            max_val = random.randint(-10, 10)
            n6 = random.randint(3, 6)
            max_values = [random.randint(-10, 10) for _ in range(n6)]

            n7 = random.randint(3, 6)
            avg_values = [random.randint(-10, 10) for _ in range(n7)]

            counter_results = list(range(1, n1 + 1))

            acc_sum = 0
            acc_results = []
            for v in acc_values:
                acc_sum += v
                acc_results.append(acc_sum)

            mult_results = [v * factor for v in mult_values]

            filter_results = [1 if v > threshold else 0 for v in filter_values]

            step_count = 0
            step_results = []
            for _ in range(n5):
                step_count += step
                step_results.append(step_count)

            max_results = []
            current_max = max_val
            for v in max_values:
                if v > current_max:
                    current_max = v
                max_results.append(current_max)

            avg_results = []
            avg_sum = 0
            avg_count = 0
            for v in avg_values:
                avg_sum += v
                avg_count += 1
                avg_results.append(avg_sum / avg_count)

            expected_lines = [
                " ".join(map(str, counter_results)),
                " ".join(map(str, acc_results)),
                " ".join(map(str, mult_results)),
                " ".join(map(str, filter_results)),
                " ".join(map(str, step_results)),
                " ".join(map(str, max_results)),
                " ".join(f"{v:.2f}" for v in avg_results),
            ]
            expected_output = "\n".join(expected_lines)

            input_lines = [
                str(n1),
                f"{n2} " + " ".join(map(str, acc_values)),
                f"{factor} {n3} " + " ".join(map(str, mult_values)),
                f"{threshold} {n4} " + " ".join(map(str, filter_values)),
                f"{step} {n5}",
                f"{max_val} {n6} " + " ".join(map(str, max_values)),
                f"{n7} " + " ".join(map(str, avg_values)),
            ]

            def make_compare(expected):
                def _compare(obt, _exp):
                    lines = [line.strip() for line in obt.strip().splitlines() if line.strip()]
                    if len(lines) != 7:
                        return False
                    for line_obt, line_exp in zip(lines[:6], expected[:6]):
                        if line_obt.split() != line_exp.split():
                            return False
                    obt_avg = lines[6].split()
                    exp_avg = expected[6].split()
                    if len(obt_avg) != len(exp_avg):
                        return False
                    for o_val, e_val in zip(obt_avg, exp_avg):
                        try:
                            if abs(float(o_val) - float(e_val)) > 1e-2:
                                return False
                        except ValueError:
                            return False
                    return True

                return _compare

            self.tests.append(TestItem(
                input_str="\n".join(input_lines),
                showed_input="\n".join(input_lines),
                expected=expected_output,
                compare_func=make_compare(expected_lines)
            ))
