from datetime import datetime

def eh_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Solicitar a primeira data ao usuário
dia1 = int(input("Digite o dia da primeira data: "))
mes1 = int(input("Digite o mês da primeira data: "))
ano1 = int(input("Digite o ano da primeira data (com 4 dígitos): "))

# Solicitar a segunda data ao usuário
dia2 = int(input("Digite o dia da segunda data: "))
mes2 = int(input("Digite o mês da segunda data: "))
ano2 = int(input("Digite o ano da segunda data (com 4 dígitos): "))

# Criar objetos datetime com as datas fornecidas
data1 = datetime(ano1, mes1, dia1)
data2 = datetime(ano2, mes2, dia2)

# Calcular a diferença em dias entre as duas datas
diferenca_dias = abs((data2 - data1).days)

# Exibir a quantidade de dias entre as duas datas
print(f"A quantidade de dias entre {data1.strftime('%d/%m/%Y')} e {data2.strftime('%d/%m/%Y')} é {diferenca_dias} dias.")
