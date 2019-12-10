print("*********************************")
print("Bem vindo no jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1,total_de_tentativas + 1): #A tentativa é 3, logo adicionar 1 aqui facilita o entendimento
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

print("Fim do jogo!")
