import random


def Rules():
    return "Rock => Scissors\n" \
           "Scissors => Paper\n" \
           "Paper => Rock"


def gameProgress(compChoice, playerChoice):
    if compChoice == 1 and playerChoice == 1:
        print('\nRock vs Rock\n\tDraw')
        return "Draw"
    elif compChoice == 1 and playerChoice == 2:
        print('\nRock vs Scissors\n\tThe computer won')
        return "The computer won"
    elif compChoice == 1 and playerChoice == 3:
        print('\nRock vs Paper\n\tThe player won')
        return "The player won"

    elif compChoice == 2 and playerChoice == 1:
        print('\nScissors vs Rock\n\tThe player won')
        return "The player won"
    elif compChoice == 2 and playerChoice == 2:
        print('\nScissors vs Scissors\n\tDraw')
        return "Draw"
    elif compChoice == 2 and playerChoice == 3:
        print('\nScissors vs Paper\n\tThe computer won')
        return "The computer won"

    elif compChoice == 3 and playerChoice == 1:
        print('\nPaper vs Rock\n\tThe computer won')
        return "The computer won"
    elif compChoice == 3 and playerChoice == 2:
        print('\nPaper vs Scissors\n\tThe player won')
        return "The player won"
    elif compChoice == 3 and playerChoice == 3:
        print('\nPaper vs Paper\n\tDraw')
        return "Draw"


def counter(CompResult, PlayerResult):
    print(f"\nThe end result of the computer: {CompResult}\n"
          f"The end result of the player: {PlayerResult}")

    if PlayerResult > CompResult:
        return "Player win"
    elif CompResult > PlayerResult:
        return "Computer win"
    else:
        return "Draw"


loop = True

while loop:
    choices = input(
        "\ntype \"1\" if u are ready to play.\t \"Rules\" if u dont know how to play.\t \"0\" if u want to quit the game: ")

    if choices.title() == "Rules":
        print(Rules())
    if choices == '0':
        print('\nThanks for playing. See u next time <3')
        break

    if choices == '1':
        PlayerFinalResult = 0
        ComputerFinalResult = 0
        gameRound = 0
        while gameRound < 3:

            playerChoice = int(input("\ntype \"1\" if u choice Rock\n"
                                     "type \"2\" if u choice Scissors\n" 
                                     "type \"3\" if u choice Paper: "))

            compChoice = random.randint(1, 3)
            result = gameProgress(compChoice, playerChoice)

            if result == "Draw":
                PlayerFinalResult += 0
                ComputerFinalResult += 0
            elif result == "The computer won":
                ComputerFinalResult += 1
            else:
                PlayerFinalResult += 1

            if gameRound == 2:
                print(counter(ComputerFinalResult, PlayerFinalResult))

            gameRound += 1