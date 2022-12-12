"""
--- Part Two ---

A rope snaps! Suddenly, the river is getting a lot closer than you remember. The bridge is still there, but some of the ropes that broke are now whipping toward you as you fall through the air!

The ropes are moving too quickly to grab; you only have a few seconds to choose how to arch your body to avoid being hit. Fortunately, your simulation can be extended to support longer ropes.

Rather than two knots, you now must simulate a rope consisting of ten knots. One knot is still the head of the rope and moves according to the series of motions. Each knot further down the rope follows the knot in front of it using the same rules as before.

Using the same series of motions as the above example, but with the knots marked H, 1, 2, ..., 9, the motions now occur as follows:

Now, you need to keep track of the positions the new tail, 9, visits. In this example, the tail never moves, and so it only visits 1 position. However, be careful: more types of motion are possible than before, so you might want to visually compare your simulated rope to the one above.

Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of the rope visit at least once?
"""
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
    directions: List[List[str]] = []
    with open("9a.txt") as f:
        for line in f.readlines():
            directions.append(line.rstrip().split(" "))
    # directions = [
    #     ["R", "5"],
    #     ["U", "8"],
    #     ["L", "8"],
    #     ["D", "3"],
    #     ["R", "17"],
    #     ["D", "10"],
    #     ["L", "25"],
    #     ["U", "20"],
    # ]
    operations: Dict[str, List[int]] = {
        "R": [1,0],
        "L": [-1, 0],
        "U": [0, 1],
        "D": [0, -1]
    }
    rope = [[0,0] for _ in range(10)] 
    tail_positions: Set[str] = set()
    tail_positions.add("0,0")
    for step in directions:
        direction, amount = step
        operation = operations[direction]
        for _ in range(int(amount)):
            prev_segment_old_position = rope[0]
            new_position = [sum(x) for x in zip(operation, rope[0])]
            rope[0] = new_position
            for index, segment in enumerate(rope):
                # Check if we need to update the segment.
                if abs(new_position[0] - segment[0]) > 1 or abs(new_position[1] - segment[1]) > 1:
                    # Convert to string since lists aren't hashable.
                    current_position = rope[index]
                    if new_position[0] > current_position[0]:
                        current_position = [sum(x) for x in zip([1,0], current_position)]
                    elif new_position[0] < current_position[0]:
                        current_position = [sum(x) for x in zip([-1,0], current_position)]
                    if new_position[1] > current_position[1]:
                        current_position = [sum(x) for x in zip([0,1], current_position)]
                    elif new_position[1] < current_position[1]:
                        current_position = [sum(x) for x in zip([0,-1], current_position)]
                    rope[index] = current_position
                    if index == 9:
                        tail_position: str = ",".join([str(x) for x in rope[index]])
                        tail_positions.add(tail_position)
                    prev_segment_old_position = current_position
                new_position = rope[index]
            # print(head, tail)
    print(len(sorted([x for x in tail_positions])))
"""
Notes: I had issues with the new logic for moving the segments which caused some headache. The if/elif loop handles that well but
it can definitely be cleaned up.
"""