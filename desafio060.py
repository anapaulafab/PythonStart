# leia um numero qualquer e mostre o seu fatorial
numero = int(input('Digite um numero: '))
contador = numero
fatorial = 1
while contador > 0:
    print(f"{contador}", end=" ")
    print(f" x " if contador > 1 else '= ', end=" ")
    fatorial *= contador
    contador-= 1
print(f"{fatorial} ")

    