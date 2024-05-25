# Dicionário com os valores das unidades em anos-luz
ano_luz = {
    "pc": 0.31,
    "al": 1,
    "ae": 63241.09,
    "ml": 525960.23,
    "sl": 31557609.92
}

# Lista de unidades
unidades = ["Parsec (pc)", "Ano-Luz (al)", "Unidade Astronômica (ae)", "Minuto-Luz (ml)", "Segundo-Luz (sl)"]

# Função para imprimir a lista de unidades de conversão
def imprimir_unidades():
    print("Unidades de conversão disponíveis:")
    for unidade in unidades:
        print(unidade)

# Função para converter valores entre unidades de tempo em deslocamento no espaço
def converter(valor, de, para):
    # Converter o valor para anos-luz
    valor_em_anos_luz = valor * ano_luz[de]
    # Converter de anos-luz para a unidade de destino
    valor_convertido = valor_em_anos_luz / ano_luz[para]
    return valor_convertido

# Imprimir a lista de unidades de conversão
imprimir_unidades()

# Solicitar o valor a ser convertido
valor = float(input("Valor a ser convertido: "))

# Solicitar a unidade origem do valor
unidade_origem = input("Converter de (pc, al, ae, ml, sl): ").strip().lower()

# Solicitar a unidade destino da conversão
unidade_destino = input("Converter para (pc, al, ae, ml, sl): ").strip().lower()

# Verificar se as unidades fornecidas são válidas
if unidade_origem not in ano_luz or unidade_destino not in ano_luz:
    print("Unidade de conversão inválida. Por favor, tente novamente.")
else:
    # Realizar a conversão
    valor_convertido = converter(valor, unidade_origem, unidade_destino)
    # Exibir o valor convertido
    print(f"Conversão: {valor} {unidade_origem} = {valor_convertido:.2f} {unidade_destino}")
