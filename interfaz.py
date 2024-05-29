from customtkinter import *
from tkinter import ttk
import tkinter as tk

import customtkinter as ctk
import lexer as Lexer
import dibujarAFD as DibujarAFD

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

codigo = ctk.CTkTextbox(master=texto_frame, height=500, width=450, text_color="#E2D2E5", font=("Courier new", 15), scrollbar_button_color="#E2D2E5", scrollbar_button_hover_color="#E2D2E5", border_color="#E2D2E5", border_width=2, fg_color="#895490")
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

tabla2 = ttk.Treeview(master=tabla_frame, columns=("Metodo", "Incompleto o completo"), show='headings')
tabla2.heading("Metodo", text="Metodo")
tabla2.heading("Incompleto o completo", text="Incompleto o completo")
tabla2.pack(side="top", padx=10, pady=10, fill="both", expand=True)

# Crear un frame para los botones y usar pack para colocarlos uno debajo del otro
botones_frame = ctk.CTkFrame(master=ventana, fg_color="#895490")
botones_frame.pack(side="left", padx=10, pady=200, fill="y")

def llenar():
    for item in tabla.get_children():
        tabla.delete(item)
    for item in tabla2.get_children():
        tabla2.delete(item)
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

def crearAutomatas():
    texto_entrada = codigo.get("1.0", "end-1c")
    print(texto_entrada)
    lexer = Lexer.Lexer(texto_entrada)
    tokens = lexer.separarPalabrasYReconocer()
    print(tokens)
    for token in tokens: 
        if token.tipo!="Desconocido":
            cadena = token.token
            DibujarAFD.draw_dfa(cadena)
    abrir_ventana_emergente()


def abrir_ventana_emergente():
    ventana_emergente = CTkToplevel()
    ventana_emergente.title("")
    ventana_emergente.geometry("400x200")
    
    label_emergente = CTkLabel(master=ventana_emergente, text="Los autómatas se generaron correctamente en la carpeta", font=("Arial", 14), wraplength=350)
    label_emergente.pack(pady=20)
    
    boton_cerrar = CTkButton(master=ventana_emergente, text="Cerrar", command=ventana_emergente.destroy)
    boton_cerrar.pack(pady=10)
    ventana_emergente.focus_set()

boton = ctk.CTkButton(master=botones_frame, text="Analizar", command=llenar, text_color="#E2D2E5", fg_color="transparent", border_color="#E2D2E5", border_width=1, hover_color="#E2D2E5", font=("Arial", 12, "bold"))
boton.pack(side="top", padx=10, pady=10)

boton2 = ctk.CTkButton(master=botones_frame, text="Crear autómatas", command=crearAutomatas, text_color="#E2D2E5", fg_color="transparent", border_color="#E2D2E5", border_width=1, hover_color="#E2D2E5", font=("Arial", 12, "bold"))
boton2.pack(side="top", padx=10, pady=10)



ventana.mainloop()
