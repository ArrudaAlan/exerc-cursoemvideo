valor = int(input('Que valor você quer sacar? R$ '))
tot = valor
cedu = 50
totcedu = 0
while True:
    if tot >= cedu:
        tot -= cedu
        totcedu += 1
    else:
        if totcedu > 0:
            print(f'Total de {totcedu} cedulas de R${cedu}')
        if cedu == 50:
            cedu = 20
        elif cedu == 20:
            cedu = 10
        elif cedu == 10:
            cedu = 1
        totcedu = 0
        if tot == 0:
            break