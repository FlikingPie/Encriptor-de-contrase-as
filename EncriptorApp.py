import customtkinter
import bcrypt
import tkinter as tk
from datetime import datetime
from hashing import show_results
from hashing import generate_file
from tkinter import messagebox

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")


class EncryptorApp:
    def menu(self):
        self.barra_menu = tk.Menu(self.root, tearoff=0)
        self.root.config(menu=self.barra_menu)

        self.menu_ver_contraseñas = tk.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="Contraseñas y encriptamientos", menu=self.menu_ver_contraseñas)

        self.menu_archivo = tk.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="Generar archivo", menu=self.menu_archivo)

        self.menu_ver_contraseñas.add_command(label="Mostrar contraseñas y encriptamientos", command=self.mostrar_encriptamientos)
        self.menu_archivo.add_command(label="Generar txt", command=self.generar_archivo )

    def __init__(self, root):
        self.root = root
        self.root.geometry("500x350+450+250")
        self.root.title("Passwords encryptor")
        self.root.resizable(False, False)

        self.menu()

        self.label = customtkinter.CTkLabel(self.root, text="Escriba la contraseña" ,font=("Arial", 18, "bold"))
        self.label.pack(side="top")

        self.entry = customtkinter.CTkEntry(self.root, width=100)
        self.entry.pack(pady=10)

        self.boton = customtkinter.CTkButton(self.root, text="ENCRIPTAR", width=100, command=self.ingresar_contraseña)
        self.boton.pack(pady=10)


    def ingresar_contraseña(self):
        password = self.entry.get()
        if not password:
            messagebox.showwarning("Advertencia", "Debe ingresar la contraseña!!")
            return
        
        if not hasattr(self, "tree"):
            self.tree = show_results()
        
        pwd = password.encode("utf-8")
        sal = bcrypt.gensalt()
        encript = bcrypt.hashpw(pwd, sal)

        #Hora
        hora_actual = datetime.now()
        h = hora_actual.strftime("%H:%M:%S")

        self.tree.insert("", "end", values=(password, encript, h))
        self.entry.delete(0, tk.END)


    def mostrar_encriptamientos(self):
        self.tree = show_results()

    def generar_archivo(self):
        if not hasattr(self, "tree"): # Comprueab si el objeto 'tabla' existeSS
           messagebox.showwarning("Advertencia", "Primero debes abrir la tabla")
           return

        generate_file(self.tree)
