from ....base_module import BaseTaskClass, TestItem
import random


class OperatorsOverloadingMid1Test(BaseTaskClass):
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

        # Edge case: empty arrays
        self.tests.append(TestItem(
            input_str="0\n\n",
            showed_input="empty",
            expected="SUM: \nCOPY: ",
            compare_func=lambda x, y: x.strip() == y.strip()
        ))

        # Static test (n=3)
        a = [1, 2, 3]
        b = [4, 5, 6]
        n = len(a)
        # program will copy a, then mutate a[0] += 1000
        a_mut = a[:]
        a_mut[0] += 1000
        sum_expected = a_mut + b
        expected = "SUM: " + " ".join(map(str, sum_expected)) + "\nCOPY: " + " ".join(map(str, a))
        self.tests.append(TestItem(
            input_str=f"{n}\n" + " ".join(map(str, a)) + "\n" + " ".join(map(str, b)),
            showed_input="static",
            expected=expected,
            compare_func=lambda x, y: x.strip() == y.strip()
        ))

        # Random tests
        for _ in range(4):
            n = random.randint(1, 6)  # at least 1 element
            a = [random.randint(0, 10) for _ in range(n)]
            b = [random.randint(0, 10) for _ in range(n)]
            a_mut = a[:]
            a_mut[0] += 1000
            sum_expected = a_mut + b
            expected = "SUM: " + " ".join(map(str, sum_expected)) + "\nCOPY: " + " ".join(map(str, a))
            self.tests.append(TestItem(
                input_str=f"{n}\n" + " ".join(map(str, a)) + "\n" + " ".join(map(str, b)),
                showed_input="random",
                expected=expected,
                compare_func=lambda x, y: x.strip() == y.strip()
            ))