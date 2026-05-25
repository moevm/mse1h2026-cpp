from ...base_module import BaseTaskClass, TestItem


class StlEasy1Test(BaseTaskClass):
    """STL Easy 1 — функция printVectorInfo для вектора"""

    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(
            compile_name="program",
            seed=seed,
            **kwargs
        )

    def generate_task(self) -> str:
        return (
            "Напишите функцию `printVectorInfo`, которая принимает вектор и выводит информацию о нем: его размер, выделенную память и проверку на пустоту.\n\n"
            "**Функция `printVectorInfo`**\n"
            "- Принимает: `const std::vector<int>& vec` (константная ссылка на вектор целых чисел)\n"
            "- Выводит три строки:\n"
            "    - `\"Size: \"` + значение `vec.size()`\n"
            "    - `\"Capacity: \"` + значение `vec.capacity()`\n"
            "    - `\"Empty: \"` + `\"yes\"`, если вектор пуст, или `\"no\"`, если не пуст\n"
            "- Пример вывода:\n"
            "```\n"
            "Size: 3\n"
            "Capacity: 3\n"
            "Empty: no\n"
            "```\n"
            "- Ничего не возвращает (`void`)\n\n"
            "В `main` проверьте работу на пустом векторе и векторе из 5 целых чисел (например, 1,2,3,4,5)."
        )

    def _generate_tests(self):
        self.tests = [
            TestItem(
                input_str="",
                showed_input="no input",
                expected="Size: 0\nCapacity: 0\nEmpty: yes\nSize: 5\nCapacity: 5\nEmpty: no",
                compare_func=lambda x, y: x.strip() == y.strip()
            )
        ]
