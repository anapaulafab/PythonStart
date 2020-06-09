import math

x = float(input(' Digite o comprimento do cateto oposto: '))
y = float(input(' Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(x , y)
print(f' Este é o comprimento da hipotenusa: {hipotenusa}')
