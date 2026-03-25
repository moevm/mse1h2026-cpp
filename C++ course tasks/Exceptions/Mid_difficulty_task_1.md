
# Задание

Вам дан класс `Library`, который представляет систему управления библиотекой. Класс `Library` уже реализован, но в нем отсутствует проверка на некорректные операции. Вам нужно модифицировать класс, добавив выбрасывание исключений в следующих ситуациях:

1. **Попытка взять книгу, которой нет в библиотеке**
2. **Попытка взять книгу, которая уже выдана**
3. **Попытка вернуть книгу, которая не была выдана**
4. **Попытка добавить книгу с пустым названием или автором**
5. **Попытка удалить книгу, которой нет в библиотеке**

После добавления исключений в класс, вам нужно обработать их в функции `main()` с помощью `try-catch` блоков, чтобы программа не завершалась аварийно.

```cpp
struct Book {
    std::string title;
    std::string author;
    bool isIssued;
    
    Book(const std::string& t, const std::string& a) 
        : title(t), author(a), isIssued(false) {}
};

class Library {
private:
    std::vector<Book> books;
    
public:
    void addBook(const std::string& title, const std::string& author) {
        books.push_back(Book(title, author));
    }
    
    void removeBook(const std::string& title, const std::string& author) {
        auto it = std::find_if(books.begin(), books.end(),
            [&](const Book& b) { return b.title == title && b.author == author; });
        if (it != books.end()) {
            books.erase(it);
        }
    }
    
    void issueBook(const std::string& title, const std::string& author) {
        auto it = std::find_if(books.begin(), books.end(),
            [&](const Book& b) { return b.title == title && b.author == author; });
        
        if (it != books.end() && !it->isIssued) {
            it->isIssued = true;
        }
    }
    
    void returnBook(const std::string& title, const std::string& author) {
        auto it = std::find_if(books.begin(), books.end(),
            [&](const Book& b) { return b.title == title && b.author == author; });
        
        if (it != books.end() && it->isIssued) {
            it->isIssued = false;
        }
    }

    std::vector<Book> findBooksByTitle(const std::string& title) const {
        std::vector<Book> result;
        std::copy_if(books.begin(), books.end(), std::back_inserter(result),
            [&](const Book& b) { return b.title == title; });
        return result;
    }
    
    std::vector<Book> findBooksByAuthor(const std::string& author) const {
        std::vector<Book> result;
        std::copy_if(books.begin(), books.end(), std::back_inserter(result),
            [&](const Book& b) { return b.author == author; });
        return result;
    }
    
    std::vector<Book> getAllBooks() const {
        return books;
    }
    
    std::vector<Book> getAvailableBooks() const {
        std::vector<Book> result;
        std::copy_if(books.begin(), books.end(), std::back_inserter(result),
            [](const Book& b) { return !b.isIssued; });
        return result;
    }
    
    std::vector<Book> getIssuedBooks() const {
        std::vector<Book> result;
        std::copy_if(books.begin(), books.end(), std::back_inserter(result),
            [](const Book& b) { return b.isIssued; });
        return result;
    }
};

int main() {
    Library lib;
    
    lib.addBook("Война и мир", "Лев Толстой");
    lib.addBook("Преступление и наказание", "Федор Достоевский");
    lib.addBook("Мастер и Маргарита", "Михаил Булгаков");
    
    lib.issueBook("Война и мир", "Лев Толстой");
    
    lib.addBook("", "Александр Пушкин");
    
    lib.issueBook("Евгений Онегин", "Александр Пушкин");
    
    lib.issueBook("Война и мир", "Лев Толстой");
    
    lib.returnBook("Преступление и наказание", "Федор Достоевский");
    
    lib.removeBook("Анна Каренина", "Лев Толстой");
    
    return 0;
}
```

