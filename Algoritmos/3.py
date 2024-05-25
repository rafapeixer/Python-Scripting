# Solicitar o nome da disciplina e as notas bimestrais
nome_disciplina = input("Digite o nome da disciplina: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Calcular a média das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# Exibir a média
print(f"A média da disciplina {nome_disciplina} é {media:.2f}.")
