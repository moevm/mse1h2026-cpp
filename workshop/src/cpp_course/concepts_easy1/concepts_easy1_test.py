from ...c_course.base_module import BaseTaskClass, TestItem
import random
from typing import Optional

class ConceptsEasy1Test(BaseTaskClass):

    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(
            compile_name="program",
            seed=seed,
            **kwargs
        )

    def compile(self) -> Optional[str]:
        # Важно: Концепты требуют стандарт не ниже c++20
        return self._compile_internal(
            solution_name="solution.cpp",
            compiler="g++",
            compile_args="-std=c++20 -Wall -Werror",
        )

    def generate_task(self) -> str:
        return """# Задание: Использование концептов (std::integral)

Напишите шаблонную функцию `add`, которая складывает два числа. Используйте стандартный концепт, чтобы ограничить принимаемые типы только целыми числами.

### Требования:
1. **Подключение**: Подключите заголовок `<concepts>`.
2. **Функция `add(a, b)`**:
   - Принимает два аргумента одного типа `T`.
   - Ограничение: `T` должен удовлетворять концепту `std::integral`.
   - Возвращает сумму `a + b`.
3. **Реализация `main`**:
   - Программа должна считывать два целых числа из стандартного ввода и выводить их сумму через функцию `add`.

### Пример:
**Ввод:** `5 10`  
**Вывод:** `15`
"""

    def _generate_tests(self):
        random.seed(self.seed)
        self.tests = []

        # Генерируем 5 случайных тестов
        for _ in range(5):
            a = random.randint(-1000, 1000)
            b = random.randint(-1000, 1000)
            self.tests.append(TestItem(
                input_str=f"{a} {b}",
                showed_input=f"{a} {b}",
                expected=str(a + b),
                compare_func=lambda x, y: x.strip() == y.strip()
            ))
