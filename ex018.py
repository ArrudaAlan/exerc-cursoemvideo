from math import cos, sin, tan, radians
n1 = float(input('Digite o angulo que você deseja: '))
print(f'O angulo de {n1} tem o seno de {sin(radians(n1)):.2f}')
print(f'O angulo de {n1} tem o cosseno de {cos(radians(n1)):.2f}')
print(f'O angulo de {n1} tem a tangente de {tan(radians(n1)):.2f}')
