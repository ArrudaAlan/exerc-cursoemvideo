from random import randint
comp = randint(0,10) # Faz o computador "PENSAR"
print('-*-' * 20)
print('Vou pensar em um numero entre 0 e 10. Tente Advinhar...')
print('-*-' * 20)
acertou = False
palpites = 0
while not acertou:
    jog = int(input('Em que numero eu pensei? '))
    palpites += 1
    if jog == comp:
        acertou = True
    else:
        if jog < comp:
            print('Mais... tente novamente')
        elif jog > comp:
            print('Menos... Tente novamente')
print(f'Acertou com {palpites} tentativas')
