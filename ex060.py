from math import factorial
n1 = int(input('Digite um numero para calcular seu fatorial: '))
c = n1
f = factorial(n1)
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end= '')
    c -= 1
print(f'{f}', end='')