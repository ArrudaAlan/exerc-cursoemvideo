alt = float(input('Largura da parede: '))
larg = float(input('Altura da parede: '))
ar = alt * larg
tint = ar / 2
print(f'Sua parede tem a dimensão de {alt}x{larg} e sua área é de {ar:.2f}m².')
print(f'Para pintar essa parede, você precisará de {tint:.2f}l de tinta.')