# Ручной импорт лабораторных работ
from .concepts_easy1 import ConceptsEasy1Test, concepts_easy1_parser
from .concepts_hard1 import ConceptsHard1Test, concepts_hard1_parser
from .concepts_hard2 import ConceptsHard2Test, concepts_hard2_parser
from .exceptions_easy1 import ExceptionsEasy1Test, exceptions_easy1_parser
from .lambda_easy1 import LambdaEasy1Test, lambda_easy1_parser

# Собираем все парсеры в список для удобства
PARSERS = [
    concepts_easy1_parser,
    concepts_hard1_parser,
    concepts_hard2_parser,
    exceptions_easy1_parser,
    lambda_easy1_parser,
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
]