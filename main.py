from random import randint
import inquirer


def game():
    # score
    user_score = 0
    robot_score = 0

    def play_round():
        # User Selection
        user_prompt = [
            inquirer.List('choice',
                          message="Rock, paper, or scissors?",
                          choices=['Rock', 'Paper', 'Scissors'],
                          ),
        ]
        user_choice = inquirer.prompt(user_prompt)

        # Robot Selection
        random_generator = randint(1, 3)
        robot_choice = ''

        if random_generator == 1:
            robot_choice += 'Rock'
        elif random_generator == 2:
            robot_choice += 'Paper'
        elif random_generator == 3:
            robot_choice += 'Scissors'

        print('Hello' + robot_choice)

    # User chooses if they want to continue after conclusion of game
    def replay():
        user_prompt = [
            inquirer.List('choice',
                          message="Want to play again?",
                          choices=['Yes', 'No'],
                          ),
        ]
        willReplay = inquirer.prompt(user_prompt)

        if willReplay == 'Yes':
            game()
        else:
            print('Ok, Thanks for playing!')

    # After overall winner decided
    if user_score > 3:
        print("You win the game!!")
        user_score = 0
        robot_score = 0
        replay()
    elif robot_score > 3:
        print("You lose =(")
        user_score = 0
        robot_score = 0
        replay()
    play_round()


game()
