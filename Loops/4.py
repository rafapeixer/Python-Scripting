# Solicitar 5 números ao usuário e armazená-los em uma lista
numeros = []
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

# Ordenar a lista em ordem crescente
for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]

# Exibir os números em ordem crescente
print("Números em ordem crescente:")
for numero in numeros:
    print(numero)
