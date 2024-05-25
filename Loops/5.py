# Inicializar as populações e taxas de natalidade
populacao_a = 5000000
populacao_b = 7000000
taxa_a = 0.03
taxa_b = 0.02

# Inicializar o contador de anos
anos = 0

# Loop para calcular o tempo necessário para a população do país A ultrapassar a do país B
while populacao_a <= populacao_b:
    populacao_a += populacao_a * taxa_a
    populacao_b += populacao_b * taxa_b
    anos += 1

# Imprimir o resultado
print(f"Serão necessários {anos} anos para que a população do país A ultrapasse a população do país B.")
