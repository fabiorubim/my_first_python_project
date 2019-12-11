import random

print("*********************************")
print("Bem vindo no jogo de adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101) #round(random.random() * 100) #random() gera entre 0.0 e 1.0
total_de_tentativas = 3

for rodada in range(1,total_de_tentativas + 1): #A tentativa é 3, logo adicionar 1 aqui facilita o entendimento
    print("Tentativa {} de {} ".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    #Variáveis para facilitar a legibilidade
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto!")
        elif(menor): #poderia utilizar else
            print("Você errou! O seu chute foi menor que o número secreto!")

print("Fim do jogo!")