# Dicionário para converter o número do mês para o nome abreviado e completo
meses = {
    1: ("jan", "janeiro"),
    2: ("fev", "fevereiro"),
    3: ("mar", "março"),
    4: ("abr", "abril"),
    5: ("mai", "maio"),
    6: ("jun", "junho"),
    7: ("jul", "julho"),
    8: ("ago", "agosto"),
    9: ("set", "setembro"),
    10: ("out", "outubro"),
    11: ("nov", "novembro"),
    12: ("dez", "dezembro")
}

# Solicitar o dia, mês e ano de nascimento
dia = int(input("Digite o dia de nascimento: "))
mes = int(input("Digite o mês de nascimento (em número): "))
ano = int(input("Digite o ano de nascimento (com 4 dígitos): "))

# Exibir as opções de formato de data
print("Escolha o formato de exibição da data:")
print("1 – Data simples. Ex.: 10/08/1990")
print("2 – Data abreviada. Ex.: 10/ago/1990")
print("3 – Data completa. Ex.: 10 de agosto de 1990")

# Solicitar a escolha do formato de exibição
formato = int(input("Digite o código do formato de exibição: "))

# Exibir a data no formato escolhido
if formato == 1:
    print(f"{dia:02}/{mes:02}/{ano}")
elif formato == 2:
    mes_abreviado = meses[mes][0]
    print(f"{dia:02}/{mes_abreviado}/{ano}")
elif formato == 3:
    mes_completo = meses[mes][1]
    print(f"{dia:02} de {mes_completo} de {ano}")
else:
    print("Formato de exibição inválido.")
