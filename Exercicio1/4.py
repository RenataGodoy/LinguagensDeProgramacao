import math
# Solicita ao usuário o número de horas trabalhadas e o valor por hora
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
valor_por_hora = float(input("Digite o valor recebido por hora: "))

salario_total = horas_trabalhadas * valor_por_hora
2

print(f"O salário total do mês é: R$ {salario_total:.2f}")
