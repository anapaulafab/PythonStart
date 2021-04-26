dados=list()
dados.append('Carlos')
dados.append(25)
#----------------
pessoas = list()
pessoas.append(dados[:])
#----------------
pessoas = [['Carlos,25'],['Maria,19']]
print(pessoas[0][0])
print(pessoas[1][1])
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')
#------------------------------
galera = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >=21:
        print(f'{p[0]} é maior de idade.')
    else:
        print(f'{p[0]} é menor de idade')
    
