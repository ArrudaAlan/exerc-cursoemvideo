from datetime import date
n1 = int(input('Qual o ano de nascimento do atleta? '))
atual = date.today().year
idade = atual - n1
if idade <= 9:
    print(f'O atleta tem {idade} e está na categoria MIRIM.')
elif idade <= 14:
    print(f'O atleta tem {idade} e está na categoria INFANTIL.')
elif idade <= 19:
    print(f'O atleta tem {idade} e está na categoria JUNIOR.')
elif idade <= 25:
    print(f'O atleta tem {idade} e está na categoria SENIOR.')
elif idade > 25:
    print(f'O atleta tem {idade} e está na categoria MASTER.')
