print('-='*10)
print('Gerador de PA')
print('-='*10)
n1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = n1
c = 1
while c <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    c += 1
print('Fim')