# Solicitar ao usuário uma lista de números inteiros
entrada = input("Digite uma lista de números inteiros separados por espaço: ")

# Converter a string de entrada em uma lista de números inteiros
lista = [int(x) for x in entrada.split()]

# Calcular a soma dos elementos da lista
soma = sum(lista)

# Exibir o resultado
print(f'A soma dos elementos da lista é: {soma}')
