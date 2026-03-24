from typing import Optional

from src.base_module import BaseTaskClass, TestItem


class OopHard2Test(BaseTaskClass):
    """OOP -- Hard_Task_2"""

    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(
            compile_name="program",
            seed=seed,
            **kwargs
        )

    def generate_task(self) -> str:
        return (
            "Реализуйте класс Matrix3x3 с оператором умножения, оператором доступа (), "
            "оператором вывода << и статическим методом Identity()."
        )

    def _generate_tests(self):
        self.tests = [
            TestItem(
                input_str="",
                showed_input="no input",
                expected="8\noor\n[ 1 0 0 ]\n[ 0 1 0 ]\n[ 0 0 1 ]",
                compare_func=lambda x, y: x.strip() == y.strip()
            )
        ]
