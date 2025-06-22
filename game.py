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


def check_game_result_multiple(user_choice: str, computer_choice: str, result_possibilities: dict):
    if user_choice == computer_choice:
        print(f"There is a draw ({user_choice})")
        return 50
    elif computer_choice in result_possibilities[user_choice]["loss"]:
        print(f"Sorry, but the computer chose {computer_choice}")
        return 0
    elif computer_choice in result_possibilities[user_choice]["win"]:
        print(f"Well done. The computer chose {computer_choice} and failed")
        return 100
    return 0


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


def win_situations_from_multiple_options(all_options: list):
    """
    Create dictionary with all possible situation combinations

    :param all_options: options that user specified (list of strings)
    :return: dictionary with keys in sublist 'draw', 'win', and 'loss' that associates with appropriate situations
    """
    all_possibilities = dict()

    for option in all_options:
        replaced_options = all_options[all_options.index(option)+1:] + all_options[:all_options.index(option)]

        all_possibilities[option] = {"draw": option,
                                     "loss": replaced_options[:(len(replaced_options)//2)],
                                     "win": replaced_options[(len(replaced_options)//2):]}
    return all_possibilities


def game_play():

    name = greet_user()
    user_rating = check_initial_rating(name)

    options = input()

    if options:
        options_list = options.split(",") if options else []
        # print(options_list)

        current_inputs = options_list + ["!exit", "!rating"]
        win_loss_options = win_situations_from_multiple_options(options_list)
    else:
        current_inputs = possible_inputs

    print("Okay, let's start")

    while True:

        your_choice = check_user_input(user_choice=input(), data_to_compare=current_inputs)

        if your_choice == "!exit":
            print("Bye!")
            break

        if your_choice == "!rating":
            get_rating(user_rating)
            continue

        if not options:
            computer_choice = random.choice(list(win_situation.keys()))
            user_rating += check_game_result(your_choice, computer_choice)
        else:
            computer_choice = random.choice(options_list)
            user_rating += check_game_result_multiple(user_choice=your_choice, computer_choice=computer_choice, result_possibilities=win_loss_options)


if __name__ == '__main__':
    game_play()
