# Solicita a idade e classifica em menor de idade, adulto ou idoso
idade = int(input("Digite a idade: "))
if idade < 18:
    print("Menor de idade.")
elif 18 <= idade <= 59:
    print("Adulto.")
else:
    print("Idoso.")
