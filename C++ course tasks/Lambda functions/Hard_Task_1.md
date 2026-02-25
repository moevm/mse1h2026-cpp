
# Задание

Вам нужно реализовать класс `CurrencyConverter`, который позволяет конвертировать суммы между различными валютами.
Класс хранит курсы валют относительно базовой валюты и содержит методы, которые вы должны реализовать с использованием лямбда выражений.

**1) Конструктор `CurrencyConverter(const std::string& base)`**
- Принимает: строку с названием базовой валюты (например, "USD")
- Сохраняет базовую валюту в поле `baseCurrency`
- Добавляет в словарь `exchangeRates` запись: ключ = базовая валюта, значение = 1.0
- Ничего не возвращает (конструктор)

**2) Метод `addRate(const std::string& currency, double rate)`**
- Принимает:
    - `currency` - строку с названием валюты
    - `rate` - курс относительно базовой валюты
- Добавляет в словарь `exchangeRates` запись: ключ = валюта, значение = курс
- Ничего не возвращает (`void`)

**3) Метод `convert(double amount, const std::string& from, const std::string& to) const`**
- Принимает:
    - `amount` - сумму для конвертации
    - `from` - исходная валюта
    - `to` - целевая валюта
- Проверяет наличие обеих валют в словаре `exchangeRates`. Если хотя бы одной нет - выбрасывает исключение `std::runtime_error` с сообщением "Currency not found"
- Создает лямбда-выражение, которое вычисляет коэффициент конвертации: `rateTo / rateFrom`
- Лямбда должна захватывать необходимые переменные
- Применяет эту лямбду к переданной сумме
- Возвращает `double` - результат конвертации

**4) Метод `convertMany(const std::vector<double>& amounts, const std::string& from, const std::string& to) const`**
- Принимает:
    - `amounts` - вектор сумм для конвертации
    - `from` - исходная валюта
    - `to` - целевая валюта
- Проверяет наличие обеих валют в словаре (можно вызвать `convert` для одной суммы или проверить отдельно)
- **Создает лямбда-выражение-конвертер**, которое принимает одну сумму и возвращает результат её конвертации
- В цикле применяет эту лямбду к каждому элементу входного вектора
- Сохраняет результаты в новый вектор
- Возвращает `std::vector<double>` - вектор с конвертированными суммами

**5) Метод `convertFiltered(const std::vector<double>& amounts, const std::string& from, const std::string& to, bool (*predicate)(double)) const`**
- Принимает:
    - `amounts` - вектор сумм для конвертации
    - `from` - исходная валюта
    - `to` - целевая валюта
    - `predicate` - указатель на функцию-предикат, которая принимает `double` и возвращает `bool`
- Проверяет наличие обеих валют в словаре
- **Создает лямбда-выражение-конвертер**, аналогично методу `convertMany`
- В цикле проходит по всем суммам:
    - Применяет к каждой сумме переданный предикат
    - Если предикат возвращает `true` - конвертирует сумму с помощью лямбды-конвертера и добавляет результат в результирующий вектор
    - Если `false` - пропускает сумму
- Возвращает `std::vector<double>` - вектор с конвертированными суммами только для тех исходных сумм, которые удовлетворяют предикату

**7) Метод `printRates() const`**
- Принимает: ничего
- Выводит в консоль все доступные курсы валют в формате:
    Base currency: USD
    EUR: 0.85
    GBP: 0.75
    JPY: 110
    RUB: 75
- Порядок валют может быть любым
- Ничего не возвращает (`void`)

```cpp
class CurrencyConverter {
private:
    std::string baseCurrency;
    std::map<std::string, double> exchangeRates;
    
public:
    CurrencyConverter(const std::string& base);
    
    void addRate(const std::string& currency, double rate);
    
    double convert(double amount, const std::string& from, const std::string& to) const;
    
    std::vector<double> convertMany(const std::vector<double>& amounts, 
                                    const std::string& from, 
                                    const std::string& to) const;
    
    std::vector<double> convertFiltered(const std::vector<double>& amounts,
                                        const std::string& from,
                                        const std::string& to,
                                        bool (*predicate)(double)) const;
    
    void printRates() const;
};
```
