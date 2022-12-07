"""
Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs to look for messages.

A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.

Here are the first positions of start-of-message markers for all of the above examples:

    mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
    bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
    nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
    nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
    zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26

How many characters need to be processed before the first start-of-message marker is detected?
"""
from typing import Optional


if __name__ == "__main__":
    with open("6a.txt") as f:
        passcode = f.readline()

    marker: Optional[int] = None
    for index in range(len(passcode[:-13])):
        possible_marker = passcode[index: index+14]
        if len(set(possible_marker)) == 14:
            marker = index + 14
            break
    print(marker)
"""
Notes: Same as part 1, runs in O(n * m) where m is the length of the substring (14).
Set look-ups use a hash map so it is O(1) for checking the set.
Usually when the problem is the same as part 1 but longer, the new number is supposed to be too big to efficiently run it naively. 
This ran instantaneously though so I'm not sure what I missed.
"""