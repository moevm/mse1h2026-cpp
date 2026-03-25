#include <iostream>

class SafeArray {
private:
    int* data;
    size_t size;

public:
    SafeArray(size_t s = 0) : size(s) {
        data = (size > 0) ? new int[size]() : nullptr;
    }

    ~SafeArray() {
        delete[] data;
    }

    size_t getSize() const { return size; } 
    int& operator[](size_t index) {
        return data[index];
    }

    SafeArray operator+(const SafeArray& other) const {
        return SafeArray(size); 
    }

    void operator()(size_t newSize) {
        size = newSize; 
    }
};

int main() {
    SafeArray a(2);
    SafeArray b(2);

    SafeArray c = a + b;

    if (c.getSize() != 4) return 1; 

    return 0;
}