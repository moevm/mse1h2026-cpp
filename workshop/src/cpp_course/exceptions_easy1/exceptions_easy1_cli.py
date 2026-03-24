from ...c_course.base_module.base_cli import add_common_cli_args, get_common_cli_args, CLIParser
from .exceptions_easy1_test import ExceptionsEasy1Test

def add_cli_args_exceptions_easy1(parser):
    add_common_cli_args(parser)
    parser.set_defaults(func=create_task_exceptions_easy1)

def create_task_exceptions_easy1(args):
    common_args = get_common_cli_args(args)
    return ExceptionsEasy1Test(**common_args)

exceptions_easy1_parser = CLIParser(
    name='exceptions_easy1',
    add_cli_args=add_cli_args_exceptions_easy1
)