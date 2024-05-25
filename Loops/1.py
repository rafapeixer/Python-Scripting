# Solicitar a massa inicial do material radioativo
massa_inicial = float(input("Digite a massa inicial do material em gramas: "))

# Inicializar variáveis
massa = massa_inicial
tempo = 0

# Loop para calcular o tempo necessário para a massa ser menor que 0,5 gramas
while massa >= 0.5:
    massa /= 2
    tempo += 50

# Imprimir a massa final e o tempo calculado
print(f"Massa final: {massa:.2f} gramas")
print(f"Tempo necessário: {tempo} segundos")
