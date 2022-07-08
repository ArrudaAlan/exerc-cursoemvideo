dias = int(input('Por quantos dias o carro foi alugado? '))
vdias = dias * 60
km = float(input('Quantos km foram rodados? '))
vkm = km * 0.15
print(f'O total a pagar é de R${vkm+vdias:.2f}')