Идея 3: Менеджер распределенных задач (Distributed Task Manager)
Суть проекта: Система для постановки, выполнения и отслеживания статуса задач в "пуле потоков" (эмулируем).

Структура и требования:

1. ООП:
Базовый класс Task теперь шаблонный по возвращаемому типу или использует CRTP (Curiously Recurring Template Pattern) для типобезопасности.
Но чтобы хранить разные задачи в одном контейнере, нужен общий базовый класс TaskBase.
execute() теперь возвращает void, но заполняет внутренний Result<T>.

2. Управление ресурсами (RAII):
Класс TaskManager хранит std::vector<std::unique_ptr<TaskBase>> — полное владение задачами.
std::shared_ptr не очень нужен, так как задачи выполняются синхронно в эмуляции. Но если хотим показать shared_ptr, можно сделать пул потоков, где задачи расшариваются.

3. Шаблоны:
Класс Result<T> содержит std::optional<T> m_value и std::exception_ptr m_exception.
Методы: bool hasValue(), bool hasException(), T getValue(), void setValue(T value), void setException(...).
Шаблонный метод у менеджера для получения результата по типу: getResult<T>(int taskId).

4. STL и алгоритмы + Лямбды:
Контейнеры: std::deque<std::unique_ptr<TaskBase>> очередь задач; std::map<int, std::any> для хранения результатов (или лучше std::map<int, std::shared_ptr<void>> с type_info).
Алгоритмы:
std::remove_if + лямбда для удаления выполненных задач.
std::sort + лямбда для сортировки по приоритету.
std::find_if + лямбда для поиска задачи по имени.

5. Перегрузка операторов:
() для задач (функторы) — можно вызвать задачу как функцию: CalcTask(5, 3)().
<< для вывода статуса задачи: std::cout << task.
<< для вывода результата: std::cout << result (выводит значение или "ошибка").

6. Исключения:
TaskFailedException — если задача бросила исключение.
InvalidResultAccessException — если пытаются получить значение из Result, а там исключение.
TaskNotFoundException — если запрашивают результат несуществующей задачи.

7. Конкретные типы задач:
CalcTask : public Task<int> — вычисляет число (например, факториал, сумму).
IOTask : public Task<std::string> — читает данные (симулирует чтение файла, возвращает строку).
DelayTask : public Task<bool> — просто ждет и возвращает true, когда ожидание завершено.
NetworkTask : public Task<std::vector<char>> — получает данные по сети.
FileTask : public Task<size_t> — записывает файл и возвращает размер записанных данных.



Генерация вариантов (по хешу):
Типы задач: Реализовать 3 конкретных типа из списка: [CalcTask, IOTask, DelayTask, NetworkTask, FileTask].
Контейнер: std::vector или std::deque для очереди.
Сортировка: По приоритету или по времени создания.
