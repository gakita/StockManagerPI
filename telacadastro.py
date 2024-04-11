import tkinter as tk
from tkinter import messagebox
from tkinter import *
from commons import Commons


class telaCadastro(Commons):

    def __init__(self, root):
        self.root = root
        self.montar_tela_cadastro()
        self.design()
        self.root.mainloop()

    def montar_tela_cadastro(self):
        self.root.geometry("300x300")
        self.root.title("Cadastrar")
        self.root.resizable(False, False)
        self.root.configure(background="#ffffff")

    def button_design(self):
        self.cadastrar_button = tk.Button(self.root, text="Cadastrar", command=self.cadastro, bg="#72da70", fg="#000")



if __name__ == "__main__":
    root = tk.Tk()
    telaCadastro(root)