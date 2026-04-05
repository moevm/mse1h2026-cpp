from ....base_module.base_cli import add_common_cli_args, get_common_cli_args, CLIParser
from .mid_task_2_test import OperatorsOverloadingMid2Test


def add_cli_args_mid2(parser):
    add_common_cli_args(parser)
    parser.set_defaults(func=create_task_mid2)


def create_task_mid2(args):
    common_args = get_common_cli_args(args)
    task = OperatorsOverloadingMid2Test(**common_args)

    if hasattr(args, "solution") and args.solution:
        task.solution_path = args.solution

    return task


mid_task_2_parser = CLIParser(
    name='operators_overloading_mid_2',
    add_cli_args=add_cli_args_mid2
)