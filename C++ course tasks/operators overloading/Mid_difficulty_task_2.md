
# Задание

Дан класс `Fraction` для работы с обыкновенными дробями. Дробь хранится в виде числителя и знаменателя, всегда сокращенной. Класс уже содержит конструктор, метод сокращения и метод вывода.
Вам необходимо дописать класс `Fraction`, добавив в него перегрузку операторов:

1. **Арифметические операторы:** `+`, `-`, `*`, `/` - для выполнения соответствующих операций с дробями. (возвращает новый объект класса)
2. **Операторы сравнения:** `==`, `!=`, `<`, `>`, `<=`, `>=` - для сравнения дробей. (возвращает true и false)
3. **Оператор преобразования в `double`** - для преобразования дроби в число с плавающей точкой.

## Исходный код

```cpp
#include <iostream>

class Fraction {
private:
    int numerator;
    int denominator;
    
    // Сокращение дроби
    void reduce() {
        if (denominator < 0) {
            numerator = -numerator;
            denominator = -denominator;
        }
        int gcd = std::gcd(abs(numerator), denominator);
        numerator /= gcd;
        denominator /= gcd;
    }
    
public:
    Fraction(int num = 0, int den = 1) : numerator(num), denominator(den) {
        if (den == 0) {
            throw std::invalid_argument("Знаменатель не может быть нулем");
        }
        reduce();
    }
    
    void print() const {
        std::cout << numerator;
        if (denominator != 1) {
            std::cout << "/" << denominator;
        }
    }
    
    // 1. Арифметические операторы: +, -, *, /
    
    // 2. Операторы сравнения: ==, !=, <, >, <=, >=
    
    // 3. Оператор преобразования в double
};

