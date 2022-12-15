def task1(players):
    """
    * Variables
    * A / X: ROCK
    * B / Y: PAPER
    * C / Z: Scissors
    """
    moves = {"X": "A", "Y": "B", "Z": "C"}
    points = {"X": 1, "Y": 2, "Z": 3}
    if (players[0] == "A" and moves[players[1]] == "B"
        or players[0] == "B" and moves[players[1]] == "C" 
        or players[0] == "C" and moves[players[1]] == "A"):
        return 6 + points[players[1]]
    elif players[0] == moves[players[1]]:
        return 3 + points[players[1]]
    else:
        return points[players[1]]

def task2(players):
    """
    * Variables
    * A: ROCK       X: Lose
    * B: PAPER      Y: Draw
    * C: SCISSORS   Z: Win
    """
    draw = {"A": 4, "B": 5, "C": 6}
    win = {"A": 8, "B": 9, "C": 7}
    lose = {"A": 3, "B": 1, "C": 2}
    if players[1] == "X":
        return lose[players[0]]
    elif players[1] == "Y":
        return draw[players[0]]
    else:
        return win[players[0]]


def get_points():
    with open('day_2_input.txt', 'r') as f:
        rounds = f.readlines()
    points_task1, points_task2 = 0, 0
    for round in rounds:
        points_task1 += task1(round.strip().split(" "))
        points_task2 += task2(round.strip().split(" "))
    print(points_task1, points_task2)

if __name__ == "__main__":
    get_points()
# end main