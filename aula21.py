#Funções #interactive help #docstrings #Argumentos opcionais
#Escopo de variáveis # Retorno de resultados

 #interactive help
# help() colocar no terminal e quit para sair

#docstrings
def contador(i,f,p):
    """
    Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem 
    :param p: passo da contagem
    :retur : sem retorno
    """
    
    c = 1
    while c<= f:
        print(f'{c}')
        c += p
    print('fim')


contador(0,100,10)

#Parametros opcionais

def somar(a=0,b=0,c=0):
    s=a+b+c
    print(f'A soma vale {s}')


    somar(8,4)

#Escopo de variáveis
def teste():
    global n #pra usar a variavel global
    n=4
    x=8 #variável local
    print(f' na função teste, n vale {n}')
    print(f'{x}')


n=2 #variável global 
print(f'n vale {n}')
#variavel local nao funciona em escopo global

#retornando valores
def somar(a=0,b=0,c=0):
    s=a+b+c
    return s


resposta1 = somar(8,4,7)

print(somar(8,4,7))
print(f'A resposta é {resposta1}')
