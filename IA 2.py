#feito com IA 
#exercício 2

import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

ARQUIVO = "clientes.csv"

class SistemaCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadastro de Clientes")
        self.root.geometry("900x600")

        self.criar_interface()
        self.criar_tabela()
        self.carregar_dados()

    # -------- INTERFACE --------
    def criar_interface(self):
        frame = ttk.Frame(self.root)
        frame.pack(pady=10)

        self.campos = {}

        labels = ["Nome", "Idade", "E-mail", "Celular", "Cidade"]

        for i, texto in enumerate(labels):
            ttk.Label(frame, text=texto).grid(row=i, column=0, padx=5, pady=5)

            entry = ttk.Entry(frame, width=30)
            entry.grid(row=i, column=1, padx=5, pady=5)

            self.campos[texto] = entry

        # Botões
        ttk.Button(frame, text="Cadastrar", command=self.salvar).grid(row=6, column=0, pady=10)
        ttk.Button(frame, text="Limpar", command=self.limpar).grid(row=6, column=1)

        # Busca
        ttk.Label(frame, text="Buscar:").grid(row=7, column=0)
        self.buscar_entry = ttk.Entry(frame)
        self.buscar_entry.grid(row=7, column=1)

        ttk.Button(frame, text="Pesquisar", command=self.buscar).grid(row=7, column=2)

    # -------- TABELA --------
    def criar_tabela(self):
        colunas = ("Nome", "Idade", "E-mail", "Celular", "Cidade")

        self.tree = ttk.Treeview(self.root, columns=colunas, show="headings")

        for col in colunas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        self.tree.pack(pady=20, fill="both", expand=True)

    # -------- VALIDAÇÃO --------
    def validar(self, dados):
        if not dados["Nome"]:
            messagebox.showerror("Erro", "Nome obrigatório")
            return False

        if not dados["Idade"].isdigit():
            messagebox.showerror("Erro", "Idade inválida")
            return False

        if "@" not in dados["E-mail"]:
            messagebox.showerror("Erro", "E-mail inválido")
            return False

        return True

    # -------- SALVAR --------
    def salvar(self):
        dados = {campo: self.campos[campo].get() for campo in self.campos}

        if not self.validar(dados):
            return

        arquivo_existe = os.path.isfile(ARQUIVO)

        with open(ARQUIVO, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=dados.keys())

            if not arquivo_existe:
                writer.writeheader()

            writer.writerow(dados)

        messagebox.showinfo("Sucesso", "Cliente cadastrado!")

        self.adicionar_tabela(dados)
        self.limpar()

    # -------- CARREGAR --------
    def carregar_dados(self):
        if not os.path.exists(ARQUIVO):
            return

        with open(ARQUIVO, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                self.adicionar_tabela(row)

    # -------- ADICIONAR NA TABELA --------
    def adicionar_tabela(self, dados):
        self.tree.insert("", tk.END, values=list(dados.values()))

    # -------- LIMPAR --------
    def limpar(self):
        for campo in self.campos.values():
            campo.delete(0, tk.END)

    # -------- BUSCAR --------
    def buscar(self):
        termo = self.buscar_entry.get().lower()

        for item in self.tree.get_children():
            self.tree.delete(item)

        if not os.path.exists(ARQUIVO):
            return

        with open(ARQUIVO, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if termo in str(row).lower():
                    self.adicionar_tabela(row)


# -------- EXECUTAR --------
root = tk.Tk()
app = SistemaCadastro(root)
root.mainloop()