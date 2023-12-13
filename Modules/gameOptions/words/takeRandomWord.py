from Modules.gameOptions.words import wordList
import random
def randomWord():
    randomNumber = random.randint(0, len(wordList.wordList))
    return wordList.wordList[randomNumber]
