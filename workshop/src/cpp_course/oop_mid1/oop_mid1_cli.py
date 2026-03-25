from ...base_module.base_cli import add_common_cli_args, get_common_cli_args, CLIParser
from .oop_mid1_test import OopMid1Test


def add_cli_args_oop_mid_1(parser):
    add_common_cli_args(parser)
    parser.set_defaults(func=create_task_oop_mid_1)


def create_task_oop_mid_1(args):
    common_args = get_common_cli_args(args)
    return OopMid1Test(**common_args)


oop_mid_1_parser = CLIParser(
    name='oop_mid1',
    add_cli_args=add_cli_args_oop_mid_1
)