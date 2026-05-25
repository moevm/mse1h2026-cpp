import random
import re
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

**4) Оператор `<<` для вывода**
- Перегрузите оператор `<<` для вывода матрицы в поток.
- Выводит матрицу в формате:
```cpp
[ 1 0 0 ]
[ 0 1 0 ]
[ 0 0 1 ]
```

**5) Статический метод Identity()**
- Возвращает единичную матрицу (на главной диагонали 1, остальные 0).

### Формат ввода
1. 9 чисел для матрицы A (по строкам).  
2. 9 чисел для матрицы B (по строкам).  
3. `r c v` — позиция и значение для изменения A.  
4. `r1 c1` — позиция для чтения A.  
5. `r2 c2` — позиция для проверки выхода за границы.

### Формат вывода
1. Матрица `A * B`.  
2. Значение `A(r1, c1)` после изменения.  
3. Строка `out_of_range`, если доступ по `(r2, c2)` некорректен.  
4. Единичная матрица.
"""

    def _generate_tests(self):
        random.seed(self.seed)
        self.tests = []

        def multiply(a, b):
            result = [[0 for _ in range(3)] for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    result[i][j] = sum(a[i][k] * b[k][j] for k in range(3))
            return result

        def matrix_lines(matrix):
            return [f"[ {row[0]} {row[1]} {row[2]} ]" for row in matrix]

        for _ in range(4):
            a_vals = [random.randint(-5, 5) for _ in range(9)]
            b_vals = [random.randint(-5, 5) for _ in range(9)]
            a = [a_vals[i * 3:(i + 1) * 3] for i in range(3)]
            b = [b_vals[i * 3:(i + 1) * 3] for i in range(3)]

            r_mod, c_mod = random.randint(0, 2), random.randint(0, 2)
            new_val = random.randint(-5, 5)
            a[r_mod][c_mod] = new_val

            r_read, c_read = random.randint(0, 2), random.randint(0, 2)
            read_val = a[r_read][c_read]

            if random.choice([True, False]):
                r_bad, c_bad = 3, 0
            else:
                r_bad, c_bad = -1, 1

            product = multiply(a, b)

            expected_lines = matrix_lines(product)
            expected_lines.append(str(read_val))
            expected_lines.append("out_of_range")
            expected_lines += matrix_lines([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
            expected_output = "\n".join(expected_lines)

            input_lines = [
                " ".join(map(str, a_vals)),
                " ".join(map(str, b_vals)),
                f"{r_mod} {c_mod} {new_val}",
                f"{r_read} {c_read}",
                f"{r_bad} {c_bad}",
            ]

            def make_compare(expected_product, expected_read):
                def _compare(obt, _exp):
                    lines = [line.strip() for line in obt.strip().splitlines() if line.strip()]
                    if len(lines) != 8:
                        return False
                    for i in range(3):
                        values = re.findall(r"-?\d+", lines[i])
                        if len(values) != 3:
                            return False
                        if [int(v) for v in values] != expected_product[i]:
                            return False
                    try:
                        read_value = int(re.findall(r"-?\d+", lines[3])[0])
                    except (IndexError, ValueError):
                        return False
                    if read_value != expected_read:
                        return False
                    if "out_of_range" not in lines[4]:
                        return False
                    identity = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
                    for i in range(3):
                        values = re.findall(r"-?\d+", lines[5 + i])
                        if len(values) != 3:
                            return False
                        if [int(v) for v in values] != identity[i]:
                            return False
                    return True

                return _compare

            self.tests.append(TestItem(
                input_str="\n".join(input_lines),
                showed_input="\n".join(input_lines),
                expected=expected_output,
                compare_func=make_compare(product, read_val)
            ))
