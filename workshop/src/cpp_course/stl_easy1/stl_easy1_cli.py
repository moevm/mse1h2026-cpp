from ...base_module.base_cli import add_common_cli_args, get_common_cli_args, CLIParser
from .stl_easy1_test import StlEasy1Test


def add_cli_args_stl_easy_1(parser):
    add_common_cli_args(parser)
    parser.set_defaults(func=create_task_stl_easy_1)


def create_task_stl_easy_1(args):
    common_args = get_common_cli_args(args)
    return StlEasy1Test(**common_args)


stl_easy_1_parser = CLIParser(
    name='stl_easy1',
    add_cli_args=add_cli_args_stl_easy_1
)
