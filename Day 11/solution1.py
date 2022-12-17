"""
--- Day 11: Monkey in the Middle ---

As you finally start making your way upriver, you realize your pack is much lighter than you remember. Just then, one of the items from your pack goes flying overhead. Monkeys are playing Keep Away with your missing things!

To get your stuff back, you need to be able to predict where the monkeys will throw your items. After some careful observation, you realize the monkeys operate based on how worried you are about each item.

You take some notes (your puzzle input) on the items each monkey currently has, how worried you are about those items, and how the monkey makes decisions based on your worry level. For example:

Each monkey has several attributes:

    Starting items lists your worry level for each item the monkey is currently holding in the order they will be inspected.
    Operation shows how your worry level changes as that monkey inspects an item. (An operation like new = old * 5 means that your worry level after the monkey inspected the item is five times whatever your worry level was before inspection.)
    Test shows how the monkey uses your worry level to decide where to throw an item next.
        If true shows what happens with an item if the Test was true.
        If false shows what happens with an item if the Test was false.

After each monkey inspects an item but before it tests your worry level, your relief that the monkey's inspection didn't damage the item causes your worry level to be divided by three and rounded down to the nearest integer.

The monkeys take turns inspecting and throwing items. On a single monkey's turn, it inspects and throws all of the items it is holding one at a time and in the order listed. Monkey 0 goes first, then monkey 1, and so on until each monkey has had one turn. The process of each monkey taking a single turn is called a round.

When a monkey throws an item to another monkey, the item goes on the end of the recipient monkey's list. A monkey that starts a round with no items could end up inspecting and throwing many items by the time its turn comes around. If a monkey is holding no items at the start of its turn, its turn ends.

In the above example, the first round proceeds as follows:

Chasing all of the monkeys at once is impossible; you're going to have to focus on the two most active monkeys if you want any hope of getting your stuff back. Count the total number of times each monkey inspects items over 20 rounds:

Monkey 0 inspected items 101 times.
Monkey 1 inspected items 95 times.
Monkey 2 inspected items 7 times.
Monkey 3 inspected items 105 times.

In this example, the two most active monkeys inspected items 101 and 105 times. The level of monkey business in this situation can be found by multiplying these together: 10605.

Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?
"""
from typing import List, Callable


class Monkey:
    def __init__(self, items: List[int], operation: Callable[[int], int], prime: int, true_monkey: int, false_monkey: int):
        self.items = items
        self.operation = operation
        self.prime = prime
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.tosses = 0

    def toss(self, value: int) -> tuple[int, int]:
        target_monkey, item_worry_level = self.test(value)
        self.items.pop(0)
        return target_monkey, item_worry_level

    def add_to_items(self, item: int) -> None:
        self.items.append(item)

    def test(self, worry_level: int) -> tuple[int, int]:
        worry_level = self.operation(worry_level) // 3
        if worry_level % self.prime == 0:
            return self.true_monkey, worry_level
        else:
            return self.false_monkey, worry_level


def monkey_0_test(worry_level: int):
        return worry_level * 5

def monkey_1_test(worry_level: int):
    return worry_level + 1

def monkey_2_test(worry_level: int):
    return worry_level + 8

def monkey_3_test(worry_level: int):
    return worry_level + 4

def monkey_4_test(worry_level: int):
    return worry_level + 7

def monkey_5_test(worry_level: int):
    return worry_level + 2

def monkey_6_test(worry_level: int):
    return worry_level * 11

def monkey_7_test(worry_level: int):
    return worry_level * worry_level

if __name__ == "__main__":


    monkey_0 = Monkey([89, 84, 88, 78, 70], monkey_0_test, 7, 6, 7)
    monkey_1 = Monkey([76, 62, 61, 54, 69, 60, 85], monkey_1_test, 17, 0, 6)
    monkey_2 = Monkey([83, 89, 53], monkey_2_test, 11, 5, 3)
    monkey_3 = Monkey([95, 94, 85, 57], monkey_3_test, 13, 0, 1)
    monkey_4 = Monkey([82, 98], monkey_4_test, 19, 5, 2)
    monkey_5 = Monkey([69], monkey_5_test, 2, 1, 3)
    monkey_6 = Monkey([82, 70, 58, 87, 59, 99, 92, 65], monkey_6_test, 5, 7, 4)
    monkey_7 = Monkey([91, 53, 96, 98, 68, 82], monkey_7_test, 3, 4, 2)

    monkeys = [monkey_0, monkey_1, monkey_2, monkey_3, monkey_4, monkey_5, monkey_6, monkey_7]
    for _ in range(20):
        for monkey in monkeys:
            while monkey.items:
                monkey.tosses += 1
                monkey_number, item_worry_level = monkey.toss(monkey.items[0])
                target_monkey = monkeys[monkey_number]
                target_monkey.add_to_items(item_worry_level)

    for monkey in monkeys:
        print(monkey.tosses)

"""
Notes: This problem is not very clean to implement but I practiced some OOP and tried to make this as clean as possible.
"""