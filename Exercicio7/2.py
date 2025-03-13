# Solicitar uma palavra ao usuário
palavra = input("Digite uma palavra para contar os caracteres: ")

# Dicionário para armazenar a contagem de cada caractere
contagem = {}

# Contar a ocorrência de cada caractere
for char in palavra:
    if char in contagem:
        contagem[char] += 1
    else:
        contagem[char] = 1

# Exibir o dicionário com a contagem
print("\nContagem de caracteres na palavra:")
print(contagem)
