from ...base_module.base_cli import add_common_cli_args, get_common_cli_args, CLIParser
from .oop_mid2_test import OopMid2Test


def add_cli_args_oop_mid_2(parser):
    add_common_cli_args(parser)
    parser.set_defaults(func=create_task_oop_mid_2)


def create_task_oop_mid_2(args):
    common_args = get_common_cli_args(args)
    return OopMid2Test(**common_args)


oop_mid_2_parser = CLIParser(
    name='oop_mid2',
    add_cli_args=add_cli_args_oop_mid_2
)

