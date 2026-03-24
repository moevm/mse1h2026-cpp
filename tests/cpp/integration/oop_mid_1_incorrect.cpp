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

