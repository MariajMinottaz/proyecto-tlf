from customtkinter import *
from tkinter import ttk
import tkinter as tk

import customtkinter as ctk
import lexer as Lexer

ventana = ctk.CTk(fg_color="#895490")
ventana.title("Aplicación analizador sintáctico")

ancho_pantalla = ventana.winfo_screenwidth()-100
alto_pantalla = ventana.winfo_screenheight()-100
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")
set_appearance_mode("dark")

texto_frame = ctk.CTkFrame(master=ventana, fg_color="#895490")
texto_frame.pack(side="left", padx=10, pady=10, fill="y")

titulo = CTkLabel(master=texto_frame, text="Analizador sintáctico", font=("Arial", 20, "bold"), text_color="#E2D2E5")
titulo.pack(pady=20)

codigo = ctk.CTkTextbox(master=texto_frame, height=500, width=500, text_color="#E2D2E5", font=("Courier new", 15), scrollbar_button_color="#E2D2E5", scrollbar_button_hover_color="#E2D2E5", border_color="#E2D2E5", border_width=2, fg_color="#895490")
codigo.pack(pady=5)

tabla_frame = ctk.CTkFrame(master=ventana, fg_color="#895490")
tabla_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)

style = ttk.Style()
style.theme_use("clam")

style.configure("Treeview",
                background="#895490",
                foreground="#E2D2E5",
                fieldbackground="#895490",
                font=("Courier new", 10),
                bordercolor="#E2D2E5",
                borderwidth=0)

style.configure("Treeview.Heading",
                background="#895490",
                foreground="#E2D2E5",
                bordercolor="#E2D2E5",
                font=("Courier new", 10, "bold"),
                borderwidth=0)

style.map("Treeview",
          background=[('selected', '#895490')],
          foreground=[('selected', '#E2D2E5')])

tabla = ttk.Treeview(master=tabla_frame, columns=("Token", "Tipo", "Significado"), show='headings')
tabla.heading("Token", text="Token")
tabla.heading("Tipo", text="Tipo")
tabla.heading("Significado", text="Significado")
tabla.pack(side="top", padx=10, pady=10, fill="both", expand=True)

tabla2 = ttk.Treeview(master=tabla_frame, columns=("Metodo"), show='headings')
tabla2.heading("Metodo", text="Metodo")
tabla2.pack(side="top", padx=10, pady=10, fill="both", expand=True)

def llenar():
    texto_entrada = codigo.get("1.0", "end-1c")
    print(texto_entrada)
    lexer = Lexer.Lexer(texto_entrada)
    tokens = lexer.separarPalabrasYReconocer()
    matriz = lexer.crearMatrizTokens()
    print(matriz)
    for fila in matriz:
        tabla.insert("", "end", values=fila)
    metodos = lexer.obtenerMetodosIncompletos()
    matriz2 = lexer.crearMatrizMetodos()
    print(matriz2)
    for metodo in matriz2:
        tabla2.insert("", "end", values=metodo)

boton = ctk.CTkButton(master=ventana, text="Analizar", command=llenar, text_color="#E2D2E5", fg_color="transparent", border_color="#E2D2E5", border_width=1, hover_color="#E2D2E5", font=("Arial", 12, "bold"))
boton.pack(side="left", padx=10, pady=10, expand=True)

ventana.mainloop()
