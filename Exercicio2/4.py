# Solicita duas notas, calcula a média e informa a situação do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print("Aprovado.")
elif 5 <= media < 7:
    print("Recuperação.")
else:
    print("Reprovado.")