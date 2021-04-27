#Tuplas = () ; Listas = [] e Dicionário = {}
dados = dict()
dados = {'nome': 'João','idade': 25}
print(dados['nome'])
# inserir 
dados['profissão']='Médico'
#apagar
del dados['idade']
#mostrar
print(dados.values())
print(dados.keys())
print(dados.items())
for k,v in dados.items():
    print(f'O {k} é {v}')

###################################

pessoas = {'nome': 'Ana','sexo': 'F', 'idade': 27}
print(f'O{pessoas["nome"]} tem {pessoas["idade"]} anos')
#
print(pessoas.items())
#
for k,v in pessoas.items():
    print(f'{k} = {v}')
#######
brasil = []
estado1 = {'uf':'Paraná', 'sigla': 'PR'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)

