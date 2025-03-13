def conversao_entrada():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            print(f"O dobro do número é: {numero * 2}")
            break  # Se a conversão for bem-sucedida, sai do loop
        except ValueError:
            print("Erro: Você deve digitar um número inteiro válido!")

# Chamar a função
conversao_entrada()
