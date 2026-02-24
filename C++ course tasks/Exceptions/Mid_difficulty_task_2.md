
# Задание

Вам дан класс `SafeStack`, который представляет стек с ограниченным размером. 
Класс `SafeStack` уже реализован, но в нем отсутствует проверка на некорректные операции. Вам нужно модифицировать класс, добавив выбрасывание исключений в следующих ситуациях:

1. **Попытка извлечь элемент из пустого стека (`pop`)**
2. **Попытка получить верхний элемент пустого стека (`top`)**
3. **Попытка добавить элемент в полный стек (`push`)**
4. **Создание стека с некорректным размером (отрицательный или ноль)**
5. **Попытка получить элемент по индексу за пределами стека**

После добавления исключений в класс, вам нужно обработать их в функции `main()` с помощью `try-catch` блоков, чтобы программа не завершалась аварийно.

```cpp
class SafeStack {
private:
    std::vector<int> data;
    size_t maxSize;
    
public:
    SafeStack(size_t size) : maxSize(size) {
    }
    
    void push(int value) {
        data.push_back(value);
    }
    
    void pop() {
        data.pop_back();
    }
    
    int top() const {
        return data.back();
    }
    
    bool isEmpty() const {
        return data.empty();
    }
    
    bool isFull() const {
        return data.size() >= maxSize;
    }
    
    size_t size() const {
        return data.size();
    }
    
    size_t capacity() const {
        return maxSize;
    }
    
    int at(size_t index) const {
        return data[index];
    }
    
    void clear() {
        data.clear();
    }
};

int main() {
    SafeStack stack(3);

    stack.push(10);
    stack.push(20);
    stack.push(30);
    
    stack.pop();
    
    SafeStack badStack(0);
    
    stack.push(40);
    stack.push(50); // Здесь стек уже полный
    
    SafeStack emptyStack(3);
    emptyStack.pop();
    
    std::cout << emptyStack.top() << std::endl;
    
    std::cout << stack.at(5) << std::endl;
    
    return 0;
}
```
