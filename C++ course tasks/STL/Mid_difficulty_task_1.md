
# Задание

Вам дан класс `PalindromeChecker`, который использует стек для проверки строк на палиндромы. Нужно реализовать его методы, согласно заданию:

**1) Метод `fillNumberStack`**
- Принимает: два целых числа - начало и конец диапазона
- Заполняет `numberStack` числами от `from` до `to` включительно (используйте `push`)
- Предполагается, что `from <= to`
- Ничего не возвращает

**2) Метод `popAllNumbers`**
- Принимает: ничего
- Извлекает все элементы из `numberStack` в порядке LIFO
- Каждый извлеченный элемент добавляет в вектор
- Возвращает `std::vector<int>` с извлеченными числами

**3) Метод `isPalindrome`**
- Принимает: строку для проверки
- Создает локальный стек символов (или использует `charStack` после очистки)
- Помещает все символы строки в стек
- Сравнивает исходную строку с символами, извлеченными из стека
- Возвращает `true`, если строка является палиндромом, иначе `false`
- Метод должен учитывать регистры и пробелы

**4) Метод `isPalindromeIgnoringCaseAndSpaces`**
- Принимает: строку для проверки
- Создает отфильтрованную строку: только буквы, приведенные к нижнему регистру
- Использует тот же алгоритм, что и `isPalindrome`, для отфильтрованной строки
- Возвращает `true`, если строка является палиндромом (игнорируя пробелы и регистр), иначе `false`

**5) Метод `fillCharStack`**
- Принимает: строку для заполнения
- Очищает `charStack` (пока стек не станет пустым)
- Помещает все символы строки в `charStack` в исходном порядке
- Ничего не возвращает

**6) Метод `reverseString`**
- Принимает: ничего (использует текущее состояние `charStack`)
- Извлекает все символы из `charStack` в порядке LIFO
- Составляет из них строку
- Возвращает `std::string` - перевернутую версию исходной строки

```cpp
class PalindromeChecker {
private:
    std::stack<int> numberStack;
    std::stack<char> charStack;
    
public:
    PalindromeChecker() {}
    
    void fillNumberStack(int from, int to);
    
    std::vector<int> popAllNumbers();

    bool isPalindrome(const std::string& str);
    
    bool isPalindromeIgnoringCaseAndSpaces(const std::string& str);
    
    void fillCharStack(const std::string& str);
    
    std::string reverseString();
    
    void printStackInfo() {
        std::cout << "Number stack size: " << numberStack.size() << std::endl;
        std::cout << "Char stack size: " << charStack.size() << std::endl;
    }
};
```
