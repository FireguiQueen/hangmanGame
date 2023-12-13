def findLetter():
    while(True):
        # checkWin ----
        letra = str (input("Digite uma letra: "))

        while len(letra) != 1:
            print("Normal text \x1B[3mitalic text\x1B[0m normal text")
            continue
    i=0 #A variável i vai ser o número da posição letra da palavra
    for i in range(tamanho):  #Procura na palavra pela letra escolhida
        if letra==palavra[i]:
            listaResposta[i]= letra   #Substitui o "_" da lista pela letra certa
            tentativasmax+=1
    print("".join(listaResposta)) #Mostra a lista em forma de string