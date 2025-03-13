# Armazenar informações do produto em uma tupla
produto = ("Anel de prata", 79.99, 55)  # Nome, preço, quantidade em estoque

# Exibir os dados formatados
nome, preco, quantidade = produto
print(f"Nome do produto: {nome}")
print(f"Preço: R${preco:.2f}")
print(f"Quantidade em estoque: {quantidade}")
