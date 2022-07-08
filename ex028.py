from random import randint
comp = randint(0, 5) # Faz o computador "PENSAR"
print('-*-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente Advinhar...')
print('-*-' * 20)
jog = int(input('Em que numero eu pensei? '))
if jog == comp:
    print('Parabens você adivinhou o numero')
else:
    print('Você errou!, otário!')
print (f'Pensei no número {comp}')


