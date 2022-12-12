"""
--- Part Two ---

It seems like the X register controls the horizontal position of a sprite. Specifically, the sprite is 3 pixels wide, and the X register sets the horizontal position of the middle of that sprite. (In this system, there is no such thing as "vertical position": if the sprite's horizontal position puts its pixels where the CRT is currently drawing, then those pixels will be drawn.)

You count the pixels on the CRT: 40 wide and 6 high. This CRT screen draws the top row of pixels left-to-right, then the row below that, and so on. The left-most pixel in each row is in position 0, and the right-most pixel in each row is in position 39.

Like the CPU, the CRT is tied closely to the clock circuit: the CRT draws a single pixel during each cycle. Representing each pixel of the screen as a #, here are the cycles during which the first and last pixel in each row are drawn:

Cycle   1 -> ######################################## <- Cycle  40
Cycle  41 -> ######################################## <- Cycle  80
Cycle  81 -> ######################################## <- Cycle 120
Cycle 121 -> ######################################## <- Cycle 160
Cycle 161 -> ######################################## <- Cycle 200
Cycle 201 -> ######################################## <- Cycle 240

So, by carefully timing the CPU instructions and the CRT drawing operations, you should be able to determine whether the sprite is visible the instant each pixel is drawn. If the sprite is positioned such that one of its three pixels is the pixel currently being drawn, the screen produces a lit pixel (#); otherwise, the screen leaves the pixel dark (.).

The first few pixels from the larger example above are drawn as follows:

Render the image given by your program. What eight capital letters appear on your CRT?
"""
from typing import List

def drawn_pixels(cycle: int, sprite_positions: List[int]) -> str:
    if (cycle % 40) in sprite_positions:
        return "#"
    else:
        return "."

if __name__ == "__main__":
    instructions: List[str] = []
    with open("10a.txt") as f:
        for line in f.readlines():
            instructions.append(line.rsplit()[0])

    pixels: List[str] = []
    cycle = 0
    sprite_positions: List[int] = [0,1,2]
    for instruction in instructions:
        if instruction == "noop":
            # Only cycle changes, we can use the same sprite positions.
            pixels.append(drawn_pixels(cycle, sprite_positions))
            cycle += 1
        else:
            pixels.append(drawn_pixels(cycle, sprite_positions))
            cycle += 1
            pixels.append(drawn_pixels(cycle, sprite_positions))
            cycle += 1
            sprite_positions = [x + int(instruction) for x in sprite_positions]
    for i in range(0,len(pixels),40):
        print("".join(pixels[i:i+40]))
"""
Pre-cleaning: Some preprocessing was done to make the instructions easier to work with:
- Remove addx since it doesn't add any value.
Really enjoyed this one. Same as previous problem we are just doing different directions during each cycle.

###..#..#..##..#..#.#..#.###..####.#..#.
#..#.#..#.#..#.#.#..#..#.#..#.#....#.#..
#..#.#..#.#..#.##...####.###..###..##...
###..#..#.####.#.#..#..#.#..#.#....#.#..
#.#..#..#.#..#.#.#..#..#.#..#.#....#.#..
#..#..##..#..#.#..#.#..#.###..####.#..#.
"""