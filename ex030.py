n1 = int(input('Digite um numero para saber se é PAR ou IMPAR: '))
n2 = n1 % 2
if n2 == 0:
    print(f'O numero {n1} é PAR')
else:
    print(f'O numero {n1} é IMPAR')
