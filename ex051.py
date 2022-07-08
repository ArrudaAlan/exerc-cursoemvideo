print('="'*20)
print('10 TERMOS DE UMA PA')
print('="'*20)
pt = int(input('Primeiro termo: '))
r= int(input('Razão: '))
decimo = pt + (10) * r
for c in range (pt, decimo, r):
    print(f'{c}', end=" ")