sexo =''
while sexo !='M' and sexo !='F':
    sexo = str(input('Qual o seu sexo ? [M/F]')).upper()
    if sexo!='M' and sexo !='F':
        print('Informe corretamente seu sexo com M ou F')
print(f' Seu sexo é {sexo} ')

