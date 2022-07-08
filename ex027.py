n1 = str(input('Digite o seu nome completo: ')).strip()
separa = n1.split()
print(f'O seu primeiro nome é {separa[0]}')
print(f'O seu ultimo nome é {separa[len(separa)-1]}')
