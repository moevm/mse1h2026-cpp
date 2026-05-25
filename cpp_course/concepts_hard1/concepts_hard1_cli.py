from ...base_module.base_cli import add_common_cli_args, get_common_cli_args, CLIParser
from .concepts_hard1_test import ConceptsHard1Test

def add_cli_args_concepts_hard1(parser):
    add_common_cli_args(parser)
    parser.set_defaults(func=create_task_concepts_hard1)

def create_task_concepts_hard1(args):
    common_args = get_common_cli_args(args)
    return ConceptsHard1Test(**common_args)

concepts_hard1_parser = CLIParser(
    name='concepts_hard1',
    add_cli_args=add_cli_args_concepts_hard1
)