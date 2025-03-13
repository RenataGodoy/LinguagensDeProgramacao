# Função para calcular a média de uma lista de números
def calcular_media(lista):
    return sum(lista) / len(lista)

# Programa principal
entrada = input("Digite números separados por espaço para calcular a média: ")
numeros = [float(x) for x in entrada.split()]
media = calcular_media(numeros)
print(f"A média dos números é: {media}")
