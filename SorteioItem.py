import random

a1 = str(input(' Digite o nome do aluno: '))
a2 = str(input(' Digite o nome do aluno: '))
a3 = str(input(' Digite o nome do aluno: '))
a4 = str(input(' Digite o nome do aluno: '))
#alunos = ['Maria', 'João', 'José', 'Augusto']
#lista = [a1, a2, a3, a4]
sorteio = random.choice([a1, a2, a3, a4])
print(f' O aluno escolhido foi: {sorteio}')
