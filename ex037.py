n1 = int(input('Digite um numeoro inteiro: '))
print('Escolha uma das bases para conversão')
print('[ 1 ] Converter para Binario')
print('[ 2 ] Converter para Octal')
print('[ 3 ] Converter para Hexadecimal')
n2 = int(input('Sua opção: '))
if n2 == 1:
    print(f'O numero {n1} em Binario fica {bin(n1)[2:]}')
elif n2 == 2:
    print(f'O numero {n1} em Octal fica {oct(n1)[2:]}')
else:
    print(f'O numero {n1} em Hexadecimal fica {hex(n1)[2:]}')
