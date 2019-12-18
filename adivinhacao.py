import random

def jogar():
    print("*********************************")
    print("Bem vindo no jogo de adivinhação!")
    print("*********************************")
    numero_secreto = random.randrange(1, 101) #round(random.random() * 100) #random() gera entre 0.0 e 1.0
    total_de_tentativas = 0
    pontos = 1000
    pontos_perdidos = 0

    print("Qual nível de dificuldade?")
    print("(1) Fácil  (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

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
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
            elif(maior):
                print("Você errou! O seu chute foi maior que o número secreto!")
            elif(menor): #poderia utilizar else
                print("Você errou! O seu chute foi menor que o número secreto!")
            pontos_perdidos = abs(numero_secreto - chute) #É a diferença entre os pontos
            pontos = pontos - pontos_perdidos

    print("Fim do jogo!")