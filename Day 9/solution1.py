"""
--- Day 9: Rope Bridge ---

This rope bridge creaks as you walk along it. You aren't sure how old it is, or whether it can even support your weight.

It seems to support the Elves just fine, though. The bridge spans a gorge which was carved out by the massive river far below you.

You step carefully; as you do, the ropes stretch and twist. You decide to distract yourself by modeling rope physics; maybe you can even figure out where not to step.

Consider a rope with a knot at each end; these knots mark the head and the tail of the rope. If the head moves far enough away from the tail, the tail is pulled toward the head.

Due to nebulous reasoning involving Planck lengths, you should be able to model the positions of the knots on a two-dimensional grid. Then, by following a hypothetical series of motions (your puzzle input) for the head, you can determine how the tail will move.

Due to the aforementioned Planck lengths, the rope must be quite short; in fact, the head (H) and tail (T) must always be touching (diagonally adjacent and even overlapping both count as touching):

....
.TH.
....

....
.H..
..T.
....

...
.H. (H covers T)
...

If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough:

Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?

"""

from typing import List, Dict, Set, Union
if __name__ == "__main__":
    directions: List[List[Union[str]]] = []
    with open("9a.txt") as f:
        for line in f.readlines():
            directions.append(line.rstrip().split(" "))
    # directions = [
    #     ["R", "4"],
    #     ["U", "4"],
    #     ["L", "3"],
    #     ["D", "1"],
    #     ["R", "4"],
    #     ["D", "1"],
    #     ["L", "5"],
    #     ["R", "2"],
    # ]
    operations: Dict[str, List[int]] = {
        "R": [1,0],
        "L": [-1, 0],
        "U": [0, 1],
        "D": [0, -1]
    }
    head = [0,0]
    tail = [0,0]
    tail_positions: Set[str] = set()
    tail_positions.add("0,0")
    for step in directions:
        direction, amount = step
        operation = operations[direction]
        for _ in range(int(amount)):
            old_head = head
            head = [sum(x) for x in zip(operation, head)]
            # Check if we need to update the tail.
            if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                # Convert to string since lists aren't hashable.
                tail = old_head
                tail_position: str = ",".join([str(x) for x in tail])
                tail_positions.add(tail_position)
            # print(head, tail)
    print(len(sorted([x for x in tail_positions])))
"""
Notes: Originally thought to build a 2D array but using the indexes is much better. Pretty straightforward problem.
"""