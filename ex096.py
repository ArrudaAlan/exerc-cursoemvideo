def area(n1, n2):
    a = n1 * n2
    print(f'A área do terreno é do {a}m²')


print('Controle de Terrenos')
print('-' * 20)
n1 = float(input('Largura (m): '))
n2 = float(input('Comprimento (m): '))
area(n1, n2)