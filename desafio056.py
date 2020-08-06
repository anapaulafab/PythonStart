somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ""
mulher20 = 0
for pessoa in range (1,5):
    print (f"===== {pessoa}ª PESSOA =====")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F]: ")).strip()
    somaidade+=idade
    if pessoa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
mediaidade = somaidade/4
print(f"A media de idade do grupo é de {mediaidade}")
print(f"O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}")
print(f"São {mulher20} mulheres com menos de 20 anos")
