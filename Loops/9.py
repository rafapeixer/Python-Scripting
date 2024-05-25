# Função para converter um número decimal em hexadecimal
def decimal_para_hexadecimal(numero_decimal):
    if numero_decimal == 0:
        return "0"

    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""

    while numero_decimal > 0:
        resto = numero_decimal % 16
        hexadecimal = hex_digits[resto] + hexadecimal
        numero_decimal = numero_decimal // 16

    return hexadecimal

# Solicitar um número decimal ao usuário
numero_decimal = int(input("Digite um número decimal: "))

# Converter o número decimal para hexadecimal
numero_hexadecimal = decimal_para_hexadecimal(numero_decimal)

# Exibir o valor hexadecimal
print(f"O valor hexadecimal de {numero_decimal} é {numero_hexadecimal}.")
