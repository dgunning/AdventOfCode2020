from day11 import apply_seating_rules, has_neighbours, count_adjacent_neighbours, simulate_rules, \
    visible_neighbours_in_direction, count_visible_neighbours, apply_visible_seating_rules
from tools import splitlines, print_input

layout1 = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".strip()

layout2 = """
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
""".strip()

layout3 = """
#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
""".strip()

layout4 = """
#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
""".strip()

layout6 = """
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
""".strip()


def test_apply_rules_over_rounds():
    print()
    round1 = apply_seating_rules(layout=splitlines(layout1))
    print_input(round1)
    assert round1 == splitlines(layout2)

    round2 = apply_seating_rules(layout=round1)
    print_input(round2)
    assert round2 == splitlines(layout3)

    round3 = apply_seating_rules(layout=round2)
    print_input(round3)
    assert round3 == splitlines(layout4)

    layout = splitlines(layout1)
    for i in range(6):
        layout = apply_seating_rules(layout)

    final_layout = splitlines(layout6)
    for i in range(len(layout)):
        assert layout[i] == final_layout[i]


def test_has_neighbours():
    assert not has_neighbours(list("L.LL.LL.LL"), 2)
    assert has_neighbours(list("L.L#.LL.LL"), 2)
    assert has_neighbours(list("L.#L.LL.LL"), 3)
    assert not has_neighbours(list("L.#L.LL.LL"), 9)
    assert has_neighbours(list("L.#L.LL.#L"), 9)
    assert not has_neighbours(list("#.LL.L#.##"), 3)


def test_count_adjacent_neighbours():
    layout = splitlines(layout2)
    assert count_adjacent_neighbours(layout, x=0, y=0) == 2
    assert count_adjacent_neighbours(layout, x=0, y=1) == 3
    assert count_adjacent_neighbours(layout, x=4, y=7) == 6
    assert count_adjacent_neighbours(layout, x=0, y=9) == 1
    assert count_adjacent_neighbours(layout, x=3, y=9) == 5
    assert count_adjacent_neighbours(layout, x=4, y=8) == 8

    test_layout = [splitlines((layout3))[0]]
    assert count_adjacent_neighbours(test_layout, x=6, y=0) == 8


def test_simulate_rules():
    assert simulate_rules(splitlines(layout1)) == splitlines(layout6)


layout_7 = splitlines("""
.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
""")

layout_8 = splitlines("""
.............
.L.L.#.#.#.#.
.............
""")

layout_9 = splitlines("""
.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.
""")


def test_count_neighbours_in_direction():
    assert visible_neighbours_in_direction(layout_7, x=3, y=4, x_slope=1, y_slope=0) == 1
    assert visible_neighbours_in_direction(layout_7, x=3, y=4, x_slope=1, y_slope=1) == 1
    assert visible_neighbours_in_direction(layout_7, x=3, y=4, x_slope=1, y_slope=-1) == 1
    assert visible_neighbours_in_direction(layout_7, x=3, y=4, x_slope=-1, y_slope=0) == 1
    assert visible_neighbours_in_direction(layout_7, x=3, y=4, x_slope=-1, y_slope=-1) == 1
    assert visible_neighbours_in_direction(layout_7, x=3, y=4, x_slope=-1, y_slope=1) == 1
    assert visible_neighbours_in_direction(layout_7, x=3, y=4, x_slope=0, y_slope=1) == 1
    assert visible_neighbours_in_direction(layout_7, x=3, y=4, x_slope=0, y_slope=-1) == 1


def test_count_visible_neighbours():
    assert count_visible_neighbours(layout_7, x=3, y=4) == 8
    assert count_visible_neighbours(layout_8, x=1, y=1) == 0
    assert count_visible_neighbours(layout_9, x=3, y=3) == 0


visible_round1 = splitlines("""
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
""")

visible_round2 = splitlines("""
#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#
""")

visible_round3 = splitlines("""
#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#
""")

visible_round4 = splitlines("""
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#
""")

visible_round5 = splitlines("""
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
""")

visible_round6 = splitlines("""
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
""")


def test_count_visible_neighbours2():
    assert count_visible_neighbours(visible_round2, x=3, y=0) == 0


def test_apply_visible_rules():
    round1 = apply_visible_seating_rules(splitlines(layout1))
    assert round1 == visible_round1

    round2 = apply_visible_seating_rules(round1)
    assert round2 == visible_round2

    round3 = apply_visible_seating_rules(round2)
    assert round3 == visible_round3

