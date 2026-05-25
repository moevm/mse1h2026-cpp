from ...base_module import BaseTaskClass, TestItem
import random
from typing import Optional


class ConceptsHard2Test(BaseTaskClass):
    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(
            compile_name="program",
            seed=seed,
            **kwargs
        )


    def generate_task(self) -> str:
        return """# Задание: Собственный концепт Hashable

Реализуйте концепт, который проверяет поддержку стандартного хеширования для типа.

### Требования:
1. **Подключение**: `<iostream>`, `<concepts>`, `<string>` и `<functional>`.
2. **Концепт `Hashable<T>`**:
   - Проверяет, что для типа `T` можно создать объект `std::hash<T>`.
   - Проверяет, что выражение `std::hash<T>{}(x)` (где `x` имеет тип `T`) валидно.
   - Проверяет, что результат выражения конвертируется в `std::size_t`.
3. **Функция `printHash(const T& val)`**:
   - Шаблонная функция, ограниченная концептом `Hashable`.
   - Выводит результат `std::hash<T>{}(val)` в консоль.
4. **Реализация `main`**:
   - Считайте строку из стандартного ввода.
   - Вызовите `printHash` для этой строки.

### Пример:
**Ввод:** `cpp_rules`  
**Вывод:** (некоторое число, например `1438291032`)
"""

    def _generate_tests(self):
        random.seed(self.seed)
        self.tests = []

        # Для строк хеш в Python и C++ отличается, поэтому проверяем сам факт вывода числа
        test_strings = ["hello", "world", "42", "concept_test"]
        for s in test_strings:
            self.tests.append(TestItem(
                input_str=s,
                showed_input=s,
                expected="CHECK_NUMBER",  # Специальный флаг для проверки числового вывода
                compare_func=lambda obt, exp: obt.strip().isdigit()
            ))