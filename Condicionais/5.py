# Exibir as opções de destino
print("Escolha o destino do passageiro:")
print("1 – Região Norte")
print("2 – Região Nordeste")
print("3 – Região Centro-Oeste")
print("4 – Região Sul")

# Solicitar a escolha do destino
destino = int(input("Digite o código do destino: "))

# Solicitar se a viagem inclui retorno (ida e volta)
ida_volta = input("A viagem inclui retorno (ida e volta)? (S/N): ").strip().upper()

# Determinar o preço da passagem
if destino == 1:
    if ida_volta == 'S':
        preco_passagem = 900.00  # Região Norte, ida e volta
    else:
        preco_passagem = 500.00  # Região Norte, só ida
elif destino == 2:
    if ida_volta == 'S':
        preco_passagem = 650.00  # Região Nordeste, ida e volta
    else:
        preco_passagem = 350.00  # Região Nordeste, só ida
elif destino == 3:
    if ida_volta == 'S':
        preco_passagem = 600.00  # Região Centro-Oeste, ida e volta
    else:
        preco_passagem = 350.00  # Região Centro-Oeste, só ida
elif destino == 4:
    if ida_volta == 'S':
        preco_passagem = 550.00  # Região Sul, ida e volta
    else:
        preco_passagem = 300.00  # Região Sul, só ida
else:
    preco_passagem = None
    print("Destino inválido.")

# Exibir o preço da passagem
if preco_passagem is not None:
    print(f"O preço da passagem é: R$ {preco_passagem:.2f}")
