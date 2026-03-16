import argparse
from ..base_module.base_cli import add_common_cli_args, get_common_cli_args, CLIParser
from .lab1_test import Lab1HelloTest


def add_cli_args_lab1(parser):
    """Добавляет аргументы для первого задания"""
    # Сначала добавляем общие аргументы
    add_common_cli_args(parser)

    # Устанавливаем функцию создания задания
    parser.set_defaults(func=create_task_lab1)


def create_task_lab1(args):
    """Создает задание из аргументов командной строки"""
    common_args = get_common_cli_args(args)
    return Lab1HelloTest(
        **common_args,
    )


# Создаем объект CLIParser для этого задания
lab1_parser = CLIParser(
    name='lab1_hello',
    add_cli_args=add_cli_args_lab1
)