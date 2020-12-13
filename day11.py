"""
--- Day 11: Seating System ---

Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the
 tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you
 realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can
 predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#).
For example, the initial seat layout might look like this:

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

Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable
and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to
a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat).
 The following rules are applied to every seat simultaneously:

    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.

Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

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

After a second round, the seats with four or more occupied adjacent seats become empty again:

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

This process continues for three more rounds:

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

#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##

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

At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause
no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many
seats end up occupied?


"""
from tools import get_puzzle_input, as_list_of_str, as_grid


def get_layout():
    input = get_puzzle_input('day11')
    return [list(line) for line in input]


def has_neighbours(row, x):
    left_occupied = x > 0 and row[x - 1] == '#'
    right_occupied = x < (len(row) - 2) and row[x + 1] == '#'
    return left_occupied or right_occupied


def count_adjacent_neighbours(layout, x, y):
    """
    # four or more seats adjacent to it are also occupied, the seat becomes empty.
    :param layout:
    :param x:
    :param y:
    :return:
    """
    num_neighbours = 0
    y_start, y_end = max(0, y - 1), min(len(layout) - 1, y + 1)
    x_start, x_end = max(0, x - 1), min(len(layout[y]) - 1, x + 1)
    for _y in range(y_start, y_end + 1):
        for _x in range(x_start, x_end + 1):
            if x == _x and _y == y:
                continue
            if layout[_y][_x] == '#':
                num_neighbours = num_neighbours + 1
    return num_neighbours


def visible_neighbours_in_direction(layout, x, y, x_slope, y_slope):
    _x, _y = x, y
    height = len(layout)
    width = len(layout[y])
    while True:
        _x = _x + x_slope
        _y = _y + y_slope
        if _y < 0 or _y > height -1:
            break
        if _x < 0 or _x > width -1:
            break
        spot = layout[_y][_x]
        if spot == '#':
            return 1
        elif spot == 'L':
            return 0
    return 0


def count_visible_neighbours(layout, x, y):
    slopes = [(1, -1), (1, 0), [1, 1], (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    num_visible_neighbours = 0
    for x_slope, y_slope in slopes:
        visible_in_direction = visible_neighbours_in_direction(layout,x,y, x_slope, y_slope)
        num_visible_neighbours = num_visible_neighbours + visible_in_direction
    return num_visible_neighbours


def apply_seating_rules(layout):
    grid = as_grid(layout)

    for y in range(len(layout)):
        row = grid[y]
        for x in range(len(row)):
            seat = layout[y][x]
            if seat == 'L':
                if count_adjacent_neighbours(layout, x, y) == 0:
                    grid[y][x] = '#'
            elif seat == '#':
                if count_adjacent_neighbours(layout, x, y) >= 4:
                    grid[y][x] = 'L'
            else:
                grid[y][x] = '.'
    return as_list_of_str(grid)


def apply_visible_seating_rules(layout):
    grid = as_grid(layout)

    for y in range(len(layout)):
        row = grid[y]
        for x in range(len(row)):
            seat = layout[y][x]
            if seat == 'L':
                if count_visible_neighbours(layout, x, y) == 0:
                    grid[y][x] = '#'
            elif seat == '#':
                if count_visible_neighbours(layout, x, y) >= 5:
                    grid[y][x] = 'L'
            else:
                grid[y][x] = '.'
    return as_list_of_str(grid)


def simulate_rules(layout):
    last_layout = None
    while True:
        layout = apply_seating_rules(layout)
        if layout == last_layout:
            break
        last_layout = layout

    return last_layout


def simulate_visible_rules(layout):
    last_layout = None
    while True:
        layout = apply_visible_seating_rules(layout)
        if layout == last_layout:
            break
        last_layout = layout

    return last_layout


def count_occupied(layout):
    return sum([row.count('#') for row in layout])


"""
As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats -
 they care about the first seat they can see in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of 
those eight directions. For example, the empty seat below would see eight occupied seats:

.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....

The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

.............
.L.L.#.#.#.#.
.............

The empty seat below would see no occupied seats:

.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.

Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for 
an occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply:
 empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

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

Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs,
 you count 26 occupied seats.

Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, 
how many seats end up occupied?
"""
if __name__ == '__main__':
    layout = get_layout()
    final_layout = simulate_rules(layout)

    print("There are", count_occupied(final_layout), "occupied seats with adjacent rules")

    final_layout_with_visible_rules = simulate_visible_rules(layout)
    print("There are", count_occupied(final_layout_with_visible_rules), "occupied seats with visible rules")
