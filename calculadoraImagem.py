import tkinter as tk
from tkinter import messagebox
import math

# Funções das operações matemáticas
def adicionar():
    try:
        valor = float(entrada.get())
        resultado = valor + valor2.get()
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida")

def subtrair():
    try:
        valor = float(entrada.get())
        resultado = valor - valor2.get()
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida")

def multiplicar():
    try:
        valor = float(entrada.get())
        resultado = valor * valor2.get()
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida")

def dividir():
    try:
        valor = float(entrada.get())
        if valor2.get() != 0:
            resultado = valor / valor2.get()
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, str(resultado))
        else:
            messagebox.showerror("Erro", "Divisão por zero")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida")

def raiz_quadrada():
    try:
        valor = float(entrada.get())
        resultado = math.sqrt(valor)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida")

def exponenciar():
    try:
        valor = float(entrada.get())
        resultado = valor ** valor2.get()
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida")

def seno():
    try:
        valor = float(entrada.get())
        resultado = math.sin(math.radians(valor))
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida")

def cosseno():
    try:
        valor = float(entrada.get())
        resultado = math.cos(math.radians(valor))
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida")

# Função para definir a operação selecionada
def definir_operacao(operacao):
    global operacao_atual
    operacao_atual = operacao
    try:
        global valor1
        valor1 = float(entrada.get())
        entrada.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida")

def calcular():
    try:
        valor2 = float(entrada.get())
        entrada.delete(0, tk.END)
        if operacao_atual == "adicionar":
            entrada.insert(tk.END, str(valor1 + valor2))
        elif operacao_atual == "subtrair":
            entrada.insert(tk.END, str(valor1 - valor2))
        elif operacao_atual == "multiplicar":
            entrada.insert(tk.END, str(valor1 * valor2))
        elif operacao_atual == "dividir":
            if valor2 != 0:
                entrada.insert(tk.END, str(valor1 / valor2))
            else:
                messagebox.showerror("Erro", "Divisão por zero")
        elif operacao_atual == "exponenciar":
            entrada.insert(tk.END, str(valor1 ** valor2))
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida")

# Função para limpar a entrada
def limpar():
    entrada.delete(0, tk.END)

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Campo de entrada
entrada = tk.Entry(janela, width=20, font=("Arial", 24))
entrada.grid(row=0, column=0, columnspan=4)

# Botões de números
botoes_numeros = []
for i in range(10):
    botoes_numeros.append(tk.Button(janela, text=str(i), width=5, height=2, font=("Arial", 18),
                                    command=lambda x=i: entrada.insert(tk.END, str(x))))
for i in range(1, 10):
    botoes_numeros[i].grid(row=(i-1)//3+1, column=(i-1)%3)
botoes_numeros[0].grid(row=4, column=1)

# Botões de operações
tk.Button(janela, text="+", width=5, height=2, font=("Arial", 18), command=lambda: definir_operacao("adicionar")).grid(row=1, column=3)
tk.Button(janela, text="-", width=5, height=2, font=("Arial", 18), command=lambda: definir_operacao("subtrair")).grid(row=2, column=3)
tk.Button(janela, text="*", width=5, height=2, font=("Arial", 18), command=lambda: definir_operacao("multiplicar")).grid(row=3, column=3)
tk.Button(janela, text="/", width=5, height=2, font=("Arial", 18), command=lambda: definir_operacao("dividir")).grid(row=4, column=3)

# Botões de funções avançadas
tk.Button(janela, text="√", width=5, height=2, font=("Arial", 18), command=raiz_quadrada).grid(row=1, column=4)
tk.Button(janela, text="^", width=5, height=2, font=("Arial", 18), command=lambda: definir_operacao("exponenciar")).grid(row=2, column=4)
tk.Button(janela, text="sin", width=5, height=2, font=("Arial", 18), command=seno).grid(row=3, column=4)
tk.Button(janela, text="cos", width=5, height=2, font=("Arial", 18), command=cosseno).grid(row=4, column=4)

# Botões de limpar e calcular
tk.Button(janela, text="C", width=5, height=2, font=("Arial", 18), command=limpar).grid(row=4, column=0)
tk.Button(janela, text="=", width=5, height=2, font=("Arial", 18), command=calcular).grid(row=4, column=2)

# Iniciar a aplicação
janela.mainloop()
