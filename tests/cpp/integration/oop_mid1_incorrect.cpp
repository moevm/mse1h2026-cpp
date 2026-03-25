#include <iostream>
#include <string>

class User {
private:
    static int nextId;
    static int usersCount;
    
    const int id;
    std::string username;

public:
    User(const std::string& username) : id(nextId++), username(username) {
        ++usersCount;
    }
    
    static int getUsersCount() {
        return usersCount;
    }
    
    int getId() const {
        return id;
    }
    
    std::string getName() const {
        return username;
    }
    
    void setName(const std::string& newName) {
        username = newName;
    }
};

int User::nextId = 1;
int User::usersCount = 0;


int main() {
    std::cout << User::getUsersCount() << std::endl;
    
    User alice("Alice");
    User bob("Bob");
    User charlie("Charlie");
    
    std::cout << User::getUsersCount() << std::endl;
    
    std::cout << alice.getId() << std::endl;
    std::cout << bob.getId() << std::endl;
    std::cout << charlie.getId() << std::endl;
    
    charlie.setName("Charles");
    
    std::cout << charlie.getName() << std::endl;
    
    {
        User bobCopy("Bob");
        std::cout << User::getUsersCount() << std::endl;
    }
    
    std::cout << User::getUsersCount() << std::endl;
    
    return 0;
}