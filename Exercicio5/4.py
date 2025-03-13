# Função para contar as vogais em uma palavra
def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador

# Programa principal
palavra = input("Digite uma palavra para contar as vogais: ")
numero_vogais = contar_vogais(palavra)
print(f"A palavra '{palavra}' tem {numero_vogais} vogais.")
