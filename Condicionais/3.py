def validar_valor(valor):
    return 1 <= valor <= 5

def determinar_ganhador(jogador1_palpite, jogador1_valor, jogador2_valor):
    soma = jogador1_valor + jogador2_valor
    if soma % 2 == 0:
        resultado = "par"
    else:
        resultado = "ímpar"

    if resultado == jogador1_palpite:
        return "Jogador 1"
    else:
        return "Jogador 2"

# Solicitar o palpite e valor do Jogador 1
jogador1_palpite = input("Jogador 1, escolha par ou ímpar: ").strip().lower()
jogador1_valor = int(input("Jogador 1, insira um valor de 1 a 5: "))

# Solicitar o palpite e valor do Jogador 2
jogador2_palpite = "ímpar" if jogador1_palpite == "par" else "par"
jogador2_valor = int(input("Jogador 2, insira um valor de 1 a 5: "))

# Validar os valores
if not (validar_valor(jogador1_valor) and validar_valor(jogador2_valor)):
    print("Esta rodada não valeu. Um dos valores está fora dos parâmetros informados.")
else:
    ganhador = determinar_ganhador(jogador1_palpite, jogador1_valor, jogador2_valor)
    print(f"{ganhador} ganhou esta rodada!")
