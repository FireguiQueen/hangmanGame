from Modules.other import textStyle
import string

def catchPlayerWord():
    while(True):
        word = (str) (input(textStyle.format.BOLD + "Type a word: " + textStyle.format.NORMAL))

        if (len(word) == 0):
            print(textStyle.format.WARNING + "You need to type at least one word" + textStyle.format.NORMAL)
            continue

        all_special_characters = [char for char in string.printable if not char.isalnum() and char not in string.whitespace]
        for x in all_special_characters:
            if (x in word):
                print(textStyle.format.WARNING + "Don't use special characters" + textStyle.format.NORMAL)
                catchPlayerWord()
                break

        return word.lower()

catchPlayerWord()