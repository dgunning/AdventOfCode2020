from day06 import get_common_question_count
from tools import get_puzzle_groups


def test_get_common_question_count():
    groups = get_puzzle_groups('dec06')
    question_count = get_common_question_count(groups[0])
