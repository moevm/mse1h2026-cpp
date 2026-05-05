from ....base_module import BaseTaskClass, TestItem
import random


class OperatorsOverloadingMid1Test(BaseTaskClass):
    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(compile_name="program", seed=seed, **kwargs)

    def generate_task(self) -> str:
        return """Задание
Дан класс SafeArray, который реализует динамический массив целых чисел с проверкой выхода за границы. Класс уже содержит конструкторы, деструктор и вспомогательные методы. Вам необходимо дописать класс SafeArray, добавив в него перегрузку пяти операторов:

Оператор [] - для доступа к элементам массива. Должен проверять выход за границы и выбрасывать исключение std::out_of_range.
Оператор = - для копирования массивов (глубокое копирование).
Оператор + - для склеивания двух массивов.
Оператор () - для изменения размера массива (принимает новый размер).

Код:
#include <iostream>

class SafeArray {
private:
    int* data;
    size_t size;

public:
    SafeArray(size_t s = 0) : size(s) {
        data = (size > 0) ? new int[size]() : nullptr;
    }

    SafeArray(const SafeArray& other) : size(other.size) {
        data = new int[size];
        for (size_t i = 0; i < size; i++) {
            data[i] = other.data[i];
        }
    }

    ~SafeArray() {
        delete[] data;
    }

    // Метод для получения размера
    size_t getSize() const { return size; }

    // 1. operator[] (доступ)

    // 2. operator= (присваивание)

    // 3. operator+ (конкатенация)

    // 4. operator() (изменение размера)
};
"""

    def _generate_tests(self):
        random.seed(self.seed)
        self.tests = []

        # STATIC TEST
        a = [1, 2, 3]
        b = [4, 5, 6]
        n = 3

        original_a = a[:]

        # COPY (before mutation)
        copy_arr = original_a[:]

        # MUTATION TEST
        a[0] = 999

        copy_arr = original_a[:]

        sum_arr = a + b

        expected = (
            "SUM: "
            + " ".join(map(str, sum_arr))
            + "\n"
            + "COPY: "
            + " ".join(map(str, copy_arr))
        )

        self.tests.append(
            TestItem(
                input_str=f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}",
                showed_input="arrays_static",
                expected=expected,
                compare_func=lambda x, y: x.strip() == y.strip(),
            )
        )

        # RANDOM TESTS
        for _ in range(4):
            n = random.randint(3, 6)
            a = [random.randint(0, 10) for _ in range(n)]
            b = [random.randint(0, 10) for _ in range(n)]

            
            original_a = a[:]

            # COPY before mutation
            copy_arr = original_a[:]

            # MUTATION TEST
            a[0] = a[0] + 1000

            # COPY
            copy_arr = original_a[:]

            # CONCATENATION
            sum_arr = a + b

            expected = (
                "SUM: "
                + " ".join(map(str, sum_arr))
                + "\n"
                + "COPY: "
                + " ".join(map(str, copy_arr))
            )

            self.tests.append(
                TestItem(
                    input_str=f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}",
                    showed_input="arrays_random",
                    expected=expected,
                    compare_func=lambda x, y: x.strip() == y.strip(),
                )
            )