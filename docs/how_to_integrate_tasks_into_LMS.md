# Как интегрировать задания в LMS Moodle?
<br>  

[**e.moevm.info**](https://e.moevm.info) → **Мои курсы** → **mse-16-cpp/mse-17-prog1**
<br>  

Далее ищем нужный раздел и блок заданий в нем (при необходимости создаем ручками). Чтобы добавить задание, идем в Банк вопросов, нажимаем на создание нового вопроса и выбираем CodeRunner. Если необходимо посмотреть готовые задания банка НАШИХ блоков, выбираем соответствие с `test`.  

Ниже описано то, как следует заполнять поля нового задания:  
<br>  

**Тип вопроса** (выбираем по ситуации):  `c++_via_python_stepik` | `c_via_python_stepik`

**Настройка**: ставим галочку рядом с "настроить"
<br>  

**Параметры шаблона**  
Тут происходит препроцессинг. Выполняются все действия, которые необходимы ДО непосредственной проверки задания: получение сида и текста задания. Текст и сид попадают в текущую среду проверки, далее получить их можно с помощью `{{ task_text | e('py') }}` и `{{ task_seed | e('py') }}`. Реализуем препроцессинг по аналогии:
```python
# Клонирование репо и добавление воркшопа в пути (удалить после обновления кодранера)
from pathlib import Path
import subprocess
import sys

repo_path = Path("/tmp/mse1h2026-cpp")
if not repo_path.exists():
    command = ["git", "clone", "--depth=1", "https://github.com/moevm/mse1h2026-cpp.git", str(repo_path)]
    subprocess.run(command, capture_output=True)
sys.path.insert(0, str(repo_path)) 
sys.path.insert(0, str(repo_path / "workshop"))

# Препроцессинг (получение текста задания и сида)
import json
import sys
from workshop.src.cpp_course.lambda_easy1 import LambdaEasy1Test

# user_id = int(sys.argv[2]).split("=")[1]   
user_id = 42  # Для отладки

seed = ((((user_id ** 2) << 10) * 43) >> 5)

lab_checker = LambdaEasy1Test(
    seed=seed,
    solution=None, 
    fail_on_first_test=True
)

task_text = lab_checker.generate_task()
data = {
    "task_text": task_text,
    "task_seed": seed,
}

print(json.dumps(data))
```
<br>  

### Элементы управления параметрами шаблона
ставим галочку "Наблюдать все", выбираем препроцессор Python

### Настройка
Это обертка над проверкой через наш воркшоп. Тут прогоняются тесты и возвращается вердикт: OK или не OK. Шаблон (реализуем по аналогии):  
```python
# Клонирование репо и добавление воркшопа в пути (удалить после обновления кодранера)
from pathlib import Path
import subprocess
import sys

repo_path = Path("/tmp/mse1h2026-cpp")
if not repo_path.exists():
    command = ["git", "clone", "--depth=1", "https://github.com/moevm/mse1h2026-cpp.git", str(repo_path)]
    subprocess.run(command, capture_output=True)
sys.path.insert(0, str(repo_path)) 
sys.path.insert(0, str(repo_path / "workshop"))



"""
Кастомная (костыльная) логика проверки задания с сидом
Все тесты прошли => print OK, иначе Wrong answer с инфой об ошибке

Пайплайн проверки не совсем стандартный!
Все тесты проводятся воркшопом внутри ОДНОГО тесткейса мудла,
тесткейс мудла ожидает ОК (или не ОК) от данного блока кода
"""

from pathlib import Path
from workshop.src.cpp_course import LambdaEasy1Test

task_seed_str = """{{ task_seed | e('py') }}"""
task_seed = int(task_seed_str.strip()) if task_seed_str.strip() else 42

student_code = """{{ STUDENT_ANSWER | e('c') }}"""
student_code = student_code.strip()

# Сохраняем решение в solution.cpp
solution_file = "solution.cpp"
Path(solution_file).write_text(student_code)

# Создаем проверяльщик
lab_checker = LambdaEasy1Test(
    seed=task_seed,
    solution=solution_file,  
    fail_on_first_test=True,
    jail_path=str(Path.cwd())  # Текущая директория как jail
)

# Запускаем проверку
try:
    passed, msg = lab_checker.check()
except Exception as e:
    passed, msg = False, f'Непредвиденная ошибка при проверке: {str(e)}'

# Выводим результат
if passed:
    print('OK')
else:
    print(f'Wrong answer\n{msg}')
```

<br>  

### Общее
Название вопроса: (вписываем название)    
Текст вопроса: советую перекопировать и отформатировать текст ручками, тк автоматизированное получение текста из кода не сохраняет md форматирование  

Пример того как можно получить текст и сид из препроцессинга:
```
Текст вашего задания:
{{ task_text | e('py') }}

Сид вашего задания: {{ task_seed | e('py') }}
```

<br>  

### Расширенная настройка
Язык ace (C++ по умолчанию - некорректное название, подсветка не работает): `c_cpp` 

<br>  

### Тестовые примеры
Создаем ОДИН тесткейс. Все тесткейсы воркшопа будут прогнаны в рамках одного тесткейса мудла. Проверка из настроек шаблона вернет **OK** или **Wrong answer**, тесткейс мудла это увидит и обработает  
```
Тестовый пример 1: 1  
Стандартный ввод: 1  
Ожидаемый результат:  OK
```
