from math import fabs
a = int(input('Digite o valor da primeira reta: '))
b = int(input('Digite o valor da segunda reta: '))
c = int(input('Digite o valor da terceira reta: '))
if fabs(b - c) < a < (b + c) and fabs(a - c) < b < (a + c) and fabs(a - b) < c < (a + b):
    print(f'As retas {a}, {b} e {c} formam um triangulo')
    if a != b and b != c and a != c:
        print('Esse triangulo é Escaleno.')
    elif a == b and b == c:
        print('Esse triangulo é Equilatero.')
    else:
        print('Esse triagulo é Isósceles')
else:
    print(f'As retas {a}, {b} e {c} não formam um triangulo')