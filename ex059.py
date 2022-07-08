from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundos Valor: '))
opc = 0
while opc != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opc = int(input('Qual a sua opção? '))
    if opc == 1:
        soma = n1 + n2
        print(f'o resultado da soma é {soma}')
    elif opc == 2:
        mult = n1 * n2
        print(f'O resultado da multiplicação é {mult}')
    elif opc == 3:
        if n1 > n2:
            print(f'O maior número é o {n1}')
        else:
            print((f'O maior número é o {n2}'))
    elif opc == 4:
        print('Informe os números novamente')
        n1 = int(input(' Primeiro Valor: '))
        n2 = int(input(' Segundo Valor: '))
    elif opc == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente')
    print('=-='*10)
    sleep(1)
print('Fim do progroma! Volte sempre!')

