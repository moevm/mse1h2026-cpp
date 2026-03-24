from ...base_module.base_cli import add_common_cli_args, get_common_cli_args, CLIParser
from .lambda_mid_1_test import LambdaMid1Test


def add_cli_args_lambda_mid_1(parser):
    add_common_cli_args(parser)
    parser.set_defaults(func=create_task_lambda_mid_1)


def create_task_lambda_mid_1(args):
    common_args = get_common_cli_args(args)
    return LambdaMid1Test(**common_args)


lambda_mid_1_parser = CLIParser(
    name='lambda_mid_1',
    add_cli_args=add_cli_args_lambda_mid_1
)
