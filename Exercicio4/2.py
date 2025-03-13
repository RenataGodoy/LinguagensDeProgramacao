# Solicitar ao usuário uma lista de números inteiros
entrada = input("Digite uma lista de números inteiros separados por espaço: ")

# Converter a string de entrada em uma lista de números inteiros
lista = [int(x) for x in entrada.split()]

# Encontrar o maior e o menor número
maior = max(lista)
menor = min(lista)

# Exibir o resultado
print(f'O maior número da lista é: {maior}')
print(f'O menor número da lista é: {menor}')
