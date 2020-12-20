from day15 import run_sequence


def test_run_sequence():
    assert run_sequence(starting_numbers=[0, 3, 6]) == 436
    assert run_sequence(starting_numbers=[2, 1, 3]) == 10
    assert run_sequence(starting_numbers=[1, 2, 3]) == 27
    assert run_sequence(starting_numbers=[2, 3, 1]) == 78
    assert run_sequence(starting_numbers=[3, 2, 1]) == 438
    assert run_sequence(starting_numbers=[3, 1, 2]) == 1836


def test_run_sequence2():
    assert run_sequence(starting_numbers=[0, 3, 6], upto=30000000) == 175594
    assert run_sequence(starting_numbers=[1, 3, 2], upto=30000000) == 2578
    assert run_sequence(starting_numbers=[2, 1, 3], upto=30000000) == 3544142