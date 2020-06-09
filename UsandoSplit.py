import random

a1 = str(input(' Digite os nomes dos alunos: '))
#transforma string em lista
a2 = a1.split(',')

sorteio = random.choice(a2)
print(f' O aluno escolhido foi: {sorteio}')
