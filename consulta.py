import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from mainScreen import MainScreen

class Consulta():

    def __init__(self, root_parameter):
        self.root = root_parameter
        self.montar_tela_consulta()
        self.consulta_func()
        self.root.mainloop()

    def montar_tela_consulta(self):
        self.root.geometry("1200x720")
        self.root.title("Stock Management System")
        self.root.resizable(False, False)
        self.root.configure(background="#f9f6ee")

    def  consulta_func(self):
        self.button_consultar = Button(self.root, text="Consultar")
        self.root.button_consultar.place(self.button_consultar, x=100, y=100, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    Consulta(root)