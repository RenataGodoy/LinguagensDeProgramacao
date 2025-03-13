def divisao_segura():
    try:
        # Solicitar ao usuário dois números
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Realizar a divisão
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado:.2f}")
    
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero!")
    except ValueError:
        print("Erro: Você deve inserir apenas números válidos!")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Chamar a função
divisao_segura()
