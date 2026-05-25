#include <iostream>
#include <stdexcept>

class SafeArray {
private:
    size_t size;
    int* data;

public:
    SafeArray(size_t s = 0) : size(s), data(s ? new int[s]() : nullptr) {}
    SafeArray(const SafeArray& other) : size(other.size), data(other.data) {} // shallow (WRONG)
    ~SafeArray() { delete[] data; }

    SafeArray& operator=(const SafeArray& other) {
        if (this != &other) {
            delete[] data;
            size = other.size;
            data = other.data;   // shallow (WRONG)
        }
        return *this;
    }

    int& operator[](size_t i) { return data[i]; }               // no bounds check
    const int& operator[](size_t i) const { return data[i]; }

    SafeArray operator+(const SafeArray& other) const {
        SafeArray res(size);   // wrong size
        for (size_t i = 0; i < size; ++i)
            res[i] = data[i] + other.data[i];   // element-wise (WRONG)
        return res;
    }

    size_t getSize() const { return size; }
};

int main() {
    size_t n;
    std::cin >> n;
    SafeArray a(n), b(n);
    for (size_t i = 0; i < n; ++i) std::cin >> a[i];
    for (size_t i = 0; i < n; ++i) std::cin >> b[i];

    SafeArray copy_a = a;
    a[0] += 1000;
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