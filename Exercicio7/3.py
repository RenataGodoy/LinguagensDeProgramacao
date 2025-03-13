# Dicionário com algumas palavras e suas traduções
dicionario = {
    "amor": "love",
    "felicidade": "happiness",
    "amizade": "friendship",
    "planta": "wed",
    "sonho": "dream"
}

# Solicitar uma palavra em português ao usuário
palavra = input("Digite uma palavra em português para traduzir: ").lower()

# Verificar se a palavra está no dicionário e exibir a tradução
if palavra in dicionario:
    print(f"A tradução de '{palavra}' é: {dicionario[palavra]}")
else:
    print("Desculpe, a tradução não foi encontrada!")
