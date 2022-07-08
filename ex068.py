from random import randint
v = 0
while True:
    jog = int(input('Diga um valor: '))
    comp = randint(0, 10)
    total = jog + comp
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou impar? ')).strip().upper()[0]
    print(f'Você jogos {jog} e o computador {comp}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Vence!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Game over! Voce venceu {v} vezes')