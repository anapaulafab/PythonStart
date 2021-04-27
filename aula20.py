#Funções
def mostraLinha():
    print('--------------------------')


mostraLinha()
print('Título')
mostraLinha()
#####
def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


título('Titulo 1')
título('Título 2')
título('Título 3')
########
def soma (a,b):
    s=a+b
    print(s)


soma (4,5)
#####
def contador(*núm):
    tam=len(núm)
    print(f'{núm} tem {tam} números')


contador(2,1,7)
contador(0,1)
contador(1,2,3,4)
#######
