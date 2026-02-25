# Задание

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

