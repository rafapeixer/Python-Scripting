def inicio():
    print("Você acorda em uma floresta misteriosa. Ao seu redor, há árvores altas e o som de pássaros.")
    print("Há um caminho à esquerda e outro à direita.")
    escolha = input("Você deseja ir para a esquerda ou para a direita? (esquerda/direita): ").strip().lower()
    if escolha == "esquerda":
        cena_cabana()
    elif escolha == "direita":
        cena_rio()
    else:
        print("Escolha inválida. Tente novamente.")
        inicio()

def cena_cabana():
    print("\nVocê segue pelo caminho à esquerda e encontra uma cabana abandonada.")
    print("Você decide entrar na cabana e encontra um baú trancado.")
    escolha = input("Você deseja tentar abrir o baú ou sair da cabana? (abrir/sair): ").strip().lower()
    if escolha == "abrir":
        cena_bau()
    elif escolha == "sair":
        cena_fora_cabana()
    else:
        print("Escolha inválida. Tente novamente.")
        cena_cabana()

def cena_rio():
    print("\nVocê segue pelo caminho à direita e chega a um rio.")
    print("Você pode ver uma ponte ao longe ou tentar atravessar o rio a nado.")
    escolha = input("Você deseja atravessar a ponte ou nadar pelo rio? (ponte/nadar): ").strip().lower()
    if escolha == "ponte":
        cena_ponte()
    elif escolha == "nadar":
        cena_nadar()
    else:
        print("Escolha inválida. Tente novamente.")
        cena_rio()

def cena_bau():
    print("\nVocê abre o baú e encontra um mapa da floresta.")
    print("O mapa mostra um tesouro escondido perto de um lago.")
    escolha = input("Você deseja seguir o mapa até o lago ou voltar para a floresta? (seguir/voltar): ").strip().lower()
    if escolha == "seguir":
        cena_lago()
    elif escolha == "voltar":
        inicio()
    else:
        print("Escolha inválida. Tente novamente.")
        cena_bau()

def cena_fora_cabana():
    print("\nVocê sai da cabana e encontra uma trilha que leva a uma montanha.")
    escolha = input("Você deseja seguir a trilha ou voltar para a floresta? (trilha/floresta): ").strip().lower()
    if escolha == "trilha":
        cena_montanha()
    elif escolha == "floresta":
        inicio()
    else:
        print("Escolha inválida. Tente novamente.")
        cena_fora_cabana()

def cena_ponte():
    print("\nVocê atravessa a ponte e encontra uma clareira com uma árvore gigante.")
    escolha = input("Você deseja subir na árvore ou explorar a clareira? (subir/explorar): ").strip().lower()
    if escolha == "subir":
        cena_arvore()
    elif escolha == "explorar":
        cena_clareira()
    else:
        print("Escolha inválida. Tente novamente.")
        cena_ponte()

def cena_nadar():
    print("\nVocê tenta atravessar o rio a nado, mas a correnteza é muito forte.")
    print("Você é levado pela correnteza e acaba se afogando.")
    print("Fim de jogo.")
    jogar_novamente()

def cena_lago():
    print("\nVocê segue o mapa até o lago e encontra o tesouro.")
    print("Parabéns! Você encontrou o tesouro escondido!")
    print("Fim de jogo.")
    jogar_novamente()

def cena_montanha():
    print("\nVocê segue a trilha até a montanha e encontra uma caverna.")
    escolha = input("Você deseja entrar na caverna ou continuar subindo a montanha? (caverna/montanha): ").strip().lower()
    if escolha == "caverna":
        cena_caverna()
    elif escolha == "montanha":
        cena_topo()
    else:
        print("Escolha inválida. Tente novamente.")
        cena_montanha()

def cena_arvore():
    print("\nVocê sobe na árvore e encontra um ninho de pássaros com ovos.")
    escolha = input("Você deseja pegar um ovo ou descer da árvore? (pegar/descer): ").strip().lower()
    if escolha == "pegar":
        cena_ovo()
    elif escolha == "descer":
        cena_clareira()
    else:
        print("Escolha inválida. Tente novamente.")
        cena_arvore()

def cena_clareira():
    print("\nVocê explora a clareira e encontra uma planta medicinal.")
    print("Você decide levar a planta com você.")
    print("Fim de jogo.")
    jogar_novamente()

def cena_caverna():
    print("\nVocê entra na caverna e encontra um urso adormecido.")
    escolha = input("Você deseja tentar sair da caverna silenciosamente ou enfrentar o urso? (sair/enfrentar): ").strip().lower()
    if escolha == "sair":
        cena_montanha()
    elif escolha == "enfrentar":
        cena_urso()
    else:
        print("Escolha inválida. Tente novamente.")
        cena_caverna()

def cena_topo():
    print("\nVocê continua subindo a montanha e chega ao topo.")
    print("A vista é deslumbrante, e você encontra uma pedra brilhante.")
    escolha = input("Você deseja pegar a pedra ou deixar a pedra? (pegar/deixar): ").strip().lower()
    if escolha == "pegar":
        cena_pedra()
    elif escolha == "deixar":
        print("Você deixa a pedra e desce a montanha.")
        print("Fim de jogo.")
        jogar_novamente()
    else:
        print("Escolha inválida. Tente novamente.")
        cena_topo()

def cena_ovo():
    print("\nVocê pega um ovo e desce da árvore.")
    print("De repente, um pássaro gigante aparece e leva você para longe.")
    print("Fim de jogo.")
    jogar_novamente()

def cena_urso():
    print("\nVocê decide enfrentar o urso, mas infelizmente não é páreo para ele.")
    print("Fim de jogo.")
    jogar_novamente()

def cena_pedra():
    print("\nVocê pega a pedra brilhante e sente uma energia poderosa.")
    print("Parabéns! Você encontrou um artefato mágico!")
    print("Fim de jogo.")
    jogar_novamente()

def jogar_novamente():
    escolha = input("Você deseja jogar novamente? (sim/não): ").strip().lower()
    if escolha == "sim":
        inicio()
    elif escolha == "não":
        print("Obrigado por jogar!")
    else:
        print("Escolha inválida. Tente novamente.")
        jogar_novamente()

# Iniciar o jogo
inicio()
