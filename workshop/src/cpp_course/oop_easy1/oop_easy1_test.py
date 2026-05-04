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
- double getWidth() const - возвращает ширину прямоугольника
- double getHeight() const - возвращает высоту прямоугольника
-  void setWidth(double width) - устанавливает новое значение ширины
    - Если передано отрицательное значение, устанавливать поле в `0.0`
- void setHeight(double height) - устанавливает новое значение высоты
    - Если передано отрицательное значение, устанавливать поле в `0.0`
- getArea(): возвращает площадь прямоугольника.
- getPerimeter(): возвращает периметр прямоугольника.
- isSquare(): возвращает true, если прямоугольник является квадратом (ширина равна высоте), иначе false.

### Формат ввода
1. `w1 h1` — ширина и высота первого прямоугольника.  
2. `w2 h2` — новые значения для первого прямоугольника.  
3. `w3 h3` — ширина и высота второго прямоугольника.

### Формат вывода
1. Площадь первого прямоугольника.  
2. Периметр первого прямоугольника.  
3. Признак квадрата для первого прямоугольника (0/1).  
4. Новая ширина и высота первого прямоугольника.  
5. Площадь первого прямоугольника после изменения.  
6. Признак квадрата для второго прямоугольника (0/1).
"""

    def _generate_tests(self):
        random.seed(self.seed)
        self.tests = []

        def clamp(value):
            return value if value >= 0 else 0

        for _ in range(5):
            w1, h1 = random.randint(-5, 10), random.randint(-5, 10)
            w2, h2 = random.randint(-5, 10), random.randint(-5, 10)
            w3, h3 = random.randint(-5, 10), random.randint(-5, 10)

            width1 = clamp(w1)
            height1 = clamp(h1)
            area1 = width1 * height1
            perim1 = 2 * (width1 + height1)
            square1 = 1 if width1 == height1 else 0

            width1 = clamp(w2)
            height1 = clamp(h2)
            area2 = width1 * height1

            width2 = clamp(w3)
            height2 = clamp(h3)
            square2 = 1 if width2 == height2 else 0

            expected_lines = [
                str(int(area1)),
                str(int(perim1)),
                str(square1),
                f"{int(width1)} {int(height1)}",
                str(int(area2)),
                str(square2),
            ]
            expected_output = "\n".join(expected_lines)

            input_lines = [
                f"{w1} {h1}",
                f"{w2} {h2}",
                f"{w3} {h3}",
            ]

            def make_compare(expected_vals):
                def _compare(obt, _exp):
                    lines = [line.strip() for line in obt.strip().splitlines() if line.strip()]
                    if len(lines) != 6:
                        return False
                    try:
                        area_val = float(lines[0])
                        perim_val = float(lines[1])
                        square_val = int(lines[2])
                        width_val, height_val = map(float, lines[3].split())
                        area2_val = float(lines[4])
                        square2_val = int(lines[5])
                    except ValueError:
                        return False

                    exp_area, exp_perim, exp_square, exp_w, exp_h, exp_area2, exp_square2 = expected_vals
                    if abs(area_val - exp_area) > 1e-6:
                        return False
                    if abs(perim_val - exp_perim) > 1e-6:
                        return False
                    if square_val != exp_square:
                        return False
                    if abs(width_val - exp_w) > 1e-6 or abs(height_val - exp_h) > 1e-6:
                        return False
                    if abs(area2_val - exp_area2) > 1e-6:
                        return False
                    return square2_val == exp_square2

                return _compare

            self.tests.append(TestItem(
                input_str="\n".join(input_lines),
                showed_input="\n".join(input_lines),
                expected=expected_output,
                compare_func=make_compare(
                    (
                        area1, perim1, square1,
                        width1, height1,
                        area2, square2,
                    )
                )
            ))
