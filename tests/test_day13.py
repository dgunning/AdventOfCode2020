from tools import *
from day13 import get_offset, get_next_times, get_next_buses, load_schedule, get_earliest_bus, \
    find_timestamp_at_matching_offsets, find_offset_timestamp, lcm
import math

test_input=splitlines("""
939
7,13,x,x,59,x,31,19
""")


def test_get_offset():
    assert get_offset(939, 7) == 6
    assert get_offset(939, 13) == 10
    assert get_offset(939, 59) == 5
    assert 31 - get_offset(939, 31) == 9
    assert 19 - get_offset(939, 19) == 8


def test_get_earliest_starts():
    timestamp = 939
    assert get_next_times(timestamp, 7) == 945
    assert get_next_times(timestamp, 13) == 949
    assert get_next_times(timestamp, 59) == 944


def test_get_next_buses():
    timestamp, buses, offset = load_schedule(test_input)
    next_buses = get_next_buses(timestamp, buses)
    assert next_buses[0] == (7, 945)


def test_load_schedule():
    timestamp, buses, offset = load_schedule(test_input)
    assert timestamp == 939
    assert offset == [0, 1, 4, 6, 7]


def test_get_earliest():
    timestamp, buses, offset = load_schedule(test_input)
    assert offset == [0, 1, 4, 6,7]
    bus, next_time, wait = get_earliest_bus(timestamp, buses)
    assert bus == 59
    assert next_time == 944
    assert wait == 5
    assert bus * wait == 295


def test_find_matching_offsets():
    print()
    assert find_timestamp_at_matching_offsets("17,x,13,19") == 3417
    assert find_timestamp_at_matching_offsets("67,7,59,61") == 754018
    assert find_timestamp_at_matching_offsets("67,x,7,59,61") == 779210
    assert find_timestamp_at_matching_offsets("67,7,x,59,61") == 1261476
    assert find_timestamp_at_matching_offsets("1789,37,47,1889") == 1202161486


def test_getlcm():
    print(lcm([17,13]))
    print(lcm([17,13,19]))


def test_find_offset_timestamp():
    #lines = ["17,x,13,19", "67,7,59,61", "67,x,7,59,61", "67,7,x,59,61", "1789,37,47,1889"]
    assert find_offset_timestamp("17,x,13,19") == 3417