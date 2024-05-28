from customtkinter import *
from tkinter import ttk

import customtkinter as ctk

import lexer as Lexer

ventana = ctk.CTk(fg_color="#895490")
ventana.title("Aplicación analizador sintáctico")
ventana.geometry("800x600")
set_appearance_mode("dark")


titulo = CTkLabel(master=ventana, text="Analizador sintáctico", font=("Arial", 20, "bold"), text_color="#E2D2E5")
titulo.pack(pady=20)

codigo = ctk.CTkTextbox(master=ventana, height=200, width=500, text_color="#E2D2E5", font=("Courier new", 15), scrollbar_button_color="#E2D2E5", scrollbar_button_hover_color="#E2D2E5", border_color="#E2D2E5", border_width=2, fg_color="#895490")
codigo.pack(pady=5)



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

tabla_frame = ctk.CTkFrame(master=ventana, fg_color="#895490", height=100)
tabla_frame.pack(pady=20)

tabla = ttk.Treeview(master=tabla_frame, columns=("Token", "Tipo", "Significado"), show='headings')
tabla.heading("Token", text="Token")
tabla.heading("Tipo", text="Tipo")
tabla.heading("Significado", text="Significado")

tabla2 = ttk.Treeview(master=tabla_frame, columns=("Token", "Tipo", "Significado"), show='headings')
tabla2.heading("Token", text="Token")
tabla2.heading("Tipo", text="Tipo")
tabla2.heading("Significado", text="Significado")

def llenar():
    texto_entrada = codigo.get("1.0", "end-1c")
    print(texto_entrada)
    lexer = Lexer.Lexer(texto_entrada)
    tokens = lexer.separarPalabrasYReconocer()
    matriz = lexer.crearMatrizTokens()
    print(matriz)
    for fila in matriz:
        tabla.insert("", "end", values=fila)

boton = ctk.CTkButton(master=ventana, text="Analizar", command=llenar, text_color="#E2D2E5", fg_color="transparent", border_color="#E2D2E5", border_width=1, hover_color="#E2D2E5", font=("Arial", 12, "bold"))
boton.pack(pady=10)

tabla.pack()
tabla2.pack()

ventana.mainloop()


