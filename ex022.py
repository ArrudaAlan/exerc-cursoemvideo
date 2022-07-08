n1 = str(input('Digite seu nome completo: ')).strip()
print('Estamos analisando seu nome...')
print(f'Seu nome em maiusculas é {n1.upper()}')
print(f'Seu nome em minusculo é {n1.lower()}')
n2 = (len(n1) - n1.count(' '))
print(f'Seu nome tem ao todo {n2} letras')
#print(f'Seu primeiro nome tem {n1.find(" ")}')
separa = n1.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')




