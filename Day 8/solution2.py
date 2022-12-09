"""
Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of trees.

To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)

The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.

In the example above, consider the middle 5 in the second row:

30373
25512
65332
33549
35390

    Looking up, its view is not blocked; it can see 1 tree (of height 3).
    Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
    Looking right, its view is not blocked; it can see 2 trees.
    Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height 5 that blocks its view).

A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).

However, you can do even better: consider the tree of height 5 in the middle of the fourth row:

30373
25512
65332
33549
35390

    Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
    Looking left, its view is not blocked; it can see 2 trees.
    Looking down, its view is also not blocked; it can see 1 tree.
    Looking right, its view is blocked at 2 trees (by a massive tree of height 9).

This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.

Consider each tree on your map. What is the highest scenic score possible for any tree?
"""
from typing import List


if __name__ == "__main__":
    rows: List[List[int]] = []
    with open("8a.txt") as f:
        for line in f.readlines():
            line = line.rstrip()
            rows.append([int(x) for x in line])
    EDGE = 99
    # Get the left-visible matrix

    right_matrix: List[int] = [0] * EDGE ** 2
    for row_index in range(len(rows)):
        curr_max = 0
        for col_index in range(len(rows[row_index])):
            right_scenic_score = 0
            for neighbor in range(col_index+1, len(rows[row_index])):
                if neighbor == len(rows[row_index])-1:
                    right_scenic_score += 1
                    right_matrix[row_index * EDGE + col_index] = right_scenic_score
                    break
                if rows[row_index][neighbor] < rows[row_index][col_index]:
                    right_scenic_score += 1
                elif rows[row_index][neighbor] >= rows[row_index][col_index]:
                    right_scenic_score += 1
                    right_matrix[row_index * EDGE + col_index] = right_scenic_score
                    break
            
    left_matrix: List[int] = [0] * EDGE ** 2
    for row_index in range(len(rows)):
        curr_max = 0
        for col_index in range(len(rows[row_index])-1, -1, -1):
            left_scenic_score = 0
            for neighbor in range(col_index-1, -1, -1):
                if neighbor == 0:
                    left_scenic_score += 1
                    left_matrix[row_index * EDGE + col_index] = left_scenic_score
                    break
                if rows[row_index][neighbor] < rows[row_index][col_index]:
                    left_scenic_score += 1
                elif rows[row_index][neighbor] >= rows[row_index][col_index]:
                    left_scenic_score += 1
                    left_matrix[row_index * EDGE + col_index] = left_scenic_score
                    break
    
    bottom_matrix: List[int] = [0] * EDGE ** 2
    for col_index in range(len(rows)):
        curr_max = 0
        for row_index in range(len(rows[col_index])):
            down_scenic_score = 0
            for neighbor in range(row_index+1, len(rows[row_index])):
                if neighbor == len(rows[row_index])-1:
                    down_scenic_score += 1
                    bottom_matrix[row_index * EDGE + col_index] = down_scenic_score
                    break
                if rows[neighbor][col_index] < rows[row_index][col_index]:
                    down_scenic_score += 1
                elif rows[neighbor][col_index] >= rows[row_index][col_index]:
                    down_scenic_score += 1
                    bottom_matrix[row_index * EDGE + col_index] = down_scenic_score
                    break

    top_matrix: List[int] = [0] * EDGE ** 2
    for col_index in range(len(rows)):
        curr_max = 0
        for row_index in range(len(rows[col_index])-1, -1, -1):
            up_scenic_score = 0
            for neighbor in range(row_index-1, -1, -1):
                # print(rows[row_index][col_index], rows[neighbor][col_index])
                if neighbor == 0:
                    up_scenic_score += 1
                    top_matrix[row_index * EDGE + col_index] = up_scenic_score
                    break
                if rows[neighbor][col_index] < rows[row_index][col_index]:
                    up_scenic_score += 1
                elif rows[neighbor][col_index] >= rows[row_index][col_index]:
                    up_scenic_score += 1
                    top_matrix[row_index * EDGE + col_index] = up_scenic_score
                    break

    # # Product or on the 4 lists.
    max_scenic_score = 0
    for i in range(EDGE**2):
        scenic_score = left_matrix[i] * right_matrix[i] * top_matrix[i] * bottom_matrix[i]
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score
    print(max_scenic_score)
"""
Notes: About as clunky as part 1 and can also use some cleaning.
"""