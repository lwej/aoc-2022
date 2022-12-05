rock = 1
paper = 2
scissors = 3

lose = 0
draw = 3
win = 6


def calculate_score(player1, player2):
    game_score = 0
    points = player2
    if player1 == player2:
        game_score = draw
    if player1 == 1:
        if player2 == 2:
            game_score = win
        elif player2 == 3:
            game_score = lose
    elif player1 == 2:
        if player2 == 1:
            game_score = lose
        elif player2 == 3:
            game_score = win
    elif player1 == 3:
        if player2 == 1:
            game_score = win
        elif player2 == 2:
            game_score = lose

    return game_score + points


def calc_secret_score(player1, player2):
    game_score = 0
    points = 0

    if player1 == 1:
        if player2 == 1:
            game_score = lose
            points = scissors
        elif player2 == 2:
            game_score = draw
            points = rock
        elif player2 == 3:
            game_score = win
            points = paper
    elif player1 == 2:
        if player2 == 1:
            game_score = lose
            points = rock
        elif player2 == 2:
            game_score = draw
            points = paper
        elif player2 == 3:
            game_score = win
            points = scissors
    elif player1 == 3:
        if player2 == 1:
            game_score = lose
            points = paper
        elif player2 == 2:
            game_score = draw
            points = scissors
        elif player2 == 3:
            game_score = win
            points = rock

    return game_score + points


def interpret_chars(p_choice):
    if p_choice == 'A' or p_choice == 'X':
        p_choice = 1
    elif p_choice == 'B' or p_choice == 'Y':
        p_choice = 2
    elif p_choice == 'C' or p_choice == 'Z':
        p_choice = 3

    return p_choice


with open("input", "r") as f:
    lines = f.readlines()
    score = 0
    for line in lines:
        p1 = interpret_chars(line[0])
        p2 = interpret_chars(line[2])
        # score += calc_secret_score(p1, p2)
        score += calculate_score(p1, p2)


print(f"Answer: {score}")
