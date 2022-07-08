n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'Sua média foi {media}, você está REPROVADO!')
elif media < 7:
    print(f'Sua media foi {media}, você está em RECUPERAÇÃO!')
elif media >= 7:
    print(f'Sua media foi {media}, você está APROVADO!')
