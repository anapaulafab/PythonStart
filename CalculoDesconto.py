#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

n = float(input(' Qual o valor do produto? R$ '))
print (f' O valor do produto com 5% de desconto é de R$ {n-n*5/100:.2f}')
