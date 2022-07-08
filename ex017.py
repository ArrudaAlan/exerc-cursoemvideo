from math import hypot
cop = float(input('Comprimento do cateto oposto: '))
cad = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa de {cop} e {cad} mede {hypot(cop, cad)}m')
