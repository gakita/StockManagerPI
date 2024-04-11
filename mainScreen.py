import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from commons import Commons



class MainScreen(Commons):
    def __init__(self,root_parameter):
        self.root = root_parameter
        self.montar_tela_principal()
        self.design()
        self.buttons_design()
        self.root.protocol("WM_DELETE_WINDOW", self.confirm_exit)
        self.root.mainloop()

    def montar_tela_principal(self):
        self.root.geometry("1200x720")
        self.root.title("Stock Management System")
        self.root.resizable(False, False)
        self.root.configure(background="#f9f6ee")

    def buttons_design(self):
        consultar_button = Button(text="F1\nConsultar")
        consultar_button.configure(background="black", foreground="white")
        consultar_button.place(x=10, y=10, width=100, height=100)
        nova_venda_button = self.tk.Button(text="F2\nNova Venda")
        total_item_button = self.tk.Button(text="F3\nTotal do Item")
        tabela_precos_button = self.tk.Button(text="F4\nTabela de preços")
        quantidade_button = self.tk.Button(text="F5\nQuantidade")
        valor_button = self.tk.Button(text="F6\nValor")
        cancelar_item_button = self.tk.Button(text="F7\nCancelar Item")
        excluir_venda_button = self.tk.Button(text="F8\nExcluir Venda")








if __name__ == "__main__":
    root = tk.Tk()
    MainScreen(root)