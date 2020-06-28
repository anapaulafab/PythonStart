precoNormal = float(input(' Digite o preço normal: '))
formaPagamento = int (input('''Digite a condição de pagamento:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Digite: '''))
if formaPagamento == 1:
    print(f'10% desconto: {precoNormal-precoNormal*10/100:.2f}')
elif formaPagamento == 2:
    print(f'5% de desconto: {precoNormal-precoNormal*5/100:.2f}')
elif formaPagamento == 3:
    print(f' Preço normal {precoNormal:.2f}')
elif formaPagamento == 4:
    print(f'com juros: {precoNormal+precoNormal*20/100:.2f}')

