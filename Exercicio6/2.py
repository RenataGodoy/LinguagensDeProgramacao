# Solicitar ao usuário quatro números inteiros
numeros = tuple(int(input(f"Digite o número {i+1}: ")) for i in range(4))

# Quantas vezes o número 9 apareceu na tupla
quantidade_9 = numeros.count(9)

# Posição do primeiro número 3 (se existir)
if 3 in numeros:
    posicao_3 = numeros.index(3)
else:
    posicao_3 = -1  # Caso o número 3 não exista

# Números pares
pares = [num for num in numeros if num % 2 == 0]

# Exibir os resultados
print(f"O número 9 apareceu {quantidade_9} vez(es).")
if posicao_3 != -1:
    print(f"O primeiro número 3 foi digitado na posição {posicao_3}.")
else:
    print("O número 3 não foi digitado.")
print(f"Números pares na tupla: {pares}")
