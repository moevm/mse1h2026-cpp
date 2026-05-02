from ....base_module import BaseTaskClass, TestItem
import subprocess
import os


class OperatorsOverloadingMid1Test(BaseTaskClass):

    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(compile_name="program", seed=seed, **kwargs)

    def generate_task(self):
        return """Mid task 1:
Implement class SafeArray with overloaded operators:
[], =, +, ()
"""

    def _generate_tests(self):
        self.tests = [
            TestItem(
                input_str="",
                showed_input="no input",
                expected="10\n20\n30",   # <-- adjust
                compare_func=lambda x, y: x.strip() == y.strip()
            )
        ]

    def compile(self, source_file: str) -> str:
        exe_file = "solution.exe"
        source_file = os.path.join("/work", os.path.basename(source_file))

        result = subprocess.run(
            ["g++", source_file, "-o", exe_file],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise RuntimeError(f"Compilation failed:\n{result.stderr}")

        return exe_file

    def run(self, exe_file: str) -> str:
        result = subprocess.run(
            [f"./{exe_file}"],
            capture_output=True,
            text=True
        )
        return result.stdout

    def check(self):
        exe = self.compile(self.solution_path)

        for test in self.tests:
            output = self.run(exe)

            if not test.compare_func(output, test.expected):
                return False, f"Wrong answer\nExpected:\n{test.expected}\nGot:\n{output}"

        return True, "OK"