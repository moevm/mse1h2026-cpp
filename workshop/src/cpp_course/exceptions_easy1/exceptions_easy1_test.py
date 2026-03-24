import random
from typing import Optional
from ...c_course.base_module import BaseTaskClass, TestItem

class ExceptionsEasy1Test(BaseTaskClass):
    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(
            compile_name="program",
            seed=seed,
            **kwargs
        )

    def compile(self) -> Optional[str]:
        return self._compile_internal(
            solution_name="solution.cpp",
            compiler="g++",
            compile_args="-std=c++20 -Wall -Werror",
        )

    def generate_task(self) -> str:
        return """# Задание: Калькулятор с исключениями

Реализуйте класс `Calculator`, который корректно обрабатывает ошибки с помощью `try-catch` и выбрасывает исключения.

### Требования:
1. **Класс `Calculator`**:
   - Метод `double divide(double a, double b) const`: выбрасывает `std::runtime_error("Деление на ноль невозможно")`, если `b == 0`.
   - Метод `double calculate(const std::string& op, double a, double b) const`: 
     - Поддерживает `+`, `-`, `*`, `/`.
     - Для `/` вызывает `divide`.
     - Если символ операции неизвестен, выбрасывает `std::invalid_argument("Неизвестная операция")`.
2. **Функция `main`**:
   - Считывает строку (операция) и два числа (`double`).
   - Оборачивает вызов `calculate` в блок `try-catch`.
   - При успехе выводит результат.
   - При исключении выводит текст ошибки через `e.what()`.

### Пример:
**Ввод:** `/ 10 0`  
**Вывод:** `Деление на ноль невозможно`
"""

    def _generate_tests(self):
        random.seed(self.seed)
        self.tests = []

        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b if b != 0 else "error"
        }

        # Стандартные тесты
        for op_char, func in ops.items():
            a, b = round(random.uniform(1, 100), 1), round(random.uniform(1, 100), 1)
            expected = func(a, b)
            self.tests.append(TestItem(
                input_str=f"{op_char} {a} {b}",
                showed_input=f"{a} {op_char} {b}",
                expected=str(expected),
                compare_func=lambda obt, exp: abs(float(obt) - float(exp)) < 1e-3
            ))

        # Тест на деление на ноль
        self.tests.append(TestItem(
            input_str="/ 10 0",
            showed_input="10 / 0",
            expected="Деление на ноль невозможно",
            compare_func=lambda obt, exp: exp in obt
        ))

        # Тест на неизвестную операцию
        self.tests.append(TestItem(
            input_str="? 5 5",
            showed_input="5 ? 5",
            expected="Неизвестная операция",
            compare_func=lambda obt, exp: exp in obt
        ))