from day12 import parse_instruction, navigate, turn, turn_right, turn_left, move_towards_waypoint, Waypoint, \
    navigate_waypoint
from tools import splitlines

test_instructions = splitlines("""
F10
N3
F7
R90
F11
""")


def test_parse_instruction():
    direction, units = parse_instruction('F10')
    assert direction == 'F'
    assert units == 10


def test_turn():
    assert turn(270, 90) == 0
    assert turn(270, 180) == 90
    assert turn(270, 270) == 180

    assert turn(270, -90) == 180
    assert turn(270, -180) == 90
    assert turn(270, -270) == 0

    assert turn(0, -90) == 270
    assert turn(90, -90) == 0
    assert turn(180, -90) == 90
    assert turn(180, -180) == 0
    assert turn(180, 180) == 0

    assert turn_right(270, 90) == 0
    assert turn_left(270, 90) == 180


def test_navigate():
    print()
    heading, longitude, latitude, manhattan = navigate(instructions=test_instructions)
    assert manhattan == 25


def test_move_towards_waypoint():
    waypoint = Waypoint(10, 1)
    assert move_towards_waypoint(waypoint, 0, 0, 10) == (100, 10)
    assert move_towards_waypoint(waypoint, 20, 20, 5) == (70, 25)


def test_move_waypoint():
    waypoint = Waypoint(10, 1)
    waypoint = waypoint.move(0, 3)
    assert waypoint.north == 4
    assert waypoint.east == 10


def test_rotate_waypoint():
    waypoint = Waypoint(10, 1)
    waypoint_rotated = waypoint.rotate_right(90)
    assert waypoint_rotated.east == 1
    assert waypoint_rotated.north == -10

    waypoint_rotated = waypoint.rotate_right(180)
    assert waypoint_rotated.east == -10
    assert waypoint_rotated.north == -1

    waypoint_rotated = waypoint.rotate_right(270)
    assert waypoint_rotated.east == -1
    assert waypoint_rotated.north == 10

    rotated = Waypoint(east=10, north=4).rotate_right(90)
    assert rotated.east == 4
    assert rotated.north == -10


def test_rotate_left():
    waypoint = Waypoint(10, 1)
    waypoint_rotated = waypoint.rotate_left(90)
    assert waypoint_rotated.east == -1
    assert waypoint_rotated.north == 10

    waypoint_rotated = waypoint.rotate_right(180)
    assert waypoint_rotated.east == -10
    assert waypoint_rotated.north == -1

    waypoint_rotated = waypoint.rotate_right(270)
    assert waypoint_rotated.east == 1
    assert waypoint_rotated.north == -10


def test_navigate_waypoint():
    print()
    heading, longitude, latitude, manhattan = navigate_waypoint(instructions=test_instructions)
    assert longitude == 214
    assert latitude == -72
    assert manhattan == 286