frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)

#sem usar o for(fatiamento)
inverso = junto[::-1]

#usando o for
"""inverso = ''
for letra in range (len(junto)-1,-1,-1):
    inverso += junto[letra]"""
print (f'O inverso de {junto} é {inverso} ')
if inverso == junto:
    print ('A frase é um palíndromo')
else:
    print("A frase não é um palíndromo")
