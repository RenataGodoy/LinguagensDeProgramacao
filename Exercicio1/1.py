import math

# Solicita ao usuário o valor do raio
raio = float(input("Digite o valor do raio do círculo: "))

area = math.pi * (raio ** 2)

print(f"A área do círculo com raio {raio} é: {area:.2f}")