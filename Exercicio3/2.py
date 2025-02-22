# Solicita números ao usuário até que ele digite um número negativo
# Ao final, exibe a soma de todos os números positivos digitados
soma = 0
while True:
    num = float(input("Digite um número (negativo para sair): "))
    if num < 0:
        break
    soma += num
print(f"A soma dos números positivos digitados é: {soma}")