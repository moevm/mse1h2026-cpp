from ....base_module.base_cli import add_common_cli_args, get_common_cli_args, CLIParser
from .mid_task_1_test import OperatorsOverloadingMid1Test
from pathlib import Path

def add_cli_args_mid1(parser):
    add_common_cli_args(parser)
    parser.set_defaults(func=create_task_mid1)

def create_task_mid1(args):
    common_args = get_common_cli_args(args)
    task = OperatorsOverloadingMid1Test(**common_args)

    if args.solution:
        if args.mode == "check":
            task.solution_path = f"/work/{args.solution}"
        else:
            task.solution_path = str(
                Path("tests/cpp/integration") / args.solution
            )

    return task

mid_task_1_parser = CLIParser(
    name='operators_overloading_mid_1',
    add_cli_args=add_cli_args_mid1
)