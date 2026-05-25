from ...base_module import BaseTaskClass, TestItem
import random
from typing import Optional


class ConceptsHard1Test(BaseTaskClass):

    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(
            compile_name="program",
            seed=seed,
            **kwargs
        )


    def generate_task(self) -> str:
        return """# Задание: Ограничение диапазона (std::totally_ordered)

Реализуйте шаблонную функцию `safe_clamp`, которая ограничивает значение заданным диапазоном.

### Требования:
1. **Подключение**: Подключите `<concepts>` и `<iostream>`.
2. **Функция `safe_clamp(val, min, max)`**:
   - Все три аргумента имеют один тип `T`.
   - Ограничение: тип `T` должен удовлетворять концепту `std::totally_ordered`.
   - Логика:
     - Если `val < min`, вернуть `min`.
     - Если `val > max`, вернуть `max`.
     - Иначе вернуть `val`.
3. **Реализация `main`**:
   - Считайте три числа типа `double` (значение, минимум, максимум).
   - Выведите результат работы `safe_clamp`.

### Пример:
**Ввод:** `15.5 0.0 10.0`  
**Вывод:** `10`
"""

    def _generate_tests(self):
        random.seed(self.seed)
        self.tests = []

        # Функция для эмуляции clamp в Python
        def py_clamp(v, lo, hi):
            return max(lo, min(v, hi))

        # Генерируем 10 тестов с плавающей точкой
        for _ in range(10):
            # Генерируем диапазон
            v1 = round(random.uniform(-1000, 1000), 2)
            v2 = round(random.uniform(-1000, 1000), 2)
            lo, hi = min(v1, v2), max(v1, v2)

            # Генерируем значение (иногда внутри, иногда снаружи)
            choice = random.choice(['inside', 'below', 'above'])
            if choice == 'inside':
                val = round(random.uniform(lo, hi), 2)
            elif choice == 'below':
                val = round(lo - random.uniform(1, 100), 2)
            else:
                val = round(hi + random.uniform(1, 100), 2)

            expected = py_clamp(val, lo, hi)

            self.tests.append(TestItem(
                input_str=f"{val} {lo} {hi}",
                showed_input=f"val={val}, range=[{lo}, {hi}]",
                expected=str(expected),
                # Используем float comparison для надежности
                compare_func=lambda obt, exp: abs(float(obt) - float(exp)) < 1e-5
            ))