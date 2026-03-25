from ...base_module import BaseTaskClass, TestItem


class OopEasy1Test(BaseTaskClass):
    """OOP -- Easy_Task_1"""

    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(
            compile_name="program",
            seed=seed,
            **kwargs
        )

    def generate_task(self) -> str:
        return (
            "Реализуйте класс Rectangle с инкапсуляцией, валидацией отрицательных "
            "значений и методами getArea/getPerimeter/isSquare."
        )

    def _generate_tests(self):
        self.tests = [
            TestItem(
                input_str="",
                showed_input="no input",
                expected="12\n14\n0\n0 5\n0\n1",
                compare_func=lambda x, y: x.strip() == y.strip()
            )
        ]
