# Solicitar o preço normal de etiqueta do produto
preco_etiqueta = float(input("Digite o preço normal de etiqueta do produto: "))

# Exibir as opções de condição de pagamento
print("Escolha a condição de pagamento:")
print("1 – À vista em dinheiro ou cheque, recebe 10% de desconto")
print("2 – À vista no cartão de crédito, recebe 15% de desconto")
print("3 – Em duas vezes, preço normal de etiqueta sem juros")
print("4 – Em duas vezes, preço normal de etiqueta mais juros de 10%")

# Solicitar a escolha da condição de pagamento
condicao_pagamento = int(input("Digite o código da condição de pagamento: "))

# Calcular o valor a ser pago com base na condição de pagamento
if condicao_pagamento == 1:
    valor_final = preco_etiqueta * 0.90  # 10% de desconto
elif condicao_pagamento == 2:
    valor_final = preco_etiqueta * 0.85  # 15% de desconto
elif condicao_pagamento == 3:
    valor_final = preco_etiqueta  # Preço normal
elif condicao_pagamento == 4:
    valor_final = preco_etiqueta * 1.10  # 10% de juros
else:
    valor_final = None
    print("Condição de pagamento inválida.")

# Exibir o valor a ser pago
if valor_final is not None:
    print(f"O valor a ser pago é: R$ {valor_final:.2f}")
