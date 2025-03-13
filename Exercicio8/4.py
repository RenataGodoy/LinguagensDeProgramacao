def acessar_elemento_lista():
    lista = [10, 20, 30, 40, 50]  # Lista com 5 números
    try:
        indice = int(input("Digite o índice (0-4) para acessar um valor da lista: "))
        print(f"Elemento na posição {indice}: {lista[indice]}")
    
    except IndexError:
        print("Erro: Índice fora do alcance da lista! Digite um número entre 0 e 4.")
    except ValueError:
        print("Erro: O índice deve ser um número inteiro!")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Chamar a função
acessar_elemento_lista()
