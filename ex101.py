def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos não vota.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos voto é opcional'
    else:
        return f'Com {idade} anos voto é obrigatório'

nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))