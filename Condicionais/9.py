def calcular_digito_verificador(cpf, multiplicadores):
    soma = sum([int(cpf[i]) * multiplicadores[i] for i in range(len(multiplicadores))])
    resto = (soma * 10) % 11
    return 0 if resto == 10 else resto

# Solicitar os 11 dígitos do CPF separadamente
cpf = [input(f"Digite o {i+1}º dígito do CPF: ") for i in range(11)]

# Validar o primeiro dígito verificador
multiplicadores_primeiro = [10, 9, 8, 7, 6, 5, 4, 3, 2]
primeiro_digito_verificador = calcular_digito_verificador(cpf, multiplicadores_primeiro)

# Validar o segundo dígito verificador
multiplicadores_segundo = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
segundo_digito_verificador = calcular_digito_verificador(cpf, multiplicadores_segundo)

# Verificar se os dígitos verificadores estão corretos
if int(cpf[9]) == primeiro_digito_verificador and int(cpf[10]) == segundo_digito_verificador:
    print("O CPF é válido.")
else:
    print("O CPF é inválido.")
