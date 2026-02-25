
# Задание:

Вам необходимо реализовать класс `Graph`, представляющий неориентированный граф. Вершины графа хранятся с использованием `std::shared_ptr`. Для хранения смежности используются `std::weak_ptr`, чтобы избежать циклических ссылок. Заготовка класса и структуры вершин даны, вы должны написать методы.

**1) Метод `addVertex(int id, const std::string& data = "")`**
- Принимает: уникальный идентификатор вершины и опциональные данные
- Создает новую вершину через `std::make_shared<Vertex>(id, data)`
- Добавляет вершину в вектор `vertices`
- Если вершина с таким `id` уже существует, выбрасывает исключение `std::invalid_argument` с сообщением "Vertex with this ID already exists"
- Возвращает `std::shared_ptr<Vertex>` на созданную вершину

**2) Метод `removeVertex(int id)`**
- Принимает: идентификатор удаляемой вершины
- Находит вершину по `id` и удаляет её из вектора `vertices`
- Проходит по всем оставшимся вершинам и удаляет `weak_ptr` на удаляемую вершину из их cписков соседей
- Если вершина не найдена, выбрасывает исключение `std::invalid_argument` с сообщением "Vertex not found"
- Ничего не возвращает

**3) Метод `addEdge(int id1, int id2)`**
- Принимает: идентификаторы двух вершин, между которыми создается ребро
- Находит обе вершины через `getVertex`
- Если одна из вершин не найдена, выбрасывает исключение `std::invalid_argument` с сообщением "One or both vertices not found"
- Проверяет, существует ли уже ребро между ними (чтобы не добавлять дубликат)
- Добавляет в список соседей первой вершины `weak_ptr` на вторую
- Добавляет в список соседей второй вершины `weak_ptr` на первую
- Ничего не возвращает

**4) Метод `removeEdge(int id1, int id2)`**
- Принимает: идентификаторы двух вершин, между которыми удаляется ребро
- Находит обе вершины через `getVertex`
- Если одна из вершин не найдена, выбрасывает исключение `std::invalid_argument` с сообщением "Vertex not found"
- Удаляет `weak_ptr` на вторую вершину из списка соседей первой
- Удаляет `weak_ptr` на первую вершину из списка соседей второй
- Если ребра не существовало, ничего не делает
- Ничего не возвращает

**5) Метод `getVertex(int id) const`**
- Принимает: идентификатор вершины
- Ищет вершину с указанным `id` в векторе `vertices`
- Возвращает `std::shared_ptr<Vertex>` на найденную вершину
- Если вершина не найдена, возвращает `nullptr`

**6) Метод `hasVertex(int id) const`**
- Принимает: идентификатор вершины
- Возвращает `true`, если вершина с таким `id` существует, иначе `false`

**7) Метод `hasEdge(int id1, int id2) const`**
- Принимает: идентификаторы двух вершин
- Находит обе вершины через `getVertex`
- Если одна из вершин не найдена, возвращает `false`
- Проверяет, есть ли во второй вершине `weak_ptr` на первую
- Возвращает `true`, если ребро существует, иначе `false`

**8) Метод `vertexCount() const`**
- Возвращает количество вершин в графе (размер вектора `vertices`)

**9) Метод `edgeCount() const`**
- Подсчитывает количество ребер в графе
- Проходит по всем вершинам и суммирует размеры списков соседей, затем делит на 2
- Возвращает `size_t` - количество ребер


**Вершина:**
```cpp
struct Vertex {
    int id;
    std::string data;
    std::vector<std::weak_ptr<Vertex>> neighbors;
    Vertex(int id, const std::string& data = "") : id(id), data(data) {}
};
```

**Класс:**
```cpp
class Graph {
private:
    std::vector<std::shared_ptr<Vertex>> vertices;
    
public:
    Graph() = default;
    
    std::shared_ptr<Vertex> addVertex(int id, const std::string& data = "");
    
    void removeVertex(int id);
    
    void addEdge(int id1, int id2);
    
    void removeEdge(int id1, int id2);
    
    std::shared_ptr<Vertex> getVertex(int id) const;
    
    bool hasVertex(int id) const;
    
    bool hasEdge(int id1, int id2) const;
    
    size_t vertexCount() const;
    
    size_t edgeCount() const;
    
};
```
