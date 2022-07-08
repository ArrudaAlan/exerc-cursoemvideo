n1 = float(input('Qual o salário atual do funcionario? R$ '))
n2 = n1 * (15/100+1)
print(f'Um funcionário que  ganhava R${n1:.2f}, com 15% de aumento, passa a receber R${n2:.2f}')
print(f'Um aumento real de R${n2-n1:.2f}.')
