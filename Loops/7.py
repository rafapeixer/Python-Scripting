# Inicializar variáveis
contagem_a = 0

# Loop para solicitar palavras ao usuário
while True:
    palavra = input("Digite uma palavra (ou pressione Enter para sair): ").strip()
    if palavra == "":
        break
    # Contar letras "A" (considerando maiúsculas e minúsculas)
    contagem_a += palavra.lower().count('a')

# Exibir o resultado
print(f"O total de letras 'A' no conjunto de palavras é: {contagem_a}")
