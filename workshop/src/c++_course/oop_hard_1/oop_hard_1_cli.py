from ..base_module.base_cli import add_common_cli_args, get_common_cli_args, CLIParser
from .oop_hard_1_test import OopHard1Test


def add_cli_args_oop_hard_1(parser):
    add_common_cli_args(parser)
    parser.set_defaults(func=create_task_oop_hard_1)


def create_task_oop_hard_1(args):
    common_args = get_common_cli_args(args)
    return OopHard1Test(**common_args)


oop_hard_1_parser = CLIParser(
    name='oop_hard_task_1',
    add_cli_args=add_cli_args_oop_hard_1
)
