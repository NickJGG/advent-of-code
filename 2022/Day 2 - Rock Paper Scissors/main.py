ROCK, LOSS = 0, 0
PAPER, DRAW = 1, 1
SCISSORS, WIN = 2, 2

WINNERS = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER
}

SHAPE_SCORE = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3
}

RESULT_SCORE = {
    WIN: 6,
    DRAW: 3,
    LOSS: 0
}

def part_one():
    lines = read_file()
    total_score = 0

    for line in lines:
        if not line:
            break
            
        opponent_choice, my_choice = read_choices(line)

        total_score += SHAPE_SCORE[my_choice]

        if my_choice == opponent_choice:
            total_score += RESULT_SCORE[DRAW]
        elif WINNERS[my_choice] == opponent_choice:
            total_score += RESULT_SCORE[WIN]
    
    print(f"1. Your total score is { total_score }")

def part_two():
    lines = read_file()
    total_score = 0

    for line in lines:
        if not line:
            break
            
        opponent_choice, desired_result = read_choices(line)
        
        if desired_result == WIN:
            for shape, beats in WINNERS.items():
                if beats == opponent_choice:
                    my_choice = shape

                    break
        elif desired_result == LOSS:
            my_choice = WINNERS[opponent_choice]
        else:
            my_choice = opponent_choice

        total_score += SHAPE_SCORE[my_choice] + RESULT_SCORE[desired_result]
    
    print(f"2. Your total score is { total_score }")

def read_choices(line):
    opponent_choice, my_choice = line.split(" ")
    opponent_choice = ord(opponent_choice) - ord("A")
    my_choice = ord(my_choice) - ord("X")

    return opponent_choice, my_choice

def read_file():
    file = open("input.txt", "r")
    all_text = file.read()
    lines = all_text.split("\n")

    return lines

if __name__ == "__main__":
    part_one()
    part_two()
