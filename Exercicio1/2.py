import math

# Solicita ao usuário a temperatura em Celsius
temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32

print(f"A temperatura {temperatura_celsius}°C em Fahrenheit é: {temperatura_fahrenheit:.2f}°F")