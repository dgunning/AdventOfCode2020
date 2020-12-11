from tools import get_puzzle_input
from day05 import get_seat, get_row, get_column


def test_puzzle_input():
    puzzle_input = get_puzzle_input('dec05')
    assert puzzle_input[0] == 'FFFBFBFLRR'
    assert puzzle_input[-1] == 'FFBBBFBRLL'


def test_get_row():
    row = get_row('FBFBBFFRLR')
    assert row == 44


def test_get_column():
    column = get_column('FBFBBFFRLR')
    assert column == 5


def test_get_seat():
    assert get_seat('FBFBBFFRLR') == (44,5,357)

    # BFFFBBFRRR: row 70, column 7, seat ID 567.
    assert get_seat('BFFFBBFRRR') == (70, 7, 567)
    # FFFBBBFRRR: row 14, column 7, seat ID 119.
    assert get_seat('FFFBBBFRRR') == (14, 7, 119)
    # BBFFBBFRLL: row 102, column 4, seat ID 820.
    assert get_seat('BBFFBBFRLL') == (102, 4, 820)


