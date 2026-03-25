from ...base_module.base_cli import add_common_cli_args, get_common_cli_args, CLIParser
from .operators_overloading_test import (
    OperatorsOverloadingEasy1Test,
    OperatorsOverloadingMid1Test,
    OperatorsOverloadingMid2Test,
)


def add_cli_args_easy(parser):
    add_common_cli_args(parser)
    parser.set_defaults(func=create_task_easy)


def create_task_easy(args):
    common_args = get_common_cli_args(args)
    return OperatorsOverloadingEasy1Test(**common_args)


easy_task_1_parser = CLIParser(
    name='operators_overloading_easy_1',
    add_cli_args=add_cli_args_easy
)


def add_cli_args_mid1(parser):
    add_common_cli_args(parser)
    parser.set_defaults(func=create_task_mid1)


def create_task_mid1(args):
    common_args = get_common_cli_args(args)
    return OperatorsOverloadingMid1Test(**common_args)


mid_task_1_parser = CLIParser(
    name='operators_overloading_mid_1',
    add_cli_args=add_cli_args_mid1
)


def add_cli_args_mid2(parser):
    add_common_cli_args(parser)
    parser.set_defaults(func=create_task_mid2)


def create_task_mid2(args):
    common_args = get_common_cli_args(args)
    return OperatorsOverloadingMid2Test(**common_args)


mid_task_2_parser = CLIParser(
    name='operators_overloading_mid_2',
    add_cli_args=add_cli_args_mid2
)