from datetime import date
n1 = int(input('Digite o ano de seu nascimento: '))
atual = date.today().year
idade = atual - n1
print(f"Quem nasceu em {n1} tem {idade} anos")
if idade < 18:
    print(f'Você deve se alistar em {18 - idade} anos')
elif idade == 18:
    print(f'Você deve se alistar imediatamente!')
elif idade > 18:
    print(f'Você se alistou há {idade - 18} anos.')
