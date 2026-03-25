from typing import Optional, Callable
import enum
import os
import subprocess
import shlex
from dataclasses import dataclass
from pathlib import Path

COMPILE_TIMEOUT = 60
RUN_TIMEOUT = 5

FAILED_TEST_MSG = "Test is failed.\nInput: '{inp}'\nObtained: '{obt}'.\nExpected: '{exp}'"

DEFAULT_TEST_NUM = 50


@dataclass
class TestItem:
    input_str: str
    showed_input: str
    expected: str
    compare_func: Callable[[str, str], bool]


class BaseTaskClass:

    def __init__(
            self, compile_name: str = "program", seed: int = 0,
            tests_num: int = DEFAULT_TEST_NUM, fail_on_first_test: bool = True,
            array_align: str = "center", jail_exec: str = "chroot",
            jail_path: Optional[str] = None, output_type: Optional[str] = 'bash', solution: Optional[str] = None,
    ):
        self.solution = solution
        self.check_files = {}
        self.static_check_files = {}
        self.prog_name = compile_name
        self.seed = seed
        self.tests_num = tests_num
        self.tests: list[TestItem] = []
        self.compile_timeout = COMPILE_TIMEOUT
        self.run_timeout = RUN_TIMEOUT
        self.fail_on_first = fail_on_first_test
        self._array_align = array_align
        self.allowed_symbols = []
        self.jail_exec = jail_exec
        self.jail_path = jail_path if jail_path is not None else os.environ.get("JAIL_PATH", "")
        self.output_type = output_type

    def check_sol_prereq(self) -> Optional[str]:
        """
        This is counter-intuitive, but more straightforward than other ways:
        on success it returns None, on failure it returns str with an error
        """
        lines = self.solution.splitlines()

        if len(lines) == 0:
            return "Ошибка: пустой файл."

        return None

    def _compile_file(self, file: str, compiler: str, compile_args: str, output: str = None):
        if output is not None:
            compile_args += f" -o {output} -fno-common -std=c11 -g -Wall -Werror -fsanitize=address"

        compile_command = shlex.split(f"{compiler} -c {compile_args} {file}")

        try:
            p = subprocess.run(
                compile_command,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                timeout=self.compile_timeout, check=False
            )
        except subprocess.TimeoutExpired:
            return "Timeout при компиляции"

        try:
            return p.stdout.decode('utf-8')
        except UnicodeDecodeError:
            return f"Ошибка декодирования вывода. Ожидалась UTF-8, получены бинарные данные: {p.stdout!r}"

    def _compile_internal(
            self,
            compiler,
            compile_args
    ) -> Optional[str]:
        """
        General method to compile C work
        """
        solution_name = "/work/" + self.solution
        obj_files = []

        for src_file in self.check_files.keys():
            err = self._compile_file(src_file, compiler, compile_args)
            if err is not None:
                return f"Ошибка при компиляции кода системы проверки, файл {src_file} (обратитесь за помощью к авторам курса):\n{err}"

            obj_files.append(src_file[:src_file.find('.') + 1] + "o")

        output_file = os.path.join(self.jail_path, self.prog_name)
        if obj_files:
            compile_args_list = [compiler, solution_name] + obj_files + shlex.split(compile_args) + ["-o", output_file]
        else:
            compile_args_list = [compiler, solution_name] + shlex.split(compile_args) + ["-o", output_file]

        try:
            p = subprocess.run(
                compile_args_list,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                check=False,
                timeout=self.compile_timeout
            )
        except subprocess.TimeoutExpired:
            return "Timeout при компиляции"

        if p.returncode != 0:
            output = p.stdout
            try:
                error_msg = output.decode('utf-8')
                return f"Ошибка при компиляции решения:\n{error_msg}"
            except UnicodeDecodeError:
                return f"Ошибка при компиляции решения:\n{output.decode('latin-1', errors='replace')}"
        return None

    def compile(self) -> Optional[str]:
        """Компиляция программы"""
        file_extention = self.solution.split('.')[-1]
        if file_extention == 'cpp':
            result = self._compile_internal(
                compiler="g++",
                compile_args="-std=c++20 -Wall -Werror",
            )
        else:
            result = self._compile_internal(
                compiler="gcc",
                compile_args="-Wall"
            )

        return result

    def generate_task(self) -> str:
        return "TODO: Base class"

    def _generate_tests(self):
        pass

    def _run_solution_internal(
            self, test: TestItem,
            prog_args: str = "",
    ) -> Optional[tuple[str, str]]:
        """
        Run solution natively (compiled with gcc)
        """
        # Формируем путь к исполняемому файлу
        if self.jail_path and self.jail_path.strip():
            # Если есть jail_path, используем его
            prog_path = os.path.join(self.jail_path, self.prog_name)
            run_command = f"{self.jail_exec} {self.jail_path} {prog_path} {prog_args}"
        else:
            # Если jail_path пустой, запускаем из текущей директории
            prog_path = Path.cwd() / self.prog_name
            run_command = f"{prog_path} {prog_args}"


        try:
            p = subprocess.run(
                shlex.split(run_command),
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE,
                input=test.input_str.encode(),
                timeout=self.run_timeout, check=False,
            )
        except subprocess.TimeoutExpired as te:
            return (f"Выполнение программы превысило ограничение в {te.timeout} секунд",
                    f"Программа выполняется менее {te.timeout} секунд")
        except FileNotFoundError as e:
            return (f"Не найден исполняемый файл: {prog_path}. Ошибка: {e}",
                    "Программа должна быть скомпилирована")
        except Exception as e:
            return (f"Ошибка при запуске: {e}",
                    "Программа должна быть скомпилирована")

        output = p.stderr.decode().strip() + p.stdout.decode().strip()

        if p.returncode != 0:
            return (f"Программа завершилась с кодом {p.returncode}. Вывод:\n{output}",
                    "Программа завершилась с кодом 0")

        passed = test.compare_func(output, test.expected)
        if passed:
            return None
        return output, test.expected

    def _compare_default(self, input_str: str, obtained: str) -> bool:
        return input_str.strip() == obtained.strip()

    def run_solution(self, test: TestItem) -> Optional[str]:
        return self._run_solution_internal(test)

    def make_failed_test_msg(
            self, showed_input: str, obtained: str, expected: str
    ) -> str:
        return FAILED_TEST_MSG.format(
            inp=showed_input,
            obt=obtained,
            exp=expected
        )

    def run_tests(self) -> tuple[bool, str]:
        msgs = []
        for t in self.tests:
            if (result := self.run_solution(t)) is not None:
                msgs.append(self.make_failed_test_msg(
                    t.showed_input, result[0], result[1]
                ))
                if self.fail_on_first:
                    break

        if len(msgs) == 0:
            return True, "OK"
        return False, "\n".join(msgs)

    def init_task(self) -> str:
        return self.generate_task()

    def check(self) -> tuple[bool, str]:
        """Проверяет решение студента"""
        try:
            if (msg := self.check_sol_prereq()) is not None:
                return False, msg
            if (msg := self.compile()) is not None:
                return False, msg

            self._generate_tests()

            return self.run_tests()

        except Exception as e:
            return False, f"Непредвиденная ошибка во время проверки решения: {e}"

    def make_array_failed_test_msg(
            self, caption: list[str], arrs: list[list], max_col_len: int,
            correctness: list[bool],
    ) -> str:
        """
        format:
        | i | caption[0] | caption[1] | ... | caption[N] | Correct |
        +---+------------+------------+-----+------------+---------+
        | 0 | arrs[0][0] | arrs[1][0] | ... | arrs[N][0] |    X    |
        | 1 | arrs[0][1] | arrs[1][1] | ... | arrs[N][1] |    V    |
        ....
        +---+------------+------------+-----+------------+---------+
        """
        ret = ""
        cols = ["i"]
        cols_lens = [max(len(cols[0]), len(str(len(correctness))))]
        cols += caption
        cols_lens += [max(max_col_len, len(col)) for col in cols[1:]]
        cols.append("Correct")
        correct_s, fail_s = "V", "X"
        cols_lens.append(max(map(len, (correct_s, fail_s, cols[-1]))))
        # cols_lens[:] = (col_len + 2 for col_len in cols_lens)
        ret += "| " + " | ".join(
            col.center(col_len)
            for col, col_len in zip(cols, cols_lens)
        ) + " |\n"
        separator = "+" + "+".join("-" * (col_len + 2) for col_len in cols_lens) + "+\n"
        ret += separator
        corr_iter = (correct_s if c else fail_s for c in correctness)
        for vals in zip(range(len(correctness)), *arrs, corr_iter):
            ret += "| " + " | ".join(
                self._align_value(col, col_len)
                for col, col_len in zip(vals, cols_lens)
            ) + " |\n"
        ret += separator
        return ret

    def _align_value(self, value, max_len: int) -> str:
        if self._array_align == "center":
            return str(value).center(max_len)
        elif self._array_align == "left":
            v = str(value)
            return v + max(max_len - len(v), 0) * " "
        elif self._array_align == "right":
            v = str(value)
            return max(max_len - len(v), 0) * " " + v
        else:
            return str(value)