#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

struct Book {
    std::string title;
    std::string author;
    int year;
    std::string hash;

    bool operator==(const Book& other) const { return title == other.title; }
};

class Library {
private:
    std::vector<Book> books;

public:
    void addBook(const Book& book) { books.push_back(book); }

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
    Library library;
    library.addBook({"Cpp", "A", 2001, "h1"});
    library.addBook({"Algo", "A", 2005, "h2"});
    library.addBook({"Dup", "A", 2020, "h1"});

    std::cout << library.findBooksByAuthor("A").size() << "\n";
    library.removeBook("h2");
    std::cout << library.findBooksByTitle("Algo").size() << "\n";
    library.printLibrary();
}
