# Função para converter temperatura de Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa principal
temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print(f"A temperatura de {temperatura_celsius}°C é igual a {temperatura_fahrenheit}°F.")
