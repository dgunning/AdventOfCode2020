from day10 import *
from tools import *

test_input = int_list(
    """
    16
    10
    15
    5
    1
    11
    7
    19
    6
    12
    4
    """)

test_input2 = int_list("""
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
""")


def test_get_diffs():
    assert get_diffs(test_input) == (7, 5)
    assert get_diffs(test_input2) == (22, 10)


def test_find_chains():
    adapters = [0] + test_input + [max(test_input) + 3]
    print(adapters)
    assert 8 == find_chain(adapters)

    adapters = sorted([0] + test_input2 + [max(test_input2) + 3])
    print(adapters)
    assert 8 == find_chain(adapters)
