print('-='*10)
print('Sequencia de Fibonacci')
print('-='*10)
n1 = int(input('Digite quantos numeros da sequencia d Fibonacci voce quer: '))
c = 3
t1 = 0
t2 = 1
print(f'{t1} -> {t2} -> ', end ='')
while c <= n1:
    t3 = t1 + t2
    print(f'{t3}', end='')
    print(' -> ' if c != n1 else ' ', end='')
    t1 = t2
    t2 = t3
    c += 1
