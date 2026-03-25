from ...base_module import BaseTaskClass, TestItem


class OopMid1Test(BaseTaskClass):
    """OOP -- Mid_Task_1"""

    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(
            compile_name="program",
            seed=seed,
            **kwargs
        )

    def generate_task(self) -> str:
        return (
            "Реализуйте класс User для системы регистрации, который автоматически присваивает уникальные ID "
            "каждому новому пользователю и подсчитывает их общее количество, используя статические члены.\n\n"
            "1) Приватные статические поля\n"
            "- static int nextId - хранит ID для следующего пользователя (изначально 1).\n"
            "- static int usersCount - хранит текущее количество активных пользователей.\n\n"
            "2) Поля объекта\n"
            "- const int id - уникальный номер (задается в конструкторе и не меняется).\n"
            "- std::string username.\n\n"
            "3) Конструктор\n"
            "- Принимает имя пользователя.\n"
            "- Присваивает полю id значение nextId.\n"
            "- Инкрементирует nextId.\n"
            "- Инкрементирует usersCount.\n\n"
            "4) Деструктор\n"
            "- Декрементирует usersCount (уменьшает счетчик активных пользователей при удалении объекта).\n\n"
            "5) Статический метод getUsersCount()\n"
            "- Возвращает текущее количество пользователей.\n\n"
            "6) Методы доступа\n"
            "- getId() - возвращает ID.\n"
            "- getName() - возвращает имя.\n\n"
            "7) Методы изменения\n"
            "- setName(const std::string& newName) — устанавливает новое имя пользователя."
        )

    def _generate_tests(self):
        self.tests = [
            TestItem(
                input_str="",
                showed_input="no input",
                expected="0\n3\n1\n2\n3\nCharles\n4\n3",
                compare_func=lambda x, y: x.strip() == y.strip()
            )
        ]