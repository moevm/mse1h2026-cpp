# Задание

Напишите составной концепт `ToStringable`, который проверяет наличие метода `.toString()`, возвращающего `std::string`.

**1) Концепт `ToStringable<T>`**
- Используйте `requires(const T& v) { ... }`.
- Проверьте наличие метода `v.toString()`.
- Проверьте, что возвращаемый тип — `std::string` (используйте `{ expression } -> std::same_as<std::string>`).

**2) Класс `Logger`**
- Имеет метод `log(const T& obj)`.
- Метод ограничен концептом `ToStringable`.
- Выводит результат `obj.toString()`.

```cpp
// concept ToStringable 

class Logger {
public:
    void log(const auto& obj) { 
    
    }
};