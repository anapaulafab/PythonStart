import random

nomes = str(input(' Digite os nomes dos alunos: '))

#transforma string em lista
nomes2 = nomes.split(',')

#essa função só embaralha a lista
sorteio = random.shuffle(nomes2)

#função sorteio não retorna valor só mexe com os parametros
print(f' O aluno escolhido foi: {nomes2}')
