# Solicitar uma frase ao usuário
frase = input("Digite uma frase para contar as palavras: ").lower()

# Dicionário para armazenar a contagem das palavras
contagem_palavras = {}

# Dividir a frase em palavras e contar
palavras = frase.split()
for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

# Exibir o dicionário com a contagem de palavras
print("\nEstatísticas da frase:")
print(contagem_palavras)
