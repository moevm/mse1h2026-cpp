from ...base_module.base_cli import add_common_cli_args, get_common_cli_args, CLIParser
from .oop_hard_2_test import OopHard2Test


def add_cli_args_oop_hard_2(parser):
    add_common_cli_args(parser)
    parser.set_defaults(func=create_task_oop_hard_2)


def create_task_oop_hard_2(args):
    common_args = get_common_cli_args(args)
    return OopHard2Test(**common_args)


oop_hard_2_parser = CLIParser(
    name='oop_hard2',
    add_cli_args=add_cli_args_oop_hard_2
)
