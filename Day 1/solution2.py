"""
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""


import heapq

if __name__ == "__main__":
    with open("1a.txt") as f:
        food_list = [line.rstrip() for line in f]

    TOP_N = 3

    heap = []
    current_calories = 0
    for item in food_list:
        if item != "":
            current_calories += int(item)
        else:  # We have finished with the current elf.
            if len(heap) >= 3:
                # Compare this elf to the current top 3.
                heapq.heappushpop(heap, current_calories)
            else:
                # We don't have 3 elves yet, so add it to the heap.
                heapq.heappush(heap, current_calories)
            current_calories = 0
            print(heap)
    print(sum(heap))

"""
Notes: A bit trickier, but this is a classic Top-N problem that can be solved with a heap. When we finish an elf, we check if we need to push it into the heap or just
skip it if it is smaller than the current heap minimum value. We are left with the 3 largest elves in the heap and can return the sum of the list. Pushing and popping 
from a heap is done in O(logn) (which in the worst case is done for every elf) so this solves in O(n*log(n))
"""