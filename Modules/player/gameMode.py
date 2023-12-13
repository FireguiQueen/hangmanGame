def chooseGameMode():
    print("=========== Hangman ============ ")

    print("Choose one of the following options: ")
    print("   1. Choose my own word")
    print("   2. Let the game choose the word")

    while(True):
        playerChoice = int (input("Option >> "))

        if (playerChoice != 1 and playerChoice != 2):
            print("--->> Put '1' or '2'. Number typed: ", playerChoice)
            continue
        return playerChoice