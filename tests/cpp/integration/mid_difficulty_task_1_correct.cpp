#include <iostream>
#include <stdexcept>

class SafeArray {
private:
    int* data;
    size_t size;

public:
    SafeArray(size_t s = 0) : size(s) {
        data = (size > 0) ? new int[size]() : nullptr;
    }

    SafeArray(const SafeArray& other) : size(other.size) {
        data = new int[size];
        for (size_t i = 0; i < size; i++)
            data[i] = other.data[i];
    }

    ~SafeArray() {
        delete[] data;
    }

    size_t getSize() const { return size; }

    int& operator[](size_t index) {
        if (index >= size)
            throw std::out_of_range("out of range");
        return data[index];
    }

    SafeArray& operator=(const SafeArray& other) {
        if (this == &other) return *this;

        delete[] data;
        size = other.size;
        data = new int[size];

        for (size_t i = 0; i < size; i++)
            data[i] = other.data[i];

        return *this;
    }

    SafeArray operator+(const SafeArray& other) const {
        SafeArray res(size + other.size);

        for (size_t i = 0; i < size; i++)
            res.data[i] = data[i];

        for (size_t i = 0; i < other.size; i++)
            res.data[size + i] = other.data[i];

        return res;
    }

    void operator()(size_t newSize) {
        int* newData = new int[newSize]();

        size_t minSize = (newSize < size) ? newSize : size;

        for (size_t i = 0; i < minSize; i++)
            newData[i] = data[i];

        delete[] data;
        data = newData;
        size = newSize;
    }
};

int main() {
    SafeArray a(2);
    a[0] = 1; a[1] = 2;

    SafeArray b(2);
    b[0] = 3; b[1] = 4;

    SafeArray c = a + b;

    if (c.getSize() != 4) return 1;
    if (c[0] != 1 || c[3] != 4) return 1;

    return 0;
}