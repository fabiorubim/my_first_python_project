print("Tentativa {1} de {0}".format(3,10))

print("R${}".format(1.59))

print("R${:f}".format(1.59)) #f indica que é um float

print("R${:.2f}".format(1.5)) #f indica que é um float dom duas casas decimais

print("R${:.2f}".format(1234.5))

print("R${:7.2f}".format(1234.5)) #7 caracteres no total, sendo 2 casas decimais

print("R${:7.2f}".format(4.5)) #7 caracteres no total, sendo 2 casas decimais  -adiciona espaços antes

print("R${:07.2f}".format(4.5)) #7 caracteres no total, sendo 2 casas decimais  -adiciona zeros antes

print("R${:08.3f}".format(4.5)) #7 caracteres no total, sendo 2 casas decimais  -adiciona zeros antes

print("R${:07d}".format(4)) #é possível utilizar com inteiros