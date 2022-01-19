from random import randint
import inquirer


def game():
    def user_selection():
        # User Selection
        user_prompt = [
            inquirer.List('choice',
                          message="Rock, paper, or scissors?",
                          choices=['Rock', 'Paper', 'Scissors'],
                          ),
        ]
        user_choice = inquirer.prompt(user_prompt)

        # User answer is saved as a dict. Must convert to string
        return str(user_choice['choice'])

    def robot_selection():
        # Robot Selection
        random_generator = randint(1, 3)
        robot_choice = ''

        if random_generator == 1:
            robot_choice += 'Rock'
        elif random_generator == 2:
            robot_choice += 'Paper'
        elif random_generator == 3:
            robot_choice += 'Scissors'

        return robot_choice

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

    def play_round():
        user_score = 0
        robot_score = 0

        user_choice = user_selection()
        robot_choice = robot_selection()

        print("Robot chooses - " + robot_choice)

        if user_choice == robot_choice:
            print("Tie. No points")
            play_round()
        elif (user_choice == "Rock" and robot_choice == "Scissors") or (
                user_choice == "Paper" and robot_choice == "Rock") or (
                user_choice == "Scissors" and robot_choice == "Paper"):
            print(user_choice + " beats " + robot_choice + "! You win this round! ")
            user_score += 1

            print("Your score: " + str(user_score))
            print("Robot's score: " + str(robot_score))

            play_round()
        else:
            print(robot_choice + " beats " + user_choice + ". You lose this round ")
            robot_score += 1

            print("Your score: " + str(user_score))
            print("Robot's score: " + str(robot_score))

            play_round()

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
