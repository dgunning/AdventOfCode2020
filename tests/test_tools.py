from tools import get_puzzle_input, get_puzzle_groups, as_list_of_str, as_grid, splitlines


def test_puzzle_groups():
    puzzle_groups = get_puzzle_groups('dec06')
    print(puzzle_groups[-1])
    assert puzzle_groups[0] == 'jmcvr\nmarvj'
    assert puzzle_groups[-1].endswith('icvoujazphgmfs')

test_grid_data=splitlines("""
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.L
""")


def test_as_grid():
    print()
    assert test_grid_data[0] == 'L.LL.LL.LL'
    grid = as_grid(test_grid_data)
    assert grid[0] == ['L','.','L','L','.','L','L','.','L','L']
    line_list = as_list_of_str(grid)
    assert line_list[0] == 'L.LL.LL.LL'
    for row in grid:
        print(row)
