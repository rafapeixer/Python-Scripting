# Solicitar o nome completo do usuário
nome_completo = input("Digite o seu nome completo: ")

# Dividir o nome completo em partes
partes_nome = nome_completo.split()

# Obter o primeiro e o último nome
primeiro_nome = partes_nome[0]
ultimo_nome = partes_nome[-1]

# Imprimir o primeiro e o último nome
print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}")
