import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *


class MainScreen():
    def __init__(self, root_parameter):
        self.root = root_parameter
        self.montar_tela_principal()
        self.design()
        self.root.protocol("WM_DELETE_WINDOW", self.confirm_exit)
        self.root.mainloop()

    def montar_tela_principal(self):
        self.root.geometry("1200x720")
        self.root.title("Stock Management System")
        self.root.resizable(False, False)
        self.root.configure(background="#f9f6ee")

    def design(self):
        self.menu_bar = tk.Menu(self.root, tearoff=0)
        self.cadastro_file = tk.Menu(self.menu_bar, tearoff=0)
        self.cadastro_file.add_command(label="1-Cadastrar")
        self.cadastro_file.add_command(label="2-Listar")
        self.menu_bar.add_cascade(label="1-Cadastrar", menu=self.cadastro_file)
        self.editar_file = tk.Menu(self.menu_bar, tearoff=0)
        self.editar_file.add_command(label="1-Editar produtos")
        self.editar_file.add_command(label="2-Editar fornecedores")
        self.menu_bar.add_cascade(label="2-Editar", menu=self.editar_file)
        self.menu_bar.add_command(label="3-Excluir")
        self.menu_bar.add_command(label="4-Configuração")
        self.menu_bar.add_command(label="5-Sair", command=self.confirm_exit)

        self.root.config(menu=self.menu_bar)

    def confirm_exit(self):
        if messagebox.askyesno("Saída", "Você tem certeza que deseja sair?"):
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    MainScreen(root)