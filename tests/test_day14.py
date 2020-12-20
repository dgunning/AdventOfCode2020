from day14 import *
from tools import *

test_input = splitlines("""
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
""")


def test_to_binary():
    assert to_binary(num=37) == '100101'.zfill(36)
    assert to_binary(num=11) == '1011'.zfill(36)
    assert to_binary(num=101) == '1100101'.zfill(36)
    assert to_binary(num=0) == '0'.zfill(36)
    assert to_binary(num=42) == '101010'.zfill(36)


def test_apply_mask():
    mask = get_mask(test_input[0])
    assert apply_mask(mask, to_binary(num=11, pad=36)) == 73
    assert apply_mask(mask, to_binary(num=101, pad=36)) == 101
    assert apply_mask(mask, to_binary(num=0, pad=36)) == 64


def test_execute_instructions():
    print()
    register = execute_instructions(test_input, masklen=36)
    print('Register sum is', sum(register.values()))


test_input2 = splitlines("""
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
""")


def test_apply_mask_v2():
    assert apply_mask_v2('000000000000000000000000000000X1001X',
                         '000000000000000000000000000000101010') == '000000000000000000000000000000X1101X'

    assert apply_mask_v2('00000000000000000000000000000000X0XX',
                         '000000000000000000000000000000011010') == '00000000000000000000000000000001X0XX'


def test_fork_x():
    assert forkX('000000000000000000000000000000X1101X') == [26,27, 58, 59]


def test_execute_instructions_v2():
    print()
    register = execute_program_v2(test_input2)
    print('Register sum is', sum(register.values()))


def test_get_mem_locations():
    print()
    chunks = forkX('0001X0XX')
    print(chunks)
