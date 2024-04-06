import tkinter as tk
from tkinter import messagebox
from tkinter import *


class telaCadastro():

    def __init__(self, root):
        self.root = root
        self.montar_tela_cadastro()
        self.design()
        self.root.mainloop()

    def montar_tela_cadastro(self):
        self.root.geometry("300x300")
        self.root.title("Login")
        self.root.resizable(False, False)
        self.root.configure(background="#ffffff")

    def design(self):
        self.menu_bar = tk.Menu(self.root, tearoff=0)
        self.cadastro_file = tk.Menu(self.menu_bar, tearoff=0)
        self.cadastro_file.add_command(label="1-Cadastrar")
        self.cadastro_file.add_command(label="2-Listar")
        self.menu_bar.add_cascade(label="1-Cadastrar", menu=self.cadastro_file)
        self.editar_file = tk.Menu(self.menu_bar, tearoff=0)
        self.editar_file.add_command(label="1-Editar produtos")
        self.editar_file.add_command(label="2-Editar fornecedores")
        self.excluir_file = tk.Menu(self.menu_bar, tearoff=0)
        self.editar_file.add_command(label="3-Excluir produto")
        self.editar_file.add_command(label="4-Excluir fornecedores")
        self.menu_bar.add_cascade(label="2-Editar", menu=self.editar_file)
