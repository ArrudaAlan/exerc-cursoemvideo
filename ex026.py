n1 = str(input('Digite uma frese: ')).strip().lower()
print(f'Letra A asparece {n1.count("a")} vezes')
print(f'A primeira letra A apareceu na posição {n1.find("a")+1}')
print(f'A ultima letra A apareceu na posição {n1.rfind("a")+1-n1.count(" ")}')


