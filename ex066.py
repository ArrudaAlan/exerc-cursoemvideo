n1 = cont = soma = 0
while True:
    n1 = int(input('Digite um numero [999 para parar]: '))
    if n1 == 999:
        break
    soma += n1
    cont += 1
print(f'Você digitou {cont} numeros e a soma entre eles foi {soma}')