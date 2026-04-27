import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter
from tabulate import tabulate


def show_results():
    top = customtkinter.CTkToplevel()
    top.geometry("800x400+450+300")
    top.title("Tabla generada")

    headings = ["Password", "Encrypted", "Hora"]
    tree = ttk.Treeview(top, show="headings", columns=headings)

    for col in headings:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor="center")

    tree.pack(expand=True, fill="both")
    return tree


def generate_file(tree):
    if not tree.get_children():
        messagebox.showwarning("Advertencia", "La tabla está vacía!!")
        return
    
    with open("Encriptamientos.txt", "w") as file:
        resultados = []
        for item in tree.get_children():
            resultados.append(tree.item(item, "values"))

        tabla = tabulate(resultados, headers=["Passwords", "Encrypted", "Hora"])
        file.write(tabla)

    messagebox.showinfo("Éxito", "Archivo generado correctamente")