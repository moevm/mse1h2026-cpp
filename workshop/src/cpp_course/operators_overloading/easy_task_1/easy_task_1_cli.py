from ....base_module.base_cli import add_common_cli_args, get_common_cli_args, CLIParser
from .easy_task_1_test import OperatorsOverloadingEasy1Test


def add_cli_args_easy(parser):
    add_common_cli_args(parser)
    parser.set_defaults(func=create_task_easy)


def create_task_easy(args):
    common_args = get_common_cli_args(args)
    task = OperatorsOverloadingEasy1Test(**common_args)

    if hasattr(args, "solution") and args.solution:
        task.solution_path = args.solution

    return task


easy_task_1_parser = CLIParser(
    name='operators_overloading_easy_1',
    add_cli_args=add_cli_args_easy
)