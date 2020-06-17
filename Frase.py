frase = str(input(' Digite a Frase: ')).upper().strip()
print(f' Letra "A" aparece: {frase.count("A")} vezes \n \
A primeira letra "A" está na posição: {frase.find("A")}\n \
A última letra "A" está na posição: {frase.rfind("A")}')
