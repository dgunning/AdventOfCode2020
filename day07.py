"""
--- Day 7: Handy Haversacks ---

You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty,
 every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be
valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

    A bright white bag, which can hold your shiny gold bag directly.
    A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
    A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold
    your shiny gold bag.
    A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your
     shiny gold bag.

So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long;
make sure you get all of it.)

"""
from dataclasses import dataclass
from typing import List

from tools import get_puzzle_input

puzzle_input = get_puzzle_input('day07')


class Bag:

    def __init__(self, name):
        self.name: str = name
        self.children: List = []
        self.parents: List = []

    def add_bag(self, num, bag):
        self.children.append((num, bag))
        bag.parents.append(self)

    def contains_directly(self, bag_name):
        for num, child in self.children:
            if bag_name == child.name:
                return True
        return False

    def contains(self, bag_name):
        if self.contains_directly(bag_name):
            return True
        for num, child in self.children:
            if child.contains(bag_name):
                return True
        return False

    def get_number_of_bags_contained(self):
        bag_number = 0
        for num, child in self.children:
            # How many bags are in this bag
            bag_number = bag_number + int(num)
            # How many bags do the child bags contain
            bag_number = bag_number + (child.get_number_of_bags_contained() * int(num))
        return bag_number

    def __repr__(self):
        return f"{self.name} bag"


def get_bag_chains(bag_input):
    bag_chains = []
    for line in bag_input:
        bag, _, contents = line.strip('.').partition('contain')
        bag_contents = [(bag_line[1], bag_line[3:]) for bag_line in contents.split(',')]
        bag_chains.append((bag.strip(), bag_contents))
    return bag_chains


def build_tree(bag_input):
    bags = dict()
    for line in bag_input:
        if 'no other bags.' not in line:
            container, _, contents = line.strip('.').partition('contain')
            container = container.replace('bags', '').strip()
            for bag_line in contents.split(','):
                bag_line = bag_line.strip()
                index = bag_line.find(' ')
                num, bag = bag_line[:index], bag_line[index:].replace('bags', '').replace('bag', '').strip()
                if container not in bags:
                    bags[container] = Bag(container)
                if bag not in bags:
                    bags[bag] = Bag(bag)
                bags[container].add_bag(num, bags[bag])

    return bags


bags = build_tree(get_puzzle_input('day07'))

print("There are",
      len(bags),
      "bags")

bags_with_gold = list(filter(lambda b: b.contains('shiny gold'), bags.values()))

print("There are",
      len(bags_with_gold),
      "bag colors that can contain shiny gold bags")

"""
--- Part Two ---

It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number
 of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

    faded blue bags contain 0 other bags.
    dotted black bags contain 0 other bags.
    vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
    dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.

So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags 
(and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; 
be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.

In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?

"""
print('Shiny gold bags contain',
        bags['shiny gold'].get_number_of_bags_contained(),
      'bags in total'
      )
