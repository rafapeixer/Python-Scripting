# Solicitar o nome do produto, valor unitário e quantidade
nome_produto = input("Digite o nome do produto: ")
valor_unitario = float(input("Digite o valor unitário do produto: "))
quantidade = int(input("Digite a quantidade: "))

# Calcular o valor de compra
valor_compra = valor_unitario * quantidade

# Calcular o desconto para pagamento à vista
desconto = valor_compra * 0.15
valor_com_desconto = valor_compra - desconto

# Exibir o valor de compra e o valor com desconto
print(f"O valor de compra do produto {nome_produto} é {valor_compra:.2f}.")
print(f"Para pagamento à vista, o valor com 15% de desconto é {valor_com_desconto:.2f}.")
