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

**6) Метод `findBooksByTitle(const std::string& title)`**
- Возвращает `std::vector<Book>`, содержащий все книги с указанным названием.

**7) Метод `printLibrary()`**
- Выводит список всех книг в формате: `Title (Author, Year) - [hash]`.

### Формат ввода
1. `N` — количество книг для добавления.  
2. Далее `N` строк: `title author year hash` (без пробелов внутри полей).  
3. Еще одна строка с книгой для повторного добавления (формат тот же).  
4. Строка с именем автора для поиска.  
5. Строка с названием для поиска.  
6. Строка с hash для удаления.

### Формат вывода
1. Сообщение "Book already exists", если попытка повторного добавления неудачна.  
2. Количество найденных книг по автору.  
3. Количество найденных книг по названию.  
4. Содержимое библиотеки после удаления, по одной книге в строке.
"""

    def _generate_tests(self):
        random.seed(self.seed)
        self.tests = []

        titles = ["Cpp", "Python", "Rust", "Java", "Go"]
        authors = ["A", "B", "C", "D", "E"]

        for _ in range(5):
            n = random.randint(2, 4)
            used_hashes = []
            books = []

            for i in range(n):
                title = random.choice(titles)
                author = random.choice(authors)
                year = random.randint(1990, 2024)
                hash_val = f"h{i}{random.randint(0, 9)}"
                while hash_val in used_hashes:
                    hash_val = f"h{i}{random.randint(0, 9)}"
                used_hashes.append(hash_val)
                books.append({
                    "title": title,
                    "author": author,
                    "year": year,
                    "hash": hash_val,
                })

            duplicate = random.choice(books)
            dup_book = {
                "title": random.choice(titles),
                "author": random.choice(authors),
                "year": random.randint(1990, 2024),
                "hash": duplicate["hash"],
            }

            if random.choice([True, False]):
                author_query = random.choice(authors)
            else:
                author_query = "Unknown"

            if random.choice([True, False]):
                title_query = random.choice(titles)
            else:
                title_query = "UnknownTitle"

            remove_hash = random.choice(used_hashes)

            remaining = [b for b in books if b["hash"] != remove_hash]
            author_count = sum(1 for b in remaining if b["author"] == author_query)
            title_count = sum(1 for b in remaining if b["title"] == title_query)

            expected_lines = [
                "Book already exists",
                str(author_count),
                str(title_count),
            ]
            expected_lines += [
                f"{b['title']} ({b['author']}, {b['year']}) - [{b['hash']}]"
                for b in remaining
            ]
            expected_output = "\n".join(expected_lines)

            input_lines = [str(n)]
            input_lines += [
                f"{b['title']} {b['author']} {b['year']} {b['hash']}"
                for b in books
            ]
            input_lines.append(
                f"{dup_book['title']} {dup_book['author']} {dup_book['year']} {dup_book['hash']}"
            )
            input_lines.append(author_query)
            input_lines.append(title_query)
            input_lines.append(remove_hash)

            def make_compare(expected):
                def _compare(obt, _exp):
                    lines = [line.strip() for line in obt.strip().splitlines() if line.strip()]
                    if len(lines) != len(expected):
                        return False
                    return all(o == e for o, e in zip(lines, expected))

                return _compare

            self.tests.append(TestItem(
                input_str="\n".join(input_lines),
                showed_input="\n".join(input_lines),
                expected=expected_output,
                compare_func=make_compare(expected_lines)
            ))
