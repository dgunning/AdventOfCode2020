from tools import get_puzzle_input, get_puzzle_groups


def test_puzzle_groups():
    puzzle_groups = get_puzzle_groups('dec06')
    print(puzzle_groups[-1])
    assert puzzle_groups[0] == 'jmcvr\nmarvj'
    assert puzzle_groups[-1].endswith('icvoujazphgmfs')