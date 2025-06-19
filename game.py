import random

win_situation = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock",
    }


def fake_computer_win(user_choice: str):
    return f"Sorry, but the computer chose {win_situation.get(user_choice)}"


def check_game_result(user_choice: str, computer_choice: str):
    if user_choice == computer_choice:
        return f"There is a draw ({user_choice})"
    if win_situation.get(user_choice) == computer_choice:
        return f"Sorry, but the computer chose {computer_choice}"
    return f"Well done. The computer chose {computer_choice} and failed"


def check_user_input(user_choice: str, data_to_compare: list):

    data_to_compare = list(data_to_compare) + ["!exit"]

    if user_choice not in data_to_compare:

        while user_choice not in data_to_compare:
            print("Invalid input")
            user_choice = input()

    return user_choice

def game_play():

    while True:

        your_choice = check_user_input(user_choice=input(), data_to_compare=list(win_situation))

        if your_choice == "!exit":
            print("Bye!")
            break

        computer_choice = random.choice(list(win_situation.keys()))
        print(check_game_result(your_choice, computer_choice))


if __name__ == '__main__':
    game_play()