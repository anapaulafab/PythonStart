import random
numero = random.randint(a = 0, b = 5)
numUsuario = int(input("Tente descobrir o número de 0 a 5 escolhido: "))
if numUsuario == numero:
    print("Parabéns! Você acertou.")
else:
    print("Você errou. Tente novamente")
