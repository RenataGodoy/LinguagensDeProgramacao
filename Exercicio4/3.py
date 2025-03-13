# Solicitar ao usuário uma lista de números inteiros
entrada = input("Digite uma lista de números inteiros separados por espaço: ")

# Converter a string de entrada em uma lista de números inteiros
lista = [int(x) for x in entrada.split()]

# Criar uma lista para armazenar os números sem duplicatas, mantendo a ordem
sem_duplicatas = []
for numero in lista:
    if numero not in sem_duplicatas:
        sem_duplicatas.append(numero)

# Exibir o resultado
print(f'A lista sem duplicatas é: {sem_duplicatas}')
