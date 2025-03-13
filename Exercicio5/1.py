# Função para calcular o fatorial de um número
def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

# Programa principal
numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = calcular_fatorial(numero)
print(f"O fatorial de {numero} é: {fatorial}")
