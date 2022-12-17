"""
--- Part Two ---

You're worried you might not ever get your items back. So worried, in fact, that your relief that a monkey's inspection didn't damage an item no longer causes your worry level to be divided by three.

Unfortunately, that relief was all that was keeping your worry levels from reaching ridiculous levels. You'll need to find another way to keep your worry levels manageable.

At this rate, you might be putting up with these monkeys for a very long time - possibly 10000 rounds!

With these new rules, you can still figure out the monkey business after 10000 rounds. Using the same example above:
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
        worry_level = self.operation(worry_level)  # The "// 3" that was here before is removed
        worry_level = worry_level % 9_699_690
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
    for _ in range(10_000):
        for monkey in monkeys:
            while monkey.items:
                monkey.tosses += 1
                monkey_number, item_worry_level = monkey.toss(monkey.items[0])
                target_monkey = monkeys[monkey_number]
                target_monkey.add_to_items(item_worry_level)

    for monkey in monkeys:
        print(monkey.tosses)

"""
Notes: Same as part 1 but you remove the // 3 since worry level doesn't go down. You can % by the product of all test values since it will give you the 
same answer without the worry levels balooning to too big levels.
Cheat: I had to look at the subreddit to see how to do this.
"""