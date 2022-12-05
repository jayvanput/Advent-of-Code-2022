"""
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

    5-7,7-9 overlaps in a single section, 7.
    2-8,3-7 overlaps all of the sections 3 through 7.
    6-6,4-6 overlaps in a single section, 6.
    2-6,4-8 overlaps in sections 4, 5, and 6.

So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
"""
from typing import List


if __name__ == "__main__":
    with open("4a.txt") as f:
        pairs: List[List[int]] = []
        for line in f:
            line = line.rstrip()
            line_split = [int(x) for x in line.split("-")]
            pairs.append(line_split)

    count_of_contained_pairs = 0

    for pair in pairs:
        # Check if any of the ends of the first assignment are with the range of the second assignment.
        if (pair[0] >= pair[2] and pair[0] <= pair[3]) or (
            pair[1] >= pair[2] and pair[1] <= pair[3]) or (
            pair[2] >= pair[0] and pair[2] <= pair[1]) or (
            pair[3] >= pair[0] and pair[3] <= pair[1]):
            count_of_contained_pairs += 1
    print(count_of_contained_pairs)

"""
Notes: Changes to the original input file were made to reduce code cleaning. This includes:
    - Replacing the comma separator with a dash. This allows me to split the row into 4 ints to use in the code.
Same as solution 1 really. Solves in O(n) with an even hairier logical condition. Hardest part of this problem was following PEP8 on the if statement structure!
"""