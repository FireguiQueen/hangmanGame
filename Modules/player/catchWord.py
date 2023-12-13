from Modules.other import textStyle
def catchPlayerWord():
    while(True):
        palavra = (str) (input(textStyle.format.BOLD + "Digite uma palavra: " + textStyle.format.NORMAL))
        if (len(palavra) == 0):
            print(textStyle.format.ITALIC + textStyle.format.WARNING +"* Você precisa inserir uma palavra para continuar.." + textStyle.format.NORMAL)
            continue

        return palavra.lower()