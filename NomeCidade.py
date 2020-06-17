Cidade = str(input(' Digite o nome da cidade: ')).upper()
Primeiro = Cidade.split()[0]
print(f' A cidade começa com "SANTO" ?  {"SANTO" in Primeiro}')

Cidade = str(input(' Digite o nome da cidade: ')).strip()
print(f' A cidade começa com "SANTO" ?  {Cidade[:5].upper() == "SANTO"}')
