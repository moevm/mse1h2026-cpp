from ..base_module import BaseTaskClass
from ..base_module import TestItem
import random


class Lab1HelloTest(BaseTaskClass):
    """Задание 1: Hello, World!"""

    def __init__(self, seed: int = 42, mode: str = "init", name: str = "World", **kwargs):
        super().__init__(seed, mode, **kwargs)
        self.name = name

    def generate_task(self) -> str:
        """Генерирует текст задания"""
        return f"""# Лабораторная работа №1: Hello, World!

Напишите программу на C, которая выводит приветствие.

Вариант (seed={self.seed}): выведите "Hello, {self.name}!"

Требования:
- Используйте printf
- Добавьте перевод строки в конце
- Программа должна компилироваться без ошибок

Пример работы:
$ ./program
Hello, {self.name}!
"""

    def _generate_tests(self):
        """Генерирует тесты для проверки"""
        random.seed(self.seed)

        self.tests = []

        # Основной тест
        self.tests.append(TestItem(
            input_data="",
            expected_output=f"Hello, {self.name}!\n",
            description="Проверка вывода"
        ))

        # Дополнительные тесты для разных вариантов
        for i in range(3):
            test_name = f"Test_{i}"
            self.tests.append(TestItem(
                input_data="",
                expected_output=f"Hello, {self.name}!\n",
                description=f"Дополнительная проверка {i + 1}"
            ))

    def check(self):
        """Проверяет решение студента"""
        self.load_student_solution("solution.s")
        if not self.solution:
            return False, "Решение не загружено"

        # Здесь должна быть компиляция и запуск
        # Пока просто заглушка
        return True, "Все тесты пройдены!"