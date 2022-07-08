n1 = float(input('Qual a distancia da sua viagem em km? '))
n2 = n1*0.5 #distancia <= 200km
n3 = n1*0.45 #distancia > 200km
if n1 <= 200:
    print(f'O valor da passagem será de R${n2}')
else:
    print(f'O valor da passagem será de R${n3}')