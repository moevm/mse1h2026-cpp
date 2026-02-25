import os
from typing import Optional

from ..base_module import BaseTaskClass
from ..base_module import TestItem
import random


class Lab1HelloTest(BaseTaskClass):
    """Задание 1: Hello, World!"""

    def __init__(self, seed: int = 42, mode: str = "init", name: str = "World", **kwargs):
        # Явно указываем все параметры для родительского класса
        super().__init__(
            compile_name="program",  # Явно задаем имя исполняемого файла
            seed=seed,               # Передаем seed
            **kwargs                 # Остальные параметры
        )
        self.name = name
        self.mode = mode

    def compile(self) -> Optional[str]:
        """Компиляция C программы"""
        print(f"DEBUG: Начинаем компиляцию, prog_name = {self.prog_name}")
        print(f"DEBUG: jail_path = {self.jail_path}")

        result = self._compile_internal(
            solution_name="solution.c",
            compiler="gcc",
            compile_args="-Wall -o program"  # Явно указываем выходной файл
        )

        # Проверим, создался ли файл
        if os.path.exists("program"):
            print("DEBUG: Файл program создан успешно")
        else:
            print("DEBUG: Файл program НЕ создан")

        return result
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
        self.tests.append(TestItem(
            input_str="",
            showed_input='no input',
            expected=f"Hello, {self.name}!",
            compare_func=lambda x, y: x==y
        ))


    def check(self, solution_filename: str = "solution.c") -> tuple[bool, str]:
        """Проверяет решение студента"""
        try:
            self.load_student_solution(solution_filename)

            # Проверка предварительных условий
            if (msg := self.check_sol_prereq()) is not None:
                return False, msg
            # Компиляция
            if (msg := self.compile()) is not None:
                return False, msg

            self._generate_tests()

            # Запуск тестов
            return self.run_tests()

        except Exception as e:
            return False, f"Непредвиденная ошибка во время проверки решения: {e}"