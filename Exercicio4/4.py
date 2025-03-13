# Solicitar ao usuário uma lista de palavras
entrada = input("Digite uma lista de palavras separadas por espaço: ")

# Converter a string de entrada em uma lista de palavras
lista = entrada.split()

# Inverter a lista
lista_invertida = lista[::-1]

# Exibir o resultado
print(f'A lista na ordem inversa é: {lista_invertida}')
