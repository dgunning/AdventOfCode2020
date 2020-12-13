from tools import load_puzzle_input, splitlines
from day09 import find_outlier, find_encryption_weakness

test_input=[int(i) for i in splitlines("""
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
""")]


def test_find_outlier():
    outlier = find_outlier(test_input, window_size=5)
    assert outlier == 127


def test_find_contiguous_range():
    weakness = find_encryption_weakness(test_input, window_size=5)
    assert weakness == 62