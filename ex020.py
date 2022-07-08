from random import shuffle
n1 = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Qaurto Aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem de apresentação será: {lista}')