import math

# Solicita ao usuário o valor do raio
raio = float(input("Digite o valor do raio do círculo: "))

# Calcula a área do círculo
area = math.pi * (raio ** 2)

# Exibe o resultado
print(f"A área do círculo com raio {raio} é: {area:.2f}")