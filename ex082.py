list = []
par = []
impar = []
while True:
    list.append(int(input('Digite um número: ')))
    resp = str(input('Dejesa continuar? [S/N]')).upper()
    if resp in 'N':
        break
for i, v in enumerate(list):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('-=' * 30)
print(f'A lista completa é {list}')
print(f'A lista com números pares é {par}')
print(f'A lista com números impares é {impar}')
