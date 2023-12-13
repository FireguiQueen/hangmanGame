from Modules.other import textStyle

def chooseGameMode():
    print(textStyle.format.BOLD + "============= Hangman ============== " +textStyle.format.NORMAL)

    print(textStyle.color.GREEN + "Choose one of the following options: ")
    print("   1. Choose my own word")
    print("   2. Let the game choose the word")

    while(True):
        playerChoice = str (input(textStyle.color.GRAY + "Option: "))

        if (playerChoice != '1' and playerChoice != '2'):
            print(textStyle.format.WARNING + "type either '1' or '2' \n* Number typed: ", playerChoice + textStyle.format.NORMAL)
            continue
        return int(playerChoice)

chooseGameMode()