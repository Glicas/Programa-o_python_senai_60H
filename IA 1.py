#feito com IA

#exercício 1

import tkinter as tk
import math

# ---------------- FUNÇÕES ----------------
def clicar(valor):
    visor.insert(tk.END, valor)

def limpar():
    visor.delete(0, tk.END)

def calcular():
    try:
        conta = visor.get()
        resultado = eval(conta)
        historico.insert(tk.END, conta + " = " + str(resultado))
        visor.delete(0, tk.END)
        visor.insert(0, str(resultado))
    except:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")

# ----------- FUNÇÕES CIENTÍFICAS ----------
def raiz():
    try:
        valor = float(visor.get())
        res = math.sqrt(valor)
        visor.delete(0, tk.END)
        visor.insert(0, res)
    except:
        visor.insert(0, "Erro")

def quadrado():
    try:
        valor = float(visor.get())
        res = valor ** 2
        visor.delete(0, tk.END)
        visor.insert(0, res)
    except:
        visor.insert(0, "Erro")

def seno():
    try:
        valor = float(visor.get())
        res = math.sin(math.radians(valor))
        visor.delete(0, tk.END)
        visor.insert(0, res)
    except:
        visor.insert(0, "Erro")

def cosseno():
    try:
        valor = float(visor.get())
        res = math.cos(math.radians(valor))
        visor.delete(0, tk.END)
        visor.insert(0, res)
    except:
        visor.insert(0, "Erro")

def log():
    try:
        valor = float(visor.get())
        res = math.log10(valor)
        visor.delete(0, tk.END)
        visor.insert(0, res)
    except:
        visor.insert(0, "Erro")

# ---------------- JANELA ----------------
root = tk.Tk()
root.title("Calculadora Ultra Pro")
root.geometry("420x600")
root.configure(bg="#0f172a")

# ---------------- VISOR ----------------
visor = tk.Entry(root, font=("Arial", 22, "bold"),
                 bg="#020617", fg="#38bdf8",
                 bd=0, justify="right")
visor.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=10)

# ---------------- HISTÓRICO ----------------
historico = tk.Listbox(root, height=5, bg="#020617", fg="white")
historico.pack(fill="both", padx=10, pady=5)

# ---------------- FRAME BOTÕES ----------------
frame = tk.Frame(root, bg="#0f172a")
frame.pack()

def btn(txt, row, col, cmd, cor="#1e293b", w=5, h=2):
    tk.Button(frame, text=txt, command=cmd,
              font=("Arial", 12, "bold"),
              bg=cor, fg="white",
              activebackground="#334155",
              bd=0, width=w, height=h)\
        .grid(row=row, column=col, padx=4, pady=4)

# ----------- CIENTÍFICOS ----------
btn("√", 0, 0, raiz, "#9333ea")
btn("x²", 0, 1, quadrado, "#9333ea")
btn("sin", 0, 2, seno, "#9333ea")
btn("cos", 0, 3, cosseno, "#9333ea")
btn("log", 0, 4, log, "#9333ea")

# ----------- LINHAS PRINCIPAIS ----------
btn("C", 1, 0, limpar, "#ef4444")
btn("(", 1, 1, lambda: clicar("("))
btn(")", 1, 2, lambda: clicar(")"))
btn("/", 1, 3, lambda: clicar("/"), "#f59e0b")

btn("7", 2, 0, lambda: clicar("7"))
btn("8", 2, 1, lambda: clicar("8"))
btn("9", 2, 2, lambda: clicar("9"))
btn("*", 2, 3, lambda: clicar("*"), "#f59e0b")

btn("4", 3, 0, lambda: clicar("4"))
btn("5", 3, 1, lambda: clicar("5"))
btn("6", 3, 2, lambda: clicar("6"))
btn("-", 3, 3, lambda: clicar("-"), "#f59e0b")

btn("1", 4, 0, lambda: clicar("1"))
btn("2", 4, 1, lambda: clicar("2"))
btn("3", 4, 2, lambda: clicar("3"))
btn("+", 4, 3, lambda: clicar("+"), "#22c55e")

btn("0", 5, 0, lambda: clicar("0"), w=11)
btn(".", 5, 2, lambda: clicar("."))
btn("=", 5, 3, calcular, "#06b6d4")

# ---------------- TECLADO ----------------
def tecla(event):
    tecla = event.char
    if tecla in "0123456789+-*/().":
        clicar(tecla)
    elif event.keysym == "Return":
        calcular()
    elif event.keysym == "BackSpace":
        visor.delete(len(visor.get())-1, tk.END)

root.bind("<Key>", tecla)

root.mainloop()

