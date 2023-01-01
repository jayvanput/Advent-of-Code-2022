"""
--- Part Two ---
As you walk up the hill, you suspect that the Elves will want to turn this into a hiking trail. The beginning isn't very scenic, though; perhaps you can find a better starting point.

To maximize exercise while hiking, the trail should start as low as possible: elevation a. The goal is still the square marked E. However, the trail should still be direct, taking the fewest steps to reach its goal. So, you'll need to find the shortest path from any square at elevation a to the square marked E.

Again consider the example from above:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Now, there are six choices for starting position (five marked a, plus the square marked S that counts as being at elevation a). If you start at the bottom-left square, you can reach the goal most quickly:

...v<<<<
...vv<<^
...v>E^^
.>v>>>^^
>^>>>>>^

This path reaches the goal in only 29 steps, the fewest possible.

What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?
"""
if __name__ == "__main__":
    height_map: list[list[int]] = []
    with open("12a.txt") as f:
        for line in f.readlines():
            height_map.append([ord(char) - 96 for char in line.rstrip()])

    min_lengths: list[int] = []
    for row_index, row in enumerate(height_map):
        for col_index, col in enumerate(row):
            if col != 2:
                continue
            nodes: list[list[int]] = [[row_index,col_index]]
            discovered: list[list[int]] = [[row_index,col_index]]
            steps: int = 0
            flag = 0
            while nodes:
                next_level: list[list[int]] = []
                for u in nodes:
                    row, col = u
                    # Check node above.
                    if row >= 1:
                        if [row-1,col] not in discovered and height_map[row-1][col] - height_map[row][col] <= 1:
                            if [row-1,col] not in next_level:
                                next_level.append([row-1,col])
                                discovered.append([row-1,col])
                    # Check node to right.
                    if col < len(height_map[0])-1:
                        if [row,col+1] not in discovered and height_map[row][col+1] - height_map[row][col] <= 1:
                            if [row,col+1] not in next_level:
                                next_level.append([row,col+1])
                                discovered.append([row,col+1])
                    # Check node to left.
                    if col >= 1:
                        if [row,col-1] not in discovered and height_map[row][col-1] - height_map[row][col] <= 1:
                            if [row,col-1] not in next_level:
                                next_level.append([row,col-1])
                                discovered.append([row,col-1])
                    # Check node below.
                    if row < len(height_map)-1:
                        if [row+1,col] not in discovered and height_map[row+1][col] - height_map[row][col] <= 1:
                            if [row+1,col] not in next_level:
                                next_level.append([row+1,col])
                                discovered.append([row+1,col])
                for i in next_level:
                    if height_map[i[0]][i[1]] == 27:
                        flag = 1
                steps += 1
                if flag:
                    min_lengths.append(steps+1)
                    break
                nodes = next_level
    print(min(min_lengths))
"""
Pre-cleaning: Changed the "E" to "{" since that will give an ord of 27 which can be used as an end point.
Notes: Same as part 1, just do it for every starting point and then find the smallest one. However, there are so many "a"s (991) that
it will take a very long time to run. There are a lot less "b"s (41) so we can just use them as a starting point and add +1 for the 
adjacent a. This is safe because all "b"s are adjacent to an a.
If it weren't for this cheesy solution, I don't know if there's a way to do it < 15 seconds.
"""