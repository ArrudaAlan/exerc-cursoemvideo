n1 = float(input('Qual o valor do imovel? '))
n2 = float(input('Qual o salário do comprador? '))
n3 = int(input('Deseja pagar em quantos anos? '))
prest = n1 / (n3*12)
valprestsal = n2 * 30 / 100

if prest > valprestsal:
    print(f'Emprestimo negado, prestação acima de 30% do salario.')
else:
    print(f'Emprestimo aprovado!')


print(f'O valor da prestação será de {prest:.2f}.')