from datetime import date
n1 = int(input('Digite um ano para saber se é bissexto: '))
if n1 == 0:
    n1 = date.today().year
if n1 % 4 == 0 and n1 % 100 != 0 or n1 % 400 == 0:
    print(f'O ano de {n1} é um ano bissexto')
else:
    print(f'O ano {n1} não é um ano bissexto')
