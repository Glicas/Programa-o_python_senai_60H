#feito com IA
#exercício 3

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import csv
import os

ARQUIVO = "atendimentos.csv"

class HospitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Hospitalar")
        self.root.geometry("1200x800")
        self.root.configure(bg="#0f172a")

        self.criar_interface()
        self.criar_tabela()
        self.carregar_dados()

    # -------- INTERFACE --------
    def criar_interface(self):
        estilo = ttk.Style()
        estilo.theme_use("default")

        frame_topo = tk.Frame(self.root, bg="#0f172a")
        frame_topo.pack(pady=10)

        # LOGO
        try:
            img = Image.open("teste.jpg")
            img = img.resize((120, 120))
            self.logo = ImageTk.PhotoImage(img)
            tk.Label(frame_topo, image=self.logo, bg="#0f172a").pack()
        except:
            tk.Label(frame_topo, text="🏥", font=("Arial", 50),
                     bg="#0f172a", fg="white").pack()

        tk.Label(frame_topo, text="ATENDIMENTO HOSPITALAR",
                 font=("Arial", 22, "bold"),
                 bg="#0f172a", fg="#38bdf8").pack(pady=5)

        # FORM
        frame_form = tk.Frame(self.root, bg="#0f172a")
        frame_form.pack(pady=10)

        self.campos = {}

        campos = ["Nome", "Email", "Telefone"]

        for i, campo in enumerate(campos):
            tk.Label(frame_form, text=campo,
                     bg="#0f172a", fg="white").grid(row=i, column=0, pady=5)

            entry = tk.Entry(frame_form, width=30)
            entry.grid(row=i, column=1, pady=5)

            self.campos[campo] = entry

        # ESPECIALIDADE
        tk.Label(frame_form, text="Especialidade",
                 bg="#0f172a", fg="white").grid(row=3, column=0)

        self.combo = ttk.Combobox(frame_form,
                                 values=[
                                     "Clínico Geral",
                                     "Cardiologia",
                                     "Pediatria",
                                     "Ortopedia",
                                     "Dermatologia"
                                 ],
                                 state="readonly")
        self.combo.grid(row=3, column=1)

        # BOTÕES
        frame_btn = tk.Frame(self.root, bg="#0f172a")
        frame_btn.pack(pady=10)

        ttk.Button(frame_btn, text="Cadastrar", command=self.salvar).grid(row=0, column=0, padx=5)
        ttk.Button(frame_btn, text="Limpar", command=self.limpar).grid(row=0, column=1, padx=5)

        # BUSCA
        self.busca = ttk.Entry(self.root)
        self.busca.pack(pady=5)

        ttk.Button(self.root, text="Buscar", command=self.buscar).pack()

    # -------- TABELA --------
    def criar_tabela(self):
        colunas = ("Nome", "Email", "Telefone", "Especialidade")

        self.tree = ttk.Treeview(self.root, columns=colunas, show="headings")

        for col in colunas:
            self.tree.heading(col, text=col)

        self.tree.pack(fill="both", expand=True)

    # -------- VALIDAÇÃO --------
    def validar(self, dados):
        if not dados["Nome"]:
            messagebox.showerror("Erro", "Nome obrigatório")
            return False

        if "@" not in dados["Email"]:
            messagebox.showerror("Erro", "Email inválido")
            return False

        if len(dados["Telefone"]) < 10:
            messagebox.showerror("Erro", "Telefone inválido")
            return False

        if not self.combo.get():
            messagebox.showerror("Erro", "Escolha uma especialidade")
            return False

        return True

    # -------- SALVAR --------
    def salvar(self):
        dados = {
            "Nome": self.campos["Nome"].get(),
            "Email": self.campos["Email"].get(),
            "Telefone": self.campos["Telefone"].get(),
            "Especialidade": self.combo.get()
        }

        if not self.validar(dados):
            return

        arquivo_existe = os.path.isfile(ARQUIVO)

        with open(ARQUIVO, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=dados.keys())

            if not arquivo_existe:
                writer.writeheader()

            writer.writerow(dados)

        self.tree.insert("", tk.END, values=list(dados.values()))

        messagebox.showinfo("Sucesso", "Paciente cadastrado!")
        self.limpar()

    # -------- CARREGAR --------
    def carregar_dados(self):
        if not os.path.exists(ARQUIVO):
            return

        with open(ARQUIVO, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                self.tree.insert("", tk.END, values=list(row.values()))

    # -------- LIMPAR --------
    def limpar(self):
        for campo in self.campos.values():
            campo.delete(0, tk.END)
        self.combo.set("")

    # -------- BUSCAR --------
    def buscar(self):
        termo = self.busca.get().lower()

        for item in self.tree.get_children():
            self.tree.delete(item)

        if not os.path.exists(ARQUIVO):
            return

        with open(ARQUIVO, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                if termo in str(row).lower():
                    self.tree.insert("", tk.END, values=list(row.values()))


# -------- EXECUTAR --------
root = tk.Tk()
app = HospitalApp(root)
root.mainloop()