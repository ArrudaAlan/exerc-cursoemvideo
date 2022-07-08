print('-='*10)
print('Gerador de PA')
print('-='*10)
n1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = n1
c = 1
tot = 0
mais = 10
while mais != 0:
    tot += mais
    while c <= tot:
        print(f'{termo} -> ', end='')
        termo += razao
        c += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizando com {tot} termos mostrados')