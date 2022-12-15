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
from typing import List, Dict, Callable


class Monkey:
    def __init__(self, items: List[int], test_function: Callable[[int], tuple[int, int]]):
        self.items = items
        self.test_function = test_function

    def toss(self, value: int) -> tuple[int, int]:
        target_monkey, item_worry_level = self.test_function(value)
        self.items.pop(0)
        return target_monkey, item_worry_level

    def add_to_items(self, item: int) -> None:
        self.items.append(item)

def test_0(worry_level: int, ) -> tuple[int, int]:
    worry_level = (worry_level * 5) % 9_699_690
    if worry_level % 7 == 0:
        return 6, worry_level
    else:
        return 7, worry_level

def test_1(worry_level: int, ) -> tuple[int, int]:
    worry_level = (worry_level + 1) % 9_699_690
    if worry_level % 17 == 0:
        return 0, worry_level
    else:
        return 6, worry_level

def test_2(worry_level: int, ) -> tuple[int, int]:
    worry_level = (worry_level + 8) % 9_699_690
    if worry_level % 11 == 0:
        return 5, worry_level
    else:
        return 3, worry_level

def test_3(worry_level: int, ) -> tuple[int, int]:
    worry_level = (worry_level + 4) % 9_699_690
    if worry_level % 13 == 0:
        return 0, worry_level
    else:
        return 1, worry_level

def test_4(worry_level: int, ) -> tuple[int, int]:
    worry_level = (worry_level + 7) % 9_699_690
    if worry_level % 19 == 0:
        return 5, worry_level
    else:
        return 2, worry_level

def test_5(worry_level: int, ) -> tuple[int, int]:
    worry_level = (worry_level + 2) % 9_699_690
    if worry_level % 2 == 0:
        return 1, worry_level
    else:
        return 3, worry_level

def test_6(worry_level: int, ) -> tuple[int, int]:
    worry_level = (worry_level * 11) % 9_699_690
    if worry_level % 5 == 0:
        return 7, worry_level
    else:
        return 4, worry_level

def test_7(worry_level: int, ) -> tuple[int, int]:
    worry_level = (worry_level * worry_level) % 9_699_690
    if worry_level % 3 == 0:
        return 4, worry_level
    else:
        return 2, worry_level

if __name__ == "__main__":
    monkey_0 = Monkey([89, 84, 88, 78, 70], test_0)
    monkey_1 = Monkey([76, 62, 61, 54, 69, 60, 85], test_1)
    monkey_2 = Monkey([83, 89, 53], test_2)
    monkey_3 = Monkey([95, 94, 85, 57], test_3)
    monkey_4 = Monkey([82, 98], test_4)
    monkey_5 = Monkey([69], test_5)
    monkey_6 = Monkey([82, 70, 58, 87, 59, 99, 92, 65], test_6)
    monkey_7 = Monkey([91, 53, 96, 98, 68, 82], test_7)


    monkeys: Dict[int, Monkey] = {
        0: monkey_0,
        1: monkey_1,
        2: monkey_2,
        3: monkey_3,
        4: monkey_4,
        5: monkey_5,
        6: monkey_6,
        7: monkey_7
    }

    tosses: Dict[int, int] = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0
    }
    for _ in range(10_000):
        while monkey_0.items:
            tosses[0] += 1
            monkey_number, item_worry_level = monkey_0.toss(monkey_0.items[0])
            target_monkey = monkeys[monkey_number]
            target_monkey.add_to_items(item_worry_level)
        while monkey_1.items:
            monkey_number, item_worry_level = monkey_1.toss(monkey_1.items[0])
            target_monkey = monkeys[monkey_number]
            tosses[1] += 1
            target_monkey.add_to_items(item_worry_level)
        while monkey_2.items:
            monkey_number, item_worry_level = monkey_2.toss(monkey_2.items[0])
            target_monkey = monkeys[monkey_number]
            tosses[2] += 1
            target_monkey.add_to_items(item_worry_level)
        while monkey_3.items:
            monkey_number, item_worry_level = monkey_3.toss(monkey_3.items[0])
            target_monkey = monkeys[monkey_number]
            tosses[3] += 1
            target_monkey.add_to_items(item_worry_level)
        while monkey_4.items:
            monkey_number, item_worry_level = monkey_4.toss(monkey_4.items[0])
            target_monkey = monkeys[monkey_number]
            tosses[4] += 1
            target_monkey.add_to_items(item_worry_level)
        while monkey_5.items:
            monkey_number, item_worry_level = monkey_5.toss(monkey_5.items[0])
            target_monkey = monkeys[monkey_number]
            tosses[5] += 1
            target_monkey.add_to_items(item_worry_level)
        while monkey_6.items:
            monkey_number, item_worry_level = monkey_6.toss(monkey_6.items[0])
            target_monkey = monkeys[monkey_number]
            tosses[6] += 1
            target_monkey.add_to_items(item_worry_level)
        while monkey_7.items:
            monkey_number, item_worry_level = monkey_7.toss(monkey_7.items[0])
            target_monkey = monkeys[monkey_number]
            tosses[7] += 1
            target_monkey.add_to_items(item_worry_level)
    for key, value in tosses.items():
        print(key, value)

"""
Notes: This problem sucks.
"""