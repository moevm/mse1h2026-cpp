from ....base_module import BaseTaskClass, TestItem
import random

class OperatorsOverloadingEasy1Test(BaseTaskClass):
    def generate_task(self) -> str:
        return """Задание
Дан класс Point, описывающий точку на двухмерной плоскости с координатами x и y. Вам необходимо дописать класс Point, добавив в него перегрузку двух операторов:

Оператор + должен складывать координаты двух точек и возвращать новую точку.
Оператор == должен сравнивать две точки на равенство (возвращать true, если координаты совпадают, иначе - false).

Код:
#include <iostream>

class Point {
private:
    double x, y;

public:
    Point(double x = 0, double y = 0) : x(x), y(y) {}

    void print() const
    {
        std::cout << "(" << x << ", " << y << ")";
    }

    // ваш код перегрузки операторов

};
"""

    def _generate_tests(self):
        random.seed(self.seed)
        self.tests = []

        # Random tests (3 random points)
        for _ in range(3):
            x1 = random.randint(-10, 10)
            y1 = random.randint(-10, 10)
            x2 = random.randint(-10, 10)
            y2 = random.randint(-10, 10)
            expected = f"{x1+x2} {y1+y2}\n{1 if (x1==x2 and y1==y2) else 0}"
            self.tests.append(TestItem(
                input_str=f"{x1} {y1} {x2} {y2}",
                showed_input="random",
                expected=expected,
                compare_func=lambda x, y: x.strip() == y.strip()
            ))

        # Equal points
        x, y = 5, 7
        expected = f"{x+x} {y+y}\n1"
        self.tests.append(TestItem(
            input_str=f"{x} {y} {x} {y}",
            showed_input="equal points",
            expected=expected,
            compare_func=lambda x, y: x.strip() == y.strip()
        ))

        # Negative coordinates
        x1, y1 = -3, -4
        x2, y2 = -1, -2
        expected = f"{-4} {-6}\n0"
        self.tests.append(TestItem(
            input_str=f"{x1} {y1} {x2} {y2}",
            showed_input="negative",
            expected=expected,
            compare_func=lambda x, y: x.strip() == y.strip()
        ))