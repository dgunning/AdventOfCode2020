from typing import List, Any


def load_puzzle_input(day):
    with open(f'input/{day}.txt') as f:
        return f.read().strip()


def int_list(text: str):
    return [int(i) for i in splitlines(text.strip())]


def splitlines(text: str):
    return [line.strip() for line in text.splitlines() if line]


def get_puzzle_input(day):
    puzzle_input = load_puzzle_input(day)
    return splitlines(puzzle_input)


def print_input(puzzle_input):
    print()
    for row in puzzle_input:
        print(row)


def as_grid(data: List[Any]) -> List[List[Any]]:
    """
    Convert the list of int or str to a grid or list of lists
    :param data:
    :return: A List of Lists, simulating a gri
    """
    return [list(line) for line in data]


def as_list_of_str(data: List[List[Any]]):
    return [''.join(l) for l in data]


def get_puzzle_groups(day):
    groups = []
    puzzle_input = get_puzzle_input(day)
    num_lines = len(puzzle_input)
    text = '\n'
    for i in range(num_lines):
        if puzzle_input[i] == '' or i == num_lines:
            groups.append(text.strip())
            text = '\n'
        else:
            text = text + puzzle_input[i] + '\n'
    groups.append(text.strip())
    return groups


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


class Node:

    def __init__(self, value: List):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def is_leaf(self):
        return len(self.children) == 0