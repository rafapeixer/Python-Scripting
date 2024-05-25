from datetime import datetime, timedelta

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

# Solicitar data e hora separadamente
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano (com 4 dígitos): "))
hora = int(input("Digite a hora: "))
minuto = int(input("Digite o minuto: "))
segundo = int(input("Digite o segundo: "))

# Criar um objeto datetime com a data e hora fornecidas
data = datetime(ano, mes, dia, hora, minuto, segundo)

# Exibir opções de informação a ser acrescentada
print("Escolha a informação que deseja acrescentar:")
print("1 – Dia")
print("2 – Mês")
print("3 – Ano")
print("4 – Hora")
print("5 – Minuto")
print("6 – Segundo")

# Solicitar escolha do usuário
escolha = int(input("Digite o código da informação que deseja acrescentar: "))
quantidade = int(input("Digite a quantidade a ser acrescentada: "))

# Acrescentar a quantidade escolhida à data e hora
if escolha == 1:
    data += timedelta(days=quantidade)
elif escolha == 2:
    # Adicionar meses, considerando mudanças de ano
    mes = data.month - 1 + quantidade
    ano = data.year + mes // 12
    mes = mes % 12 + 1
    dia = min(data.day, [31, 29 if eh_bissexto(ano) and mes == 2 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][mes - 1])
    data = data.replace(year=ano, month=mes, day=dia)
elif escolha == 3:
    data = data.replace(year=data.year + quantidade)
elif escolha == 4:
    data += timedelta(hours=quantidade)
elif escolha == 5:
    data += timedelta(minutes=quantidade)
elif escolha == 6:
    data += timedelta(seconds=quantidade)
else:
    print("Código de informação inválido.")
    exit()

# Exibir a nova data e hora
print("A nova data e hora é:", data.strftime("%d/%m/%Y %H:%M:%S"))
