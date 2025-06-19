import random

win_situation = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock",
    }

possible_inputs = {"rock", "paper", "scissors", "!exit", "!rating"}


def fake_computer_win(user_choice: str):
    return f"Sorry, but the computer chose {win_situation.get(user_choice)}"


def check_game_result(user_choice: str, computer_choice: str):
    if user_choice == computer_choice:
        print(f"There is a draw ({user_choice})")
        return 50
    if win_situation.get(user_choice) == computer_choice:
        print(f"Sorry, but the computer chose {computer_choice}")
        return 0
    print(f"Well done. The computer chose {computer_choice} and failed")
    return 100


def check_user_input(user_choice: str, data_to_compare: list | set | tuple):

    if user_choice not in data_to_compare:

        while user_choice not in data_to_compare:
            print("Invalid input")
            user_choice = input()

    return user_choice

def greet_user():
    name = input("Enter your name: ")
    print(f"Hello, {name}")
    return name

def check_initial_rating(user_name: str):
    with open("rating.txt", "r") as ratings_file:
        for line in ratings_file:
            if user_name in line:
                return int(line.strip().split()[-1])
        return 0

def get_rating(rating):
    print(f"Your rating: {rating}")

def game_play():

    name = greet_user()
    user_rating = check_initial_rating(name)

    while True:

        your_choice = check_user_input(user_choice=input(), data_to_compare=possible_inputs)

        if your_choice == "!exit":
            print("Bye!")
            break

        if your_choice == "!rating":
            get_rating(user_rating)
            continue

        computer_choice = random.choice(list(win_situation.keys()))
        user_rating += check_game_result(your_choice, computer_choice)


if __name__ == '__main__':
    game_play()