"""
--- Day 12: Hill Climbing Algorithm ---

You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation of your current square; that is, if your current elevation is m, you could step to elevation n, but not to elevation o. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^

In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). The location that should get the best signal is still E, and . marks unvisited squares.

This path reaches the goal in 31 steps, the fewest possible.

What is the fewest steps required to move from your current position to the location that should get the best signal?
"""
if __name__ == "__main__":
    height_map: list[list[int]] = []
    with open("12a.txt") as f:
        for line in f.readlines():
            height_map.append([ord(char) - 96 for char in line.rstrip()])

    nodes: list[list[int]] = [[0,0]]
    discovered: list[list[int]] = [[0,0]]
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
        print(next_level)
        for i in next_level:
            print(i, height_map[i[0]][i[1]])
            if height_map[i[0]][i[1]] == 27:
                flag = 1
        if flag:
            break
        nodes = next_level
        steps += 1
    print(steps-1)
"""
Pre-cleaning: Changed the "E" to "{" since that will give an ord of 27 which can be used as an end point.
Notes: Had to go and learn graph traversal for this. BFS is pretty easy to implement at least.
"""