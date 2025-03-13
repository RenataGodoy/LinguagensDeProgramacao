# Dicionário com códigos de produtos, nomes e preços
catalogo = {
    101: ("Brinco de Pérola", 29.99),
    102: ("Pulseira de Coração", 49.90),
    103: ("Colar de Estrela", 79.50),
    104: ("Anel de Prata", 120.00)
}

# Solicitar ao usuário um código de produto para buscar
codigo = int(input("Digite o código do produto para buscar: "))

# Verificar se o código existe no catálogo e exibir as informações
if codigo in catalogo:
    nome, preco = catalogo[codigo]
    print(f"Produto: {nome}\nPreço: R${preco:.2f}")
else:
    print("Produto não encontrado!")
