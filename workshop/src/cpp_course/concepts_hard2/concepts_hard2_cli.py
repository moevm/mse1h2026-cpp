from ...c_course.base_module.base_cli import add_common_cli_args, get_common_cli_args, CLIParser
from .concepts_hard2_test import ConceptsHard2Test

def add_cli_args_concepts_hard2(parser):
    """Добавляет аргументы для задачи Hashable"""
    add_common_cli_args(parser)
    # Устанавливаем функцию-фабрику
    parser.set_defaults(func=create_task_concepts_hard2)

def create_task_concepts_hard2(args):
    """Инстанцирует ConceptsHard2Test с общими аргументами (seed и др.)"""
    common_args = get_common_cli_args(args)
    return ConceptsHard2Test(**common_args)

# Регистрация парсера для main.py
concepts_hard2_parser = CLIParser(
    name='concepts_hard2',
    add_cli_args=add_cli_args_concepts_hard2
)