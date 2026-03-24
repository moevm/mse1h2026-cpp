from typing import Optional

from src.base_module import BaseTaskClass, TestItem


class OopHard1Test(BaseTaskClass):
    """OOP -- Hard_Task_1"""

    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(
            compile_name="program",
            seed=seed,
            **kwargs
        )

    def generate_task(self) -> str:
        return (
            "Реализуйте структуры Book и класс Library с защитой от дублей по hash, "
            "поиском по автору/названию и печатью содержимого."
        )

    def _generate_tests(self):
        self.tests = [
            TestItem(
                input_str="",
                showed_input="no input",
                expected="Book already exists\n2\n0\nCpp (A, 2001) - [h1]",
                compare_func=lambda x, y: x.strip() == y.strip()
            )
        ]
