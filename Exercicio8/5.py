class SaldoInsuficienteError(Exception):
    pass

def operacoes_bancarias():
    saldo = 1000.00  # Saldo inicial
    try:
        saque = float(input("Digite o valor para saque: R$ "))
        
        if saque > saldo:
            raise SaldoInsuficienteError("Erro: Saldo insuficiente para o saque!")
        
        saldo -= saque
        print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
    
    except ValueError:
        print("Erro: Você deve digitar um número válido para o saque!")
    except SaldoInsuficienteError as e:
        print(e)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Chamar a função
operacoes_bancarias()
