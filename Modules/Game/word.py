from Modules.player import gameMode
from Modules.player import catchWord
from Modules.gameOptions.words import takeRandomWord

def word():

    mode = gameMode.chooseGameMode()

    if mode == 1:  # 1 = user chooses his word
        word = list(catchWord.catchPlayerWord())

    else:  # 2 = the game choose the word
        word = list(takeRandomWord.randomWord())

    return word