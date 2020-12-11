from day03 import mark_trees, count_trees, mountain, get_num_trees, multiply_trees_on_slopes
from tools import splitlines, load_puzzle_input

test_input = """
..##.........##.........##.........##.........##.........##.......
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#
"""

test_mountain = splitlines(test_input)


def test_toboggan_slope():
    for line in test_mountain:
        print(line)


def test_mark_trees():
    marked_mountain = mark_trees(test_mountain)
    assert 'X' in marked_mountain[2]


def test_count_trees():
    num_trees = count_trees(test_mountain)
    assert num_trees == 7


def test_count_full_mountain():
    num_trees = count_trees(mountain)
    print("There are", num_trees, "trees on mountain")


def test_get_num_trees():
    assert get_num_trees(test_mountain, (1, 1)) == 2
    assert get_num_trees(test_mountain, (3, 1)) == 7
    assert get_num_trees(test_mountain, (5, 1)) == 3
    assert get_num_trees(test_mountain, (7, 1)) == 4
    assert get_num_trees(test_mountain, (1, 2)) == 2


def test_multiply_trees():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    #result = multiply_trees_on_slopes(test_mountain, slopes)
    #assert result == 336
    #mountain = load_puzzle_input('dec03')
    result = multiply_trees_on_slopes(mountain, slopes)
    print(result)
