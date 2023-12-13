def catchPlayerWord():
    while(True):
        palavra = (str) (input("Digite uma palavra: "))
        if (len(palavra) == 0):
            print("Você precisa inserir uma palavra para continuar..")
            continue
        return palavra.lower()