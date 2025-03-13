def abrir_arquivo():
    nome_arquivo = input("Digite o nome do arquivo para ler (por exemplo, rodou.txt): ")
    
    try:
        # Tenta abrir o arquivo no modo de leitura
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print("\nConteúdo do arquivo:")
            print(conteudo)
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado!")
    except IOError:
        print("Erro: Problema ao tentar ler o arquivo!")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Chamar a função
abrir_arquivo()
