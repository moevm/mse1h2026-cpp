from ...base_module.base_cli import add_common_cli_args, get_common_cli_args, CLIParser
from .lambda_mid_2_test import LambdaMid2Test


def add_cli_args_lambda_mid_2(parser):
    add_common_cli_args(parser)
    parser.set_defaults(func=create_task_lambda_mid_2)


def create_task_lambda_mid_2(args):
    common_args = get_common_cli_args(args)
    return LambdaMid2Test(**common_args)


lambda_mid_2_parser = CLIParser(
    name='lambda_mid_difficulty_task_2',
    add_cli_args=add_cli_args_lambda_mid_2
)
