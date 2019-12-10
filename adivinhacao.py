print("*********************************")
print("Bem vindo no jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    #print("Tentativa", rodada, "de", total_de_tentativas)
    print("Tentativa {} de {} ".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    #Variáveis para facilitar a legibilidade
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto!")
        elif(menor): #poderia utilizar else
            print("Você errou! O seu chute foi menor que o número secreto!")

        rodada = rodada + 1

print("Fim do jogo!")
