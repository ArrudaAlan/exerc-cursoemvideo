from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print(''' Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jog = int(input('Qual a sua jogada?'))
print(f'Jogador escolheu {itens[jog]}')
print(f'O computador escolheu {itens[comp]}')
if comp == 0:  # pedra
    if jog == 0:  # pedra
        print('Empatou')
    elif jog == 1:  # papel
        print('O jogador ganhou!')
    elif jog == 2:  # tesoura
        print('O computador ganhou!')
    else:
        print('Opção invalida jogue novamente!')
elif comp == 1:  # papel
    if jog == 0:  # pedra
        print('O computador ganhou!')
    elif jog == 1:  # papel
        print('Empatou')
    elif jog == 2:  # tesoura
        print('O jogador ganhou!')
    else:
        print('Opção invalida jogue novamente!')
elif comp == 2:  # tesoura
    if jog == 0:  # pedra
        print('O jogador ganhou!')
    elif jog == 1:  # papel
        print('O computador ganhou!')
    elif jog == 2:  # tesoura
        print('Empatou')
    else:
        print('Opção invalida jogue novamente!')
