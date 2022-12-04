"""
As you finish identifying the misplaced items, the Elves come to you with another issue.

For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their group. For efficiency, within each group of three Elves, the badge is the only item type carried by all three Elves. That is, if a group's badge is item type B, then all three Elves will have item type B somewhere in their rucksack, and at most two of the Elves will be carrying any other item type.

The problem is that someone forgot to put this year's updated authenticity sticker on the badges. All of the badges need to be pulled out of the rucksacks so the new authenticity stickers can be attached.

Additionally, nobody wrote down which item type corresponds to each group's badges. The only way to tell which item type is the right one is by finding the one item type that is common between all three Elves in each group.

Every set of three lines in your list corresponds to a single group, but each group can have a different badge item type. So, in the above example, the first group's rucksacks are the first three lines:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg

And the second group's rucksacks are the next three lines:

wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw

In the first group, the only item type that appears in all three rucksacks is lowercase r; this must be their badges. In the second group, their badge item type must be Z.

Priorities for these items must still be found to organize the sticker attachment efforts: here, they are 18 (r) for the first group and 52 (Z) for the second group. The sum of these is 70.

Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?
"""
from typing import Dict
if __name__ == "__main__":
    with open("3a.txt") as f:
        rucksacks = [line.rstrip() for line in f]
    LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    three_elf_groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]

    output = 0
    for group in three_elf_groups:
        item_counts: Dict[str, int] = {}
        for rucksack in group:
            unique_items = set(rucksack)
            for item in unique_items:
                item_counts[item] = item_counts.get(item, 0) + 1  
                if item_counts[item] == 3:
                    output += LETTERS.index(item) + 1
                    break
    print(output)
"""
Notes: First, we bulid our groups of 3 in O(n). 
Then we create a set for each rucksack, which is done for every rucksack, so O(n). 
Finally, we iterate over each set of rucksack to add to the dictionary. Once we find the letter that appears 3 times, we exit the loop early. This is still O(n) in the 
worst case for each rucksack (if rucksacks all have unique letters and the shared letter is the last one in the third rucksack). 
Lookups and assignments in a dictionary are O(1) due to hashmaps. So the whole thing runs in O(n).

"""