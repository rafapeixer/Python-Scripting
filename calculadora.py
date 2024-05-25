import math

def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero"

def raiz_quadrada(x):
    return math.sqrt(x)

def exponenciar(x, y):
    return x ** y

def seno(x):
    return math.sin(math.radians(x))

def cosseno(x):
    return math.cos(math.radians(x))

def menu():
    print("Escolha a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Raiz Quadrada")
    print("6 - Exponenciação")
    print("7 - Seno")
    print("8 - Cosseno")
    print("0 - Sair")

while True:
    menu()
    escolha = input("Digite a sua escolha: ")

    if escolha == '0':
        print("Saindo da calculadora...")
        break

    if escolha in ['1', '2', '3', '4', '6']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

    if escolha == '5':
        num = float(input("Digite o número: "))

    if escolha == '7' or escolha == '8':
        angulo = float(input("Digite o ângulo em graus: "))

    if escolha == '1':
        print(f"Resultado: {num1} + {num2} = {adicionar(num1, num2)}")
    elif escolha == '2':
        print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
    elif escolha == '3':
        print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
    elif escolha == '4':
        print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")
    elif escolha == '5':
        print(f"Resultado: √{num} = {raiz_quadrada(num)}")
    elif escolha == '6':
        print(f"Resultado: {num1} ^ {num2} = {exponenciar(num1, num2)}")
    elif escolha == '7':
        print(f"Resultado: seno({angulo}) = {seno(angulo)}")
    elif escolha == '8':
        print(f"Resultado: cosseno({angulo}) = {cosseno(angulo)}")
    else:
        print("Escolha inválida, por favor tente novamente.")
