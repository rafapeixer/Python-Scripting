# Dicionários fornecidos
estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}
cardapio = {
    'x-burguer': ['pao', 'hamburguer'],
    'x-salada': ['pao', 'hamburguer', 'tomate'],
    'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
    'x-egg': ['pao', 'hamburguer', 'ovo'],
    'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}

# Função para imprimir o cardápio
def imprimir_cardapio():
    print("Cardápio do Restaurante Boca Feliz:")
    for item, ingredientes in cardapio.items():
        print(f"- {item}: {', '.join(ingredientes)}")
    print("\nO que deseja pedir (0 para sair)?")

# Função para verificar e processar o pedido
def processar_pedido(pedido):
    if pedido not in cardapio:
        print("Item não localizado no cardápio.")
        return

    ingredientes_necessarios = cardapio[pedido]
    ingredientes_faltantes = []

    for ingrediente in ingredientes_necessarios:
        if estoque.get(ingrediente, 0) <= 0:
            ingredientes_faltantes.append(ingrediente)

    if ingredientes_faltantes:
        for ingrediente in ingredientes_faltantes:
            print(f"Infelizmente acabou o {ingrediente}")
    else:
        for ingrediente in ingredientes_necessarios:
            estoque[ingrediente] -= 1
        print(f"Um {pedido} saindo no capricho!!!")

# Loop principal
while True:
    imprimir_cardapio()
    pedido = input().strip().lower()

    if pedido == '0':
        print("Obrigado por utilizar o sistema do Restaurante Boca Feliz!")
        break

    processar_pedido(pedido)
