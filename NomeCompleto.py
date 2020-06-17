nome = str(input(" Digite o nome completo: "))
nomeSemEspaco = nome.replace(" ","")
PrimeiroNome = nome.split()[0]
print(f' Nome em Maiúsculo: {nome.upper()}\n O nome em minúscula: {nome.lower()} \n Quantidade de letras: {len(nomeSemEspaco)}\n \
Letras do 1º nome: {len(PrimeiroNome)}')
