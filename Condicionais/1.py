# Solicitar a altura e o sexo da pessoa
altura = float(input("Digite a sua altura em metros (ex: 1.75): "))
sexo = input("Digite o seu sexo (M para masculino e F para feminino): ").strip().upper()

# Calcular o peso ideal
if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = None
    print("Sexo inválido. Por favor, digite M para masculino ou F para feminino.")

# Exibir o peso ideal
if peso_ideal is not None:
    print(f"O seu peso ideal é {peso_ideal:.2f} kg.")
1.82