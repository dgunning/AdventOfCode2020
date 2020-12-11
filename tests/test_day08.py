from day08 import load_instructions, execute_instructions, execute_with_fixes, copy_instructions
from tools import get_puzzle_input, splitlines

test_input = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

def get_test_instructions():
    return load_instructions(splitlines(test_input))

def test_puzzle_input():
    puzzle_input = get_puzzle_input('day08')
    assert puzzle_input[0] == 'jmp +336'
    assert puzzle_input[-1] == 'jmp +1'


def test_load_instructions():
    instructions = load_instructions(splitlines(test_input))
    assert instructions[0].move == 0
    assert instructions[0].name == 'nop'

    assert instructions[-1].move == 6
    assert instructions[-1].name == 'acc'

    assert instructions[4].move == -3
    assert instructions[4].name == 'jmp'


def test_execute_instructions():
    accumulator = execute_instructions(load_instructions(splitlines(test_input)))
    assert accumulator == 5

def test_copy():
    instructions = get_test_instructions()
    assert instructions[2].name =='jmp'
    instruction_copy = copy_instructions(instructions)
    instructions[2].name == 'acc'
    assert instruction_copy[2].name == 'jmp'


def test_execute_with_fixes():
    print('')
    accumulator, exit_status, pos = execute_with_fixes(load_instructions(splitlines(test_input)))
    assert accumulator ==8
