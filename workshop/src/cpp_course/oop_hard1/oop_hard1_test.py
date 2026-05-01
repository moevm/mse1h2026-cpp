import random

from ...base_module import BaseTaskClass, TestItem


class OopHard1Test(BaseTaskClass):
    """OOP -- Hard_Task_1"""

    def __init__(self, seed: int = 42, **kwargs):
        super().__init__(
            compile_name="program",
            seed=seed,
            **kwargs
        )

    def generate_task(self) -> str:
        return """# Задание

Вам необходимо реализовать систему управления библиотекой. Класс `Library` должен хранить книги и предоставлять методы для работы с ними. Используйте `std::vector` для хранения.

**1) Структура `Book`**
- Поля: `std::string title`, `std::string author`, `int year`, `std::string hash`.
- Реализовать оператор `==` для сравнения двух книг по hash.

**2) Класс `Library`**
- Приватное поле: `std::vector<Book> books`.

**3) Метод `addBook(const Book& book)`**
- Добавляет книгу в вектор.
- Перед добавлением проверяет, нет ли уже книги с таким hash. Если есть — выводит сообщение "Book already exists" и не добавляет.

**4) Метод `removeBook(const std::string& hash)`**
- Удаляет книгу с указанным hash из вектора.
- Если книги нет, ничего не делает.

**5) Метод `findBooksByAuthor(const std::string& author)`**
- Возвращает `std::vector<Book>`, содержащий все книги этого автора.

**6) Метод `findBooksByTitle(const std::string& title)`**
- Возвращает `std::vector<Book>`, содержащий все книги с указанным названием.

**7) Метод `printLibrary()`**
- Выводит список всех книг в формате: `Title (Author, Year) - [hash]`.

### Формат ввода
1. Число `N` — количество книг.
2. Далее `N` строк: `title author year hash` (каждое поле без пробелов).
3. Строка для проверки дубля: `title author year hash`.
4. Строка `authorQuery` для поиска по автору.
5. Строка `removeHash` для удаления.
6. Строка `titleQuery` для поиска по названию.

### Формат вывода
1. Сообщение "Book already exists" при попытке добавить дубль.
2. Количество книг автора `authorQuery`.
3. Количество книг с названием `titleQuery` после удаления.
4. Содержимое библиотеки (по одной книге в строке).
"""

    def _generate_tests(self):
        random.seed(self.seed)
        self.tests = []
        tests_count = min(self.tests_num, 5)

        for idx in range(tests_count):
            n = random.randint(3, 5)
            titles = [f"Title{idx}_{i}" for i in range(n)]
            authors = [random.choice(["Ann", "Boris", "Cara", "Dmitry"]) for _ in range(n)]
            years = [random.randint(1990, 2025) for _ in range(n)]
            hashes = [f"h{idx}_{i}" for i in range(n)]

            books = list(zip(titles, authors, years, hashes))
            dup_index = random.randint(0, n - 1)
            dup_book = (
                f"Dup{idx}",
                authors[dup_index],
                years[dup_index] + 1,
                hashes[dup_index],
            )

            author_query = random.choice(authors)
            remove_hash = random.choice(hashes)
            title_query = random.choice(titles)

            remaining_books = [b for b in books if b[3] != remove_hash]
            author_count = sum(1 for _, author, _, _ in books if author == author_query)
            title_count = sum(1 for title, _, _, h in remaining_books if title == title_query)

            output_lines = [
                "Book already exists",
                str(author_count),
                str(title_count),
            ]
            output_lines += [
                f"{title} ({author}, {year}) - [{h}]"
                for title, author, year, h in remaining_books
            ]

            input_lines = [str(n)]
            input_lines += [f"{title} {author} {year} {h}" for title, author, year, h in books]
            input_lines.append(f"{dup_book[0]} {dup_book[1]} {dup_book[2]} {dup_book[3]}")
            input_lines.append(author_query)
            input_lines.append(remove_hash)
            input_lines.append(title_query)

            def make_compare(expected=output_lines):
                def _compare(obt: str, _exp: str) -> bool:
                    lines = [line.strip() for line in obt.strip().splitlines() if line.strip()]
                    return lines == expected

                return _compare

            self.tests.append(TestItem(
                input_str="\n".join(input_lines),
                showed_input=" | ".join(input_lines),
                expected="\n".join(output_lines),
                compare_func=make_compare()
            ))
