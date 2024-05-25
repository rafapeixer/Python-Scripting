# Solicitar o peso e a altura do adulto
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros (ex: 1.75): "))

# Calcular o IMC
imc = peso / (altura ** 2)

# Determinar a condição de peso
if imc < 18.5:
    condicao = "Abaixo do peso"
elif 18.5 <= imc < 25:
    condicao = "Peso normal"
elif 25 <= imc < 30:
    condicao = "Acima do peso"
else:
    condicao = "Obeso"

# Exibir o IMC e a condição de peso
print(f"Seu IMC é {imc:.2f}. Você está na condição: {condicao}.")
