n1 = float(input('Qual o valor do produto? R$'))
print('Escolha a forma de pagamento:')
print('[ 1 ] À vista dinheiro.')
print('[ 2 ] À vista cartão.')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão.')
n2 = int(input('Sua opção: '))
if n2 == 1:
    print(f'O valor à vista no dinheiro fica {n1 - (n1 * 10 / 100)}')
elif n2 == 2:
    print(f'O valor à vista no cartão fica {n1 - (n1 * 5 / 100)}')
elif n2 == 3:
    print(f'O valor em 2x no cartão fica {n1}')
elif n2 == 4:
    print(f'O valor em 3x ou mais no cartão fica {n1 + (n1 * 20 / 100)}')
else:
    print('Opção invalida, tente novamente!')
