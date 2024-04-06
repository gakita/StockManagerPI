import tkinter as tk
from tkinter import messagebox
from mainScreen import MainScreen
import bcrypt

class LoginScreen():
    def __init__(self, root_parameter):
        self.root = root_parameter
        self.montar_tela_login()
        self.login_design()
        self.root.mainloop()

    def montar_tela_login(self):
        self.root.geometry("300x300")
        self.root.title("Login")
        self.root.resizable(False, False)
        self.root.configure(background="#ffffff")

    def login_design(self):
        self.username_label = tk.Label(self.root, text="Username:", bg="#ffffff")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root, width=30)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password:", bg="#ffffff")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, width=30, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.root, text="Login", command=self.login_validation, bg="#72da70", fg="#000")
        self.login_button.pack()

    def login_validation(self):
        real_password = ""

        salts = bcrypt.gensalt()
        real_password_hash = bcrypt.hashpw(real_password.encode('utf-8'), salts)

        username = self.username_entry.get()
        password = self.password_entry.get()

        self.username_entry.bind("<Return>", lambda event: self.login_validation())
        self.password_entry.bind("<Return>", lambda event: self.login_validation())

        password_hash = bcrypt.hashpw(password.encode('utf-8'), salts)

        if username == "" and password_hash == real_password_hash:
            print(real_password)
            print(password_hash)
            print(real_password_hash)
            messagebox.showinfo("Login", "Login efetuado com sucesso!")
            self.username_label.destroy()
            self.username_entry.destroy()
            self.password_label.destroy()
            self.password_entry.destroy()
            self.login_button.destroy()
            MainScreen(self.root)
        else:
            messagebox.showerror("Erro", "Login inválido. Verifique os dados e tente novamente.")
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            print(real_password)
            print(password)
            print(password_hash)
            print(real_password_hash)




if __name__ == "__main__":
    root = tk.Tk()
    LoginScreen(root)