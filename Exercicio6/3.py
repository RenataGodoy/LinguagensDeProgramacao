# Tupla com as cores do arco-íris
cores = ("rosa", "lilas", "azul bebe", "verde", "amarelo", "anil", "violeta")

# Solicitar ao usuário um número de 1 a 7
numero = int(input("Digite um número de 1 a 7 para saber a cor correspondente ao arco-íris: "))

# Exibir a cor correspondente ao número informado
if 1 <= numero <= 7:
    print(f"A cor correspondente é: {cores[numero - 1]}")
else:
    print("Número inválido. Digite um número entre 1 e 7.")
