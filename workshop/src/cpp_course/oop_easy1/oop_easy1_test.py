import random

from ...base_module import BaseTaskClass, TestItem


class OopEasy1Test(BaseTaskClass):
    """OOP -- Easy_Task_1"""

    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(
            compile_name="program",
            seed=seed,
            **kwargs
        )

    def generate_task(self) -> str:
        return """# Задание

Вам нужно реализовать класс Rectangle, описывающий прямоугольник. Класс должен обеспечивать инкапсуляцию данных и предоставлять методы для вычисления геометрических характеристик.

**1) Приватные поля**
- width (ширина) типа double
- height (высота) типа double

**2) Конструктор**
- Принимает два параметра: ширину и высоту.
- Если передано отрицательное значение, устанавливать поле в 0.0.

**3) Методы**
- double getWidth() const - возвращает ширину прямоугольника
- double getHeight() const - возвращает высоту прямоугольника
- void setWidth(double width) - устанавливает новое значение ширины
    - Если передано отрицательное значение, устанавливать поле в 0.0
- void setHeight(double height) - устанавливает новое значение высоты
    - Если передано отрицательное значение, устанавливать поле в 0.0
- getArea(): возвращает площадь прямоугольника.
- getPerimeter(): возвращает периметр прямоугольника.
- isSquare(): возвращает true, если прямоугольник является квадратом (ширина равна высоте), иначе false.

### Формат ввода
Шесть чисел: `w h newW newH sqW sqH`.

### Формат вывода
1. Площадь и периметр прямоугольника `Rectangle(w, h)` (каждое с новой строки).
2. Результат `isSquare()` для `Rectangle(w, h)`.
3. Значения ширины и высоты после `setWidth(newW)` и `setHeight(newH)`.
4. Площадь после изменения размеров.
5. Результат `isSquare()` для `Rectangle(sqW, sqH)`.
"""

    def _generate_tests(self):
        random.seed(self.seed)
        self.tests = []
        tests_count = min(self.tests_num, 6)

        for _ in range(tests_count):
            w = random.randint(-5, 10)
            h = random.randint(-5, 10)
            new_w = random.randint(-5, 10)
            new_h = random.randint(-5, 10)
            sq_w = random.randint(-3, 8)
            sq_h = random.randint(-3, 8)

            width = max(w, 0)
            height = max(h, 0)
            area = width * height
            perimeter = 2 * (width + height)
            is_square = int(width == height)

            width2 = max(new_w, 0)
            height2 = max(new_h, 0)
            area2 = width2 * height2

            sq_width = max(sq_w, 0)
            sq_height = max(sq_h, 0)
            is_square2 = int(sq_width == sq_height)

            input_line = f"{w} {h} {new_w} {new_h} {sq_w} {sq_h}"
            expected_lines = [
                f"{area}",
                f"{perimeter}",
                f"{is_square}",
                f"{width2} {height2}",
                f"{area2}",
                f"{is_square2}",
            ]

            def make_compare(
                exp_area=area,
                exp_perimeter=perimeter,
                exp_square=is_square,
                exp_width=width2,
                exp_height=height2,
                exp_area2=area2,
                exp_square2=is_square2,
            ):
                def _compare(obt: str, _exp: str) -> bool:
                    lines = [line.strip() for line in obt.strip().splitlines() if line.strip()]
                    if len(lines) != 6:
                        return False
                    try:
                        if abs(float(lines[0]) - exp_area) > 1e-6:
                            return False
                        if abs(float(lines[1]) - exp_perimeter) > 1e-6:
                            return False
                        if int(lines[2]) != exp_square:
                            return False
                        width_line = lines[3].split()
                        if len(width_line) != 2:
                            return False
                        if abs(float(width_line[0]) - exp_width) > 1e-6:
                            return False
                        if abs(float(width_line[1]) - exp_height) > 1e-6:
                            return False
                        if abs(float(lines[4]) - exp_area2) > 1e-6:
                            return False
                        if int(lines[5]) != exp_square2:
                            return False
                    except ValueError:
                        return False
                    return True

                return _compare

            self.tests.append(TestItem(
                input_str=input_line,
                showed_input=input_line,
                expected="\n".join(expected_lines),
                compare_func=make_compare()
            ))
