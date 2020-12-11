
def load_puzzle_input(day):
    with open(f'input/{day}.txt') as f:
        return f.read().strip()


def int_list(text:str):
    return [int(i) for i in splitlines(text.strip())]


def splitlines(text:str):
    return [line.strip() for line in text.splitlines() if line]


def get_puzzle_input(day):
    puzzle_input = load_puzzle_input(day)
    return splitlines(puzzle_input)


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
