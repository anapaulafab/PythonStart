#Erros e exceções
#Exception
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f' Tem um problema {erro.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Fim')
