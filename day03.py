from tools import get_puzzle_input
from functools import reduce

"""
--- Day 3: Toboggan Trajectory ---

With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy,
 it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which
  angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map
 (your puzzle input) of the open squares (.) and trees (#) you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#

These aren't the only trees, though; due to something you read about once involving arboreal
 genetics and biome stability, the same pattern repeats to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

You start on the open square (.) in the top-left corner and need to reach the bottom 
(below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers);
 start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, 
check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X 
where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees 
would you encounter?

"""
puzzle_input = get_puzzle_input('dec03')

x, y = 0, 0
height_of_mountain = len(puzzle_input)
print(height_of_mountain)

mountain = [line * 200 for line in puzzle_input]
for line in mountain.copy():
    mountain.append(line)


def get_trees_on_slope(mountain):
    x, y = 0, 0
    num_trees = 0
    for i in range(0, len(mountain) - 1):
        x = x + 3
        y = y + 1
        print(i, x, y)
        spot = mountain[y][x]
        if spot == '#':
            num_trees = num_trees + 1
            yield spot


def get_num_trees(mountain, slope):
    num_trees = 0
    width, height = len(mountain[0]), len(mountain)
    x,y = slope
    while y < height:
        line = mountain[y]
        spot = line[x]
        if spot == '#':
            num_trees = num_trees+1
        x = x + slope[0]
        if x - width >= 0:
            x = x - width
        y = y + slope[1]

    return num_trees


def multiply_trees_on_slopes(mountain, slopes):
    result = 1
    for slope in slopes:
        num_trees = get_num_trees(mountain, slope)
        print("slope", slope, "num_trees is", num_trees)
        result = result * num_trees
    return result


def mark_spot(line, x, marker):
    marked = list(line)
    marked[x] = marker
    return ''.join(marked)


def mark_trees(a_mountain, slope=(3, 1)):
    mountain = a_mountain.copy()
    x, y = 0, 0
    print('')
    #print(mountain[y])
    for i in range(0, len(mountain) - 1):
        x = x + slope[0]
        y = y + slope[1]
        line = mountain[y]
        spot = line[x]
        mountain[y] = mark_spot(mountain[y], x, 'X' if spot == '#' else '0')
        #print(mountain[y])
    return mountain


def count_trees(mountain, slope=(3, 1)):
    mountain_copy = mountain.copy()
    marked_mountain = mark_trees(mountain_copy, slope=slope)
    return sum([row.count('X') for row in marked_mountain])


trees = list(get_trees_on_slope(mountain))

print("There are",
      len(trees),
      "trees on the slope")

"""
--- Part Two ---

Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes,
 you start at the top-left corner and traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together,
 these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?

"""

slopes = [(1, 1), (3, 1), (5, 1), (7,1),(1,2)]


def find_multipicand(slopes):
    tree_counts = [count_trees(mountain, slope) for slope in slopes ]
    multiplicand = 1
    for i in tree_counts:
        multiplicand = i * multiplicand
    print("The multiplied result is",
          multiplicand)
