n1 = float(input('Qual é o salario do funcionario? R$'))
if n1 <= 1250:
    print(f'O salario do funcionario vai de {n1} para {n1+(n1*15/100):.2f}')
else:
    print(f'O salario do funcionario vai de {n1} para {n1+(n1*10/100):.2f}')
