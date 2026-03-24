from ...c_course.base_module.base_cli import add_common_cli_args, get_common_cli_args, CLIParser
from .concepts_easy1_test import ConceptsEasy1Test

def add_cli_args_concepts_easy1(parser):
    """Добавляет аргументы для первого задания"""
    # Сначала добавляем общие аргументы
    add_common_cli_args(parser)

    # Устанавливаем функцию создания задания
    parser.set_defaults(func=create_task_concepts_easy1)


def create_task_concepts_easy1(args):
    """Создает задание из аргументов командной строки"""
    common_args = get_common_cli_args(args)
    return ConceptsEasy1Test(
        **common_args,
    )


concepts_easy1_parser = CLIParser(
    name='concepts_easy1',
    add_cli_args=add_cli_args_concepts_easy1
)