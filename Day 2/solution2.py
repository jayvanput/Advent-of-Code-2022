"""
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

    In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
    In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
    In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
"""

if __name__ == "__main__":
    with open("2a.txt") as f:
        rounds = [line.rstrip() for line in f]

    OUTCOMES = {
        "A": 1,
        "B": 2,
        "C": 3
    }
    output = 0
    for round in rounds:
        opp, outcome = round[0], round[2]

        if outcome == "Y":  # Draw
            output += OUTCOMES[opp] + 3
        elif outcome == "X":  # Lose
            if OUTCOMES[opp] == 1:
                output += 3
            else:
                output += OUTCOMES[opp] - 1
        elif outcome == "Z":  # Win
            if OUTCOMES[opp] == 3:
                output += 7
            else:
                output += OUTCOMES[opp] + 7

"""
Notes: IDK if there is a better way to do this, but hard coding the outcomes and then using logic to decide the outcome seems to be the easiest.
"""