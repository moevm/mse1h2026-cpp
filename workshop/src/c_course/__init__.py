from .base_module.base_task import BaseTaskClass
from .base_module.base_cli import CLIParser, add_common_cli_args, get_common_cli_args

# Ручной импорт лабораторных работ
from .lab1_hello import Lab1HelloTest, lab1_parser

# Собираем все парсеры в список для удобства
PARSERS = [
    lab1_parser,
    # Добавляйте новые парсеры сюда
]

# Экспортируем все
__all__ = [
    'BaseTaskClass',
    'CLIParser',
    'add_common_cli_args',
    'get_common_cli_args',
    'Lab1HelloTest',
    'lab1_parser',
    'PARSERS'
]