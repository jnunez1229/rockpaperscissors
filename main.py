from random import randint
import inquirer


def game():
    # User Selection
    userPrompt = [
        inquirer.List('choice',
                      message="Rock, paper, or scissors?",
                      choices=['Rock', 'Paper', 'Scissors'],
                      ),
    ]
    userChoice = inquirer.prompt(userPrompt)

    print(userChoice["choice"])

    # if userChoice == 1 or userChoiceInt > 3 or userChoiceInt == ValueError:
    #     print("you chose paper", userChoiceInt)
    #     game()
    # userScore = 0
    # robotScore = 0
    # robotChoice = randint(1, 3)
    # print(userChoice)


game()
