import random

from ...base_module import BaseTaskClass, TestItem


class OopHard2Test(BaseTaskClass):
    """OOP -- Hard_Task_2"""

    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(
            compile_name="program",
            seed=seed,
            **kwargs
        )

    def generate_task(self) -> str:
        return """# Задание

Создайте класс Matrix3x3, реализующий математическую матрицу 3 на 3.

**1) Конструкторы**
- По умолчанию: заполняет нулями.
- Списком инициализации: принимает массив или std::initializer_list из 9 элементов.

**2) Оператор * (умножение матриц)**
- Реализует математическое умножение двух матриц (строка на столбец).
- Возвращает новый объект Matrix3x3.

**3) Оператор () для доступа**
- matrix(row, col) должен возвращать ссылку на элемент.
- Должна быть константная и неконстантная версия.
- Проверка границ: если индекс < 0 или > 2, выбросить std::out_of_range.

**4) Оператор << для вывода**
- Перегрузите оператор `<<` для вывода матрицы в поток.
- Выводит матрицу в формате:
```cpp
[ 1 0 0 ]
[ 0 1 0 ]
[ 0 0 1 ]
```

**5) Статический метод Identity()**
- Возвращает единичную матрицу (на главной диагонали 1, остальные 0).

### Формат ввода
1. 9 целых чисел — матрица A (по строкам).
2. 9 целых чисел — матрица B (по строкам).
3. Два числа `row col` для доступа к элементу результата.
4. Два числа `badRow badCol` для проверки выхода за границы.

### Формат вывода
1. Значение элемента (row, col) матрицы `A * B`.
2. Строку `oor`, если при доступе с `badRow badCol` выбрасывается `std::out_of_range`.
3. Единичную матрицу через оператор `<<`.
"""

    def _generate_tests(self):
        random.seed(self.seed)
        self.tests = []
        tests_count = min(self.tests_num, 5)

        def format_matrix(mat):
            return "\n".join(
                f"[ {row[0]} {row[1]} {row[2]} ]"
                for row in mat
            )

        for _ in range(tests_count):
            a_vals = [random.randint(-3, 4) for _ in range(9)]
            b_vals = [random.randint(-3, 4) for _ in range(9)]
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            bad_row = random.choice([-1, 3])
            bad_col = random.choice([-1, 3])

            a = [a_vals[i * 3:(i + 1) * 3] for i in range(3)]
            b = [b_vals[i * 3:(i + 1) * 3] for i in range(3)]
            product = [[0] * 3 for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    product[i][j] = sum(a[i][k] * b[k][j] for k in range(3))

            identity = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
            expected_lines = [
                str(product[row][col]),
                "oor",
                format_matrix(identity),
            ]
            expected = "\n".join([
                expected_lines[0],
                expected_lines[1],
                expected_lines[2],
            ])

            input_lines = [
                " ".join(str(v) for v in a_vals),
                " ".join(str(v) for v in b_vals),
                f"{row} {col}",
                f"{bad_row} {bad_col}",
            ]

            def make_compare(exp_matrix=format_matrix(identity), exp_value=product[row][col]):
                def _compare(obt: str, _exp: str) -> bool:
                    lines = [line.rstrip() for line in obt.strip().splitlines() if line.strip()]
                    if len(lines) != 5:
                        return False
                    try:
                        if int(lines[0]) != exp_value:
                            return False
                    except ValueError:
                        return False
                    if lines[1] != "oor":
                        return False
                    return "\n".join(lines[2:]) == exp_matrix

                return _compare

            self.tests.append(TestItem(
                input_str="\n".join(input_lines),
                showed_input=" | ".join(input_lines),
                expected=expected,
                compare_func=make_compare()
            ))
