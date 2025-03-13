# Solicitar ao usuário uma lista de números inteiros
entrada = input("Digite uma lista de números inteiros separados por espaço: ")

# Converter a string de entrada em uma lista de números inteiros
lista = [int(x) for x in entrada.split()]

# Solicitar ao usuário um número específico para contar suas ocorrências
numero = int(input("Digite o número que deseja contar na lista: "))

# Contar quantas vezes o número aparece na lista
ocorrencias = lista.count(numero)

# Exibir o resultado
print(f'O número {numero} aparece {ocorrencias} vez(es) na lista.')
