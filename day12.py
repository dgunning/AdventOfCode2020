"""
--- Day 12: Rain Risk ---

Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs
 to take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety,
 it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help, you
 quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer
 input values. After staring at them for a few minutes, you work out what they probably mean:

    Action N means to move north by the given value.
    Action S means to move south by the given value.
    Action E means to move east by the given value.
    Action W means to move west by the given value.
    Action L means to turn left the given number of degrees.
    Action R means to turn right the given number of degrees.
    Action F means to move forward by the given value in the direction the ship is currently facing.

The ship starts by facing east. Only the L and R actions change the direction the ship is facing.
(That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units,
 but would still move east if the following action were F.)

For example:

F10
N3
F7
R90
F11

These instructions would be handled as follows:

    F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
    N3 would move the ship 3 units north to east 10, north 3.
    F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
    R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
    F11 would move the ship 11 units south to east 17, south 8.

At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position
and its north/south position) from its starting position is 17 + 8 = 25.

Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's
starting position?

"""
import re
from dataclasses import dataclass
from typing import List

from tools import get_puzzle_input


def parse_instruction(instruction: str):
    match = re.match('([A-Z])(\d+)', instruction)
    return match.group(1), int(match.group(2))


@dataclass
class Waypoint:
    east: int
    north: int

    def move(self, east, north):
        return Waypoint(self.east + east, self.north + north)

    def rotate_right(self, degrees):
        if degrees == 90:
            return Waypoint(east=self.north, north=-self.east)
        elif degrees == 180:
            return Waypoint(east=-self.east, north=-self.north)
        elif degrees == 270:
            return Waypoint(east=-self.north, north=self.east)
        elif degrees == 360:
            return self

    def rotate_left(self, degrees):
        if degrees == 90:
            return Waypoint(east=-self.north, north=self.east)
        elif degrees == 180:
            return Waypoint(east=-self.east, north=-self.north)
        elif degrees == 270:
            return Waypoint(east=self.north, north=-self.east)
        elif degrees == 360:
            return self


def move_towards_waypoint(waypoint, longitude, latitude, amount):
    longitude = longitude + (amount * waypoint.east)
    latitude = latitude + (amount * waypoint.north)
    return longitude, latitude


def move(direction, longitude, latitude, distance):
    if direction == 90:
        return longitude + distance, latitude
    elif direction == 270:
        return longitude - distance, latitude
    elif direction == 0:
        return longitude, latitude + distance
    elif direction == 180:
        return longitude, latitude - distance


def turn(heading: str, degrees: int):
    heading = heading + degrees
    if heading >= 360:
        heading = heading - 360
    elif heading < 0:
        heading = heading + 360
    return heading


def turn_right(heading, degrees):
    return turn(heading, degrees)


def turn_left(heading, degrees):
    return turn(heading, -degrees)


def navigate(instructions: List[str]):
    longitude, latitude = 0, 0
    heading = 90
    for instruction in instructions:
        course, amount = parse_instruction(instruction)
        if course == 'F':
            longitude, latitude = move(heading, longitude, latitude, amount)
        elif course == 'N':
            latitude = latitude + amount
        elif course == 'S':
            latitude = latitude - amount
        elif course == 'E':
            longitude = longitude + amount
        elif course == 'W':
            longitude = longitude - amount

        elif course == 'R':
            heading = turn_right(heading, amount)
        elif course == 'L':
            heading = turn_left(heading, amount)
        manhattan = abs(longitude) + abs(latitude)
        print('heading=', heading, 'longitude=', longitude, 'latitude=', latitude, 'manhattan', manhattan)
    return heading, longitude, latitude, manhattan


def navigate_waypoint(instructions: List[str]):
    longitude, latitude = 0, 0
    waypoint = Waypoint(10, 1)
    heading = 90
    for instruction in instructions:
        course, amount = parse_instruction(instruction)
        if course == 'F':
            longitude, latitude = move_towards_waypoint(waypoint, longitude, latitude, amount)
        elif course == 'N':
            waypoint = waypoint.move(0, amount)
        elif course == 'S':
            waypoint = waypoint.move(0, -amount)
        elif course == 'E':
            waypoint = waypoint.move(amount, 0)
        elif course == 'W':
            waypoint = waypoint.move(-amount, 0)
        elif course == 'R':
            waypoint = waypoint.rotate_right(amount)
        elif course == 'L':
            waypoint = waypoint.rotate_left(amount)
        print('heading=', heading, 'longitude=', longitude, 'latitude=', latitude)
    manhattan = abs(longitude) + abs(latitude)
    return heading, longitude, latitude, manhattan


"""
--- Part Two ---

Before you can give the destination to the captain, you realize that the actual action
 meanings were printed on the back of the instructions the whole time.

Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:

    Action N means to move the waypoint north by the given value.
    Action S means to move the waypoint south by the given value.
    Action E means to move the waypoint east by the given value.
    Action W means to move the waypoint west by the given value.
    Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
    Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
    Action F means to move forward to the waypoint a number of times equal to the given value.

The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative to the ship; that is,
 if the ship moves, the waypoint moves with it.

For example, using the same instructions as above:

    F10 moves the ship to the waypoint 10 times (a total of 100 units east and 10 units north), leaving the ship at 
    east 100, north 10. The waypoint stays 10 units east and 1 unit north of the ship.
    N3 moves the waypoint 3 units north to 10 units east and 4 units north of the ship. The ship remains at east 100,
     north 10.
    F7 moves the ship to the waypoint 7 times (a total of 70 units east and 28 units north), leaving the ship at
     east 170, north 38. The waypoint stays 10 units east and 4 units north of the ship.
    R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4 units east and 10 units south
     of the ship. The ship remains at east 170, north 38.
    F11 moves the ship to the waypoint 11 times (a total of 44 units east and 110 units south), 
    leaving the ship at east 214, south 72. The waypoint stays 4 units east and 10 units south of the ship.

After these operations, the ship's Manhattan distance from its starting position is 214 + 72 = 286.

Figure out where the navigation instructions actually lead. What is the Manhattan distance between that 
location and the ship's starting position?


"""

if __name__ == '__main__':
    instructions = get_puzzle_input('day12')
    heading, longitude, latitude, manhattan = navigate(instructions)
    print('Manhattan distance is', manhattan)

    heading, longitude, latitude, manhattan = navigate_waypoint(instructions)
    print('Manhattan distance after waypoint navigation is', manhattan)
