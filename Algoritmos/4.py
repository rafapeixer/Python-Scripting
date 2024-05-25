# Solicitar o nome do produto, valor unitário e quantidade
nome_produto = input("Digite o nome do produto: ")
valor_unitario = float(input("Digite o valor unitário do produto: "))
quantidade = int(input("Digite a quantidade: "))

# Calcular o valor de compra
valor_compra = valor_unitario * quantidade

# Exibir o valor de compra
print(f"O valor de compra do produto {nome_produto} é {valor_compra:.2f}.")
