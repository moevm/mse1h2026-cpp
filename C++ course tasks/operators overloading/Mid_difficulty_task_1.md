
# Задание

Дан класс `SafeArray`, который реализует динамический массив целых чисел с проверкой выхода за границы. Класс уже содержит конструкторы, деструктор и вспомогательные методы.
Вам необходимо дописать класс `SafeArray`, добавив в него перегрузку пяти операторов:

1. **Оператор `[]`** - для доступа к элементам массива. Должен проверять выход за границы и выбрасывать исключение `std::out_of_range`.
2. **Оператор `=`** - для копирования массивов (глубокое копирование).
3. **Оператор `+`** - для склеивания двух массивов.
4. **Оператор `()`** - для изменения размера массива (принимает новый размер).

## Код:

```cpp
#include <iostream>

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
        for (size_t i = 0; i < size; i++) {
            data[i] = other.data[i];
        }
    }
    
    ~SafeArray() {
        delete[] data;
    }
    
    // Метод для получения размера
    size_t getSize() const { return size; }
    
    // 1. operator[] (доступ)
    
    // 2. operator= (присваивание)
    
    // 3. operator+ (конкатенация)
    
    // 4. operator() (изменение размера)
};
