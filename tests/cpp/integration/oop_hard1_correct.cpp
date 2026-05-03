#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

struct Book {
    std::string title;
    std::string author;
    int year;
    std::string hash;

    bool operator==(const Book& other) const { return hash == other.hash; }
};

class Library {
private:
    std::vector<Book> books;

public:
    void addBook(const Book& book) {
        auto it = std::find_if(books.begin(), books.end(), [&book](const Book& b) { return b == book; });
        if (it != books.end()) {
            std::cout << "Book already exists\n";
            return;
        }
        books.push_back(book);
    }

    void removeBook(const std::string& hash) {
        books.erase(
            std::remove_if(books.begin(), books.end(), [&hash](const Book& b) { return b.hash == hash; }),
            books.end());
    }

    std::vector<Book> findBooksByAuthor(const std::string& author) const {
        std::vector<Book> result;
        for (const auto& b : books) {
            if (b.author == author) {
                result.push_back(b);
            }
        }
        return result;
    }

    std::vector<Book> findBooksByTitle(const std::string& title) const {
        std::vector<Book> result;
        for (const auto& b : books) {
            if (b.title == title) {
                result.push_back(b);
            }
        }
        return result;
    }

    void printLibrary() const {
        for (const auto& b : books) {
            std::cout << b.title << " (" << b.author << ", " << b.year << ") - [" << b.hash << "]\n";
        }
    }
};

int main() {
    int n = 0;
    if (!(std::cin >> n)) {
        return 0;
    }

    Library library;
    for (int i = 0; i < n; ++i) {
        Book book;
        std::cin >> book.title >> book.author >> book.year >> book.hash;
        library.addBook(book);
    }

    Book duplicate;
    std::cin >> duplicate.title >> duplicate.author >> duplicate.year >> duplicate.hash;
    library.addBook(duplicate);

    std::string authorQuery;
    std::string titleQuery;
    std::string removeHash;
    std::cin >> authorQuery >> titleQuery >> removeHash;

    library.removeBook(removeHash);

    std::cout << library.findBooksByAuthor(authorQuery).size() << "\n";
    std::cout << library.findBooksByTitle(titleQuery).size() << "\n";
    library.printLibrary();
}
