from typing import Optional

from src.base_module import BaseTaskClass, TestItem


class LambdaMid2Test(BaseTaskClass):
    """Lambda functions -- Mid_difficulty_task_2"""

    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(
            compile_name="program",
            seed=seed,
            **kwargs
        )

    def generate_task(self) -> str:
        return (
            "Реализуйте набор лямбд: counter, accumulator, multiplier, "
            "filter, stepCounter, maxTracker, averageCalc."
        )

    def _generate_tests(self):
        self.tests = [
            TestItem(
                input_str="",
                showed_input="no input",
                expected="1 2\n5 8\n15\n0 1\n2 4 6\n5 5 8\n5.00 6.00 7.00",
                compare_func=lambda x, y: x.strip() == y.strip()
            )
        ]
