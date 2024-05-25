def determinar_vencedor(jogador1, jogador2):
    if jogador1 == jogador2:
        return 0  # Empate
    elif (jogador1 == 'pedra' and jogador2 == 'tesoura') or \
         (jogador1 == 'papel' and jogador2 == 'pedra') or \
         (jogador1 == 'tesoura' and jogador2 == 'papel'):
        return 1  # Jogador 1 vence
    else:
        return 2  # Jogador 2 vence

# Solicitar a quantidade de pontos para vencer
pontos_para_vencer = int(input("Digite a quantidade de pontos para vencer: "))

# Inicializar pontuações
pontos_jogador1 = 0
pontos_jogador2 = 0

# Loop do jogo
while pontos_jogador1 < pontos_para_vencer and pontos_jogador2 < pontos_para_vencer:
    # Solicitar as escolhas dos jogadores
    jogador1 = input("Jogador 1, escolha pedra, papel ou tesoura: ").strip().lower()
    jogador2 = input("Jogador 2, escolha pedra, papel ou tesoura: ").strip().lower()

    # Determinar o vencedor da rodada
    vencedor = determinar_vencedor(jogador1, jogador2)
    if vencedor == 1:
        pontos_jogador1 += 1
        print("Jogador 1 vence esta rodada!")
    elif vencedor == 2:
        pontos_jogador2 += 1
        print("Jogador 2 vence esta rodada!")
    else:
        print("Empate nesta rodada!")

    # Exibir pontuação atual
    print(f"Pontuação - Jogador 1: {pontos_jogador1}, Jogador 2: {pontos_jogador2}")

# Determinar o vencedor do jogo
if pontos_jogador1 == pontos_para_vencer:
    print("Jogador 1 vence o jogo!")
else:
    print("Jogador 2 vence o jogo!")
