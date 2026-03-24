# Ручной импорт лабораторных работ
from .concepts_easy1 import ConceptsEasy1Test, concepts_easy1_parser
from .concepts_hard1 import ConceptsHard1Test, concepts_hard1_parser
from .concepts_hard2 import ConceptsHard2Test, concepts_hard2_parser
from .exceptions_easy1 import ExceptionsEasy1Test, exceptions_easy1_parser
from .lambda_easy1 import LambdaEasy1Test, lambda_easy1_parser

from .lambda_mid_1 import LambdaMid1Test, lambda_mid_1_parser
from .lambda_mid_2 import LambdaMid2Test, lambda_mid_2_parser
from .oop_easy_1 import OopEasy1Test, oop_easy_1_parser
from .oop_hard_1 import OopHard1Test, oop_hard_1_parser
from .oop_hard_2 import OopHard2Test, oop_hard_2_parser

# Собираем все парсеры в список для удобства
PARSERS = [
    concepts_easy1_parser,
    concepts_hard1_parser,
    concepts_hard2_parser,
    exceptions_easy1_parser,
    lambda_easy1_parser,

    lambda_mid_1_parser,
    lambda_mid_2_parser,
    oop_easy_1_parser,
    oop_hard_1_parser,
    oop_hard_2_parser,
]

# Экспортируем все
__all__ = [
    PARSERS,

    # Классы проверки заданий
    'ConceptsEasy1Test',
    'ConceptsHard1Test',
    'ConceptsHard2Test',
    'ExceptionsEasy1Test',
    'LambdaEasy1Test',

    'LambdaMid1Test',
    'LambdaMid2Test',
    'OopEasy1Test',
    'OopHard1Test',
    'OopHard2Test',
]
