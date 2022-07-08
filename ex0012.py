n1 = float(input('Qual o valor do produto?'))
d = int(input('Qual o valor do desconto? '))
n2 = (n1 * ((d/100)-1)*-1)
print(f'O produto que custava R${n1}, na promoção com desconto de {d}% irá custar R${n2:.2f}')
