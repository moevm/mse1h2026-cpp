from src.c_course.base_module import BaseTaskClass, TestItem
import subprocess

class OperatorsOverloadingEasy1Test(BaseTaskClass):

    def generate_task(self):
        return "Easy task: overload + and =="

    def _generate_tests(self):
        self.tests = [
            TestItem("", "", "", lambda x, y: True)
        ]

    def compile(self, source_file):
        exe = "solution.exe"
        subprocess.run(["g++", source_file, "-o", exe], check=True)
        return exe

    def run(self, exe):
        return subprocess.run([exe]).returncode

    def check(self):
        exe = self.compile(self.solution_path)
        return (True, "OK") if self.run(exe) == 0 else (False, "Wrong answer")