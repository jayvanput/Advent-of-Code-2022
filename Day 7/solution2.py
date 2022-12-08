"""
--- Part Two ---

Now, you're ready to choose a directory to delete.

The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. You need to find a directory you can delete that will free up enough space to run the update.

In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update. Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.

To achieve this, you have the following options:

    Delete directory e, which would increase unused space by 584.
    Delete directory a, which would increase unused space by 94853.
    Delete directory d, which would increase unused space by 24933642.
    Delete directory /, which would increase unused space by 48381165.

Directories e and a are both too small; deleting them would not free up enough space. However, directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.

Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?
"""
from typing import List

class ListNode:

    def __init__(self, key: str, size: int, parent):
        self.key = key
        self.size = size
        self.parent = parent
        self.children:List[ListNode] = []

    def build_size(self):
        dir_size = self.size
        if self.children:
            for child in self.children:
                if child.size:
                    dir_size += child.size
                else:
                    child_size = child.build_size()
                    dir_size += child_size
            self.size = dir_size
        return self.size

if __name__ == "__main__":
    with open("7a.txt") as f:
        lines: List[str] = []
        for line in f.readlines()[1:]:
            if line != "$ ls\n":
                # Remove the $.
                line = line.lstrip("$ ")
                lines.append(line.rstrip())

    root = ListNode("/",0,None)
    current_node = root

    # Build the file system tree.
    for line in lines:
        direction, item = line.split(" ")
        
        # Handle directories.
        if direction == "dir":
            child = ListNode(item, 0, current_node)
            current_node.children.append(child)

        # Handle files with sizes.
        if direction.isnumeric():
            child = ListNode(item, int(direction), current_node)
            current_node.children.append(child)

        # Handle directory changes.
        if direction == "cd":
            # Handle the parent.
            if item == "..":
                current_node = current_node.parent
            else:
                for child in current_node.children:
                    if child.key == item:
                        current_node = child

    # Get directory sizes.
    root.build_size()
    NEEDED_SPACE = 30000000 - (70000000 - root.size)
    candidate_directories = []

    def helper(node):
        if node.children:
            if node.size > NEEDED_SPACE:
                candidate_directories.append(node.size)
            for child in node.children:
                helper(child)

    helper(root)
    print(min(candidate_directories))
"""
Notes: Same as part 1, but we need to figure out how much space was used (the size of the root node), subtract that from 30000000 to find the space we need to remove.
Then we just find the smallest directory above that value.
"""