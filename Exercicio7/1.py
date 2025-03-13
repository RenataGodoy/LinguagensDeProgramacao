# Dicionário para armazenar alunos e suas notas
alunos = {}

# Cadastro de pelo menos 3 alunos
for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota

# Exibir a lista de alunos e suas notas
print("\nLista de alunos e suas notas:")
for nome, nota in alunos.items():
    print(f"{nome}: {nota:.2f}")
