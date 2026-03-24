from src.base_module import BaseTaskClass, TestItem, CLIParser, add_common_cli_args
from .lambda_mid_1 import LambdaMid1Test, lambda_mid_1_parser
from .lambda_mid_2 import LambdaMid2Test, lambda_mid_2_parser
from .oop_easy_1 import OopEasy1Test, oop_easy_1_parser
from .oop_hard_1 import OopHard1Test, oop_hard_1_parser
from .oop_hard_2 import OopHard2Test, oop_hard_2_parser

__all__ = [
    "BaseTaskClass",
    "TestItem",
    "CLIParser",
    "add_common_cli_args",
    "get_common_cli_args",
    "LambdaMid1Test",
    "lambda_mid_1_parser",
    "LambdaMid2Test",
    "lambda_mid_2_parser",
    "OopEasy1Test",
    "oop_easy_1_parser",
    "OopHard1Test",
    "oop_hard_1_parser",
    "OopHard2Test",
    "oop_hard_2_parser",
]
