# Tupla com os 10 primeiros colocados no campeonato
times = ("Fluminense", "Vasco", "Marica", "Nova Iguana", "Gremili", 
         "Inter di milhao", "Bahia", "Santos", "Botafogo", "Corinthians")

# Exibir os três primeiros colocados
print("Os três primeiros colocados:", times[:3])

# Exibir os últimos três colocados
print("Os três últimos colocados:", times[-3:])

# Exibir os times em ordem alfabética
print("Times em ordem alfabética:", sorted(times))

# Solicitar ao usuário um time específico e exibir sua posição
time_especifico = input("Digite o nome de um time para saber sua posição: ")
if time_especifico in times:
    posicao_time = times.index(time_especifico) + 1  # Somamos 1 para mostrar posição real
    print(f"O {time_especifico} está na posição {posicao_time}.")
else:
    print("Time não encontrado.")
