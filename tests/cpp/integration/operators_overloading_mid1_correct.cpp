#include <iostream>
#include <stdexcept>

class SafeArray {
private:
    size_t size;
    int* data;

public:
    SafeArray(size_t s = 0) : size(s), data(s > 0 ? new int[s]() : nullptr) {}

    SafeArray(const SafeArray& other) : size(other.size), data(new int[size]) {
        for (size_t i = 0; i < size; ++i) data[i] = other.data[i];
    }

    ~SafeArray() { delete[] data; }

    SafeArray& operator=(const SafeArray& other) {
        if (this != &other) {
            delete[] data;
            size = other.size;
            data = new int[size];
            for (size_t i = 0; i < size; ++i) data[i] = other.data[i];
        }
        return *this;
    }

    int& operator[](size_t index) {
        if (index >= size) throw std::out_of_range("Index out of range");
        return data[index];
    }

    const int& operator[](size_t index) const {
        if (index >= size) throw std::out_of_range("Index out of range");
        return data[index];
    }

    SafeArray operator+(const SafeArray& other) const {
        SafeArray result(size + other.size);
        for (size_t i = 0; i < size; ++i) result[i] = data[i];
        for (size_t i = 0; i < other.size; ++i) result[size + i] = other.data[i];
        return result;
    }

    size_t getSize() const { return size; }
};

int main() {
    size_t n;
    std::cin >> n;
    SafeArray a(n), b(n);
    for (size_t i = 0; i < n; ++i) std::cin >> a[i];
    for (size_t i = 0; i < n; ++i) std::cin >> b[i];

    SafeArray copy_a = a;            // deep copy
    if (n > 0) a[0] += 1000;         // mutate only if not empty

    SafeArray sum = a + b;

    std::cout << "SUM: ";
    for (size_t i = 0; i < sum.getSize(); ++i) {
        if (i) std::cout << " ";
        std::cout << sum[i];
    }
    std::cout << "\nCOPY: ";
    for (size_t i = 0; i < copy_a.getSize(); ++i) {
        if (i) std::cout << " ";
        std::cout << copy_a[i];
    }
    std::cout << std::endl;
    return 0;
}