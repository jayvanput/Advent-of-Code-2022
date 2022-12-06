"""
--- Part Two ---

As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 

However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3

Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3

Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3

In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?

"""
from typing import List
if __name__ == "__main__":
    stacks: List[List[str]] = [[] for _ in range(9)]
    with open("5a stacks.txt") as f:
        for line in f:
            crates = line.rstrip().split(" ")
            for index, crate in enumerate(crates):
                if crate != "*":
                    stacks[index].append(crate)
    with open("5a.txt") as g:
        for line in g:
            count, start, end = [int(x) for x in line.rsplit()]
            
            mini_stack: List[str] = []
            for i in range(count):
                crate = stacks[start-1].pop()
                mini_stack.append(crate)
            while mini_stack:
                crate = mini_stack.pop()
                stacks[end-1].append(crate)
        output = "".join([stack[-1] for stack in stacks])
        print(output)
"""
Pre-cleaning: See solution1
Notes: Same as solution1, but we can maintain the order by using a transitional stack "mini_stack" to push in the reverse order, and then pop from the ministack to 
maintain the original order. I think this is a common type of question for coding challenges (using multiple stacks to maintain order).
"""