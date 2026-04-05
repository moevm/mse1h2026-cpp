from ....base_module import BaseTaskClass, TestItem
import subprocess


class OperatorsOverloadingMid1Test(BaseTaskClass):

    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(
            compile_name="program",
            seed=seed,
            **kwargs
        )

    def generate_task(self) -> str:
        return """Mid_difficulty_task_1:
Реализовать класс SafeArray с перегрузками операторов:
[], =, +, ().
"""

    def _generate_tests(self):
        self.tests = [
            TestItem(
                input_str="",
                showed_input="",
                expected="",
                compare_func=lambda x, y: True
            )
        ]

    def compile(self, source_file: str) -> str:
        exe_file = "solution.exe"

        result = subprocess.run(
            ["g++", source_file, "-o", exe_file],
            capture_output=True
        )

        if result.returncode != 0:
            raise RuntimeError("Compilation failed")

        return exe_file

    def run(self, exe_file: str) -> int:
        result = subprocess.run([exe_file], capture_output=True)
        return result.returncode

    def check(self):
        exe = self.compile(self.solution_path)
        code = self.run(exe)

        if code == 0:
            return True, "OK"
        return False, f"Wrong answer (exit code {code})"