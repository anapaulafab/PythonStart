ano = int(input(' Digite o ano: '))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print(f' {ano} é Bissexto!')
else: 
    print (f'{ano} não é Bissexto!')