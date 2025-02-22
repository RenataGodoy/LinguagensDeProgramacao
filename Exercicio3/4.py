# Solicita dois números inteiros ao usuário e exibe os números ímpares dentro desse intervalo
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))
print("Números ímpares no intervalo:")
for i in range(inicio, fim + 1):
    if i % 2 != 0:
        print(i)