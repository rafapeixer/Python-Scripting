# Gerar números entre 1000 e 1999 e verificar quais deles têm resto 5 quando divididos por 11
for numero in range(1000, 2000):
    if numero % 11 == 5:
        print(numero)
