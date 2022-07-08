n1 = int(input('Qual é a velocidade atual do carro? '))
multa = (n1-80)*7
if n1 < 81:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite de velocidade pertido de 80 km/h')
    print(f'Você deve pagar uma multa de {multa} reais')
