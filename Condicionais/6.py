import math

# Solicitar os coeficientes A, B e C
a = float(input("Digite o valor do coeficiente A: "))
b = float(input("Digite o valor do coeficiente B: "))
c = float(input("Digite o valor do coeficiente C: "))

# Verificar se é uma equação do 2º grau
if a == 0:
    print("O valor de A deve ser diferente de zero para que seja uma equação do 2º grau.")
else:
    # Calcular o discriminante (delta)
    delta = b**2 - 4*a*c

    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        # Calcular a raiz única
        x = -b / (2*a)
        print(f"A equação possui uma raiz real: x = {x:.2f}")
    else:
        # Calcular as duas raízes reais
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"A equação possui duas raízes reais: x1 = {x1:.2f} e x2 = {x2:.2f}")
