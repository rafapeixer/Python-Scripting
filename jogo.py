import pygame
import random

# Inicializa o Pygame
pygame.init()

# Definindo as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

# Dimensões da tela
LARGURA_TELA = 800
ALTURA_TELA = 600

# Cria a tela do jogo
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Jogo de Desvio de Objetos")

# Definindo as variáveis do jogador
largura_jogador = 50
altura_jogador = 60
x_jogador = (LARGURA_TELA // 2) - (largura_jogador // 2)
y_jogador = ALTURA_TELA - altura_jogador - 10
velocidade_jogador = 5

# Definindo as variáveis dos objetos que caem
largura_objeto = 50
altura_objeto = 50
velocidade_objeto = 5
intervalo_objetos = 1000  # Intervalo em milissegundos para a criação de novos objetos

# Lista para armazenar os objetos que caem
objetos = []

# Definindo o relógio do jogo
relogio = pygame.time.Clock()

# Variável para controlar o loop principal
jogando = True

# Variável para contar os pontos
pontos = 0

# Tempo inicial
tempo_inicial = pygame.time.get_ticks()

# Função para criar novos objetos que caem
def criar_objeto():
    x = random.randint(0, LARGURA_TELA - largura_objeto)
    y = -altura_objeto
    return [x, y]

# Função para desenhar o jogador
def desenhar_jogador(x, y):
    pygame.draw.rect(tela, BRANCO, [x, y, largura_jogador, altura_jogador])

# Função para desenhar os objetos que caem
def desenhar_objetos(objetos):
    for objeto in objetos:
        pygame.draw.rect(tela, VERMELHO, [objeto[0], objeto[1], largura_objeto, altura_objeto])

# Função para desenhar os pontos
def desenhar_pontos(pontos):
    fonte = pygame.font.SysFont(None, 36)
    texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto, (10, 10))

# Loop principal do jogo
while jogando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False

    # Movendo o jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and x_jogador > 0:
        x_jogador -= velocidade_jogador
    if teclas[pygame.K_RIGHT] and x_jogador < LARGURA_TELA - largura_jogador:
        x_jogador += velocidade_jogador

    # Atualizando a posição dos objetos
    for objeto in objetos:
        objeto[1] += velocidade_objeto

    # Removendo objetos que saíram da tela
    objetos = [objeto for objeto in objetos if objeto[1] < ALTURA_TELA]

    # Criando novos objetos
    if pygame.time.get_ticks() % intervalo_objetos < 20:
        objetos.append(criar_objeto())

    # Verificando colisões
    for objeto in objetos:
        if (objeto[1] + altura_objeto > y_jogador and objeto[1] < y_jogador + altura_jogador and
                objeto[0] + largura_objeto > x_jogador and objeto[0] < x_jogador + largura_jogador):
            jogando = False

    # Atualizando os pontos
    tempo_decorrido = (pygame.time.get_ticks() - tempo_inicial) // 1000
    pontos = tempo_decorrido * 3

    # Preenchendo a tela com a cor preta
    tela.fill(PRETO)

    # Desenhando o jogador e os objetos
    desenhar_jogador(x_jogador, y_jogador)
    desenhar_objetos(objetos)

    # Desenhando os pontos
    desenhar_pontos(pontos)

    # Atualizando a tela
    pygame.display.flip()

    # Controlando a taxa de quadros
    relogio.tick(60)

# Finalizando o Pygame
pygame.quit()
