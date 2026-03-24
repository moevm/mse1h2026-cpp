from ...base_module import BaseTaskClass, TestItem


class LambdaMid1Test(BaseTaskClass):
    """Lambda functions -- Mid_difficulty_task_1"""

    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(
            compile_name="program",
            seed=seed,
            **kwargs
        )

    def generate_task(self) -> str:
        return (
            "Реализуйте лямбды isOlderThan30, increaseSalary, compare и "
            "calculateAverageAge для структуры Person."
        )

    def _generate_tests(self):
        self.tests = [
            TestItem(
                input_str="",
                showed_input="no input",
                expected="1\n220\nAnna Boris Ivan\n30.33",
                compare_func=lambda x, y: x.strip() == y.strip()
            )
        ]
