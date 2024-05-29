import tkinter as tk
from PIL import Image, ImageTk
import pydot

def draw_dfa(cadena):
    graph = pydot.Dot(graph_type='digraph')

    states = ['q{}'.format(i) for i in range(len(cadena) + 1)]

    for state in states:
        node = pydot.Node(state)
        if state == 'q{}'.format(len(cadena)):
            node.set_shape('doublecircle')
        graph.add_node(node)

    for i in range(len(cadena)):
        graph.add_edge(pydot.Edge('q{}'.format(i), 'q{}'.format(i + 1), label=cadena[i]))

    nombre = "automatas/"+cadena+".png"
    graph.write_png(nombre)
    #show_image(nombre)

def show_image(image_path):
    root = tk.Tk()
    root.title("DFA Visualizer")

    # Cargar la imagen
    img = Image.open(image_path)

    # Convertir la imagen a formato Tkinter
    img_tk = ImageTk.PhotoImage(img)

    # Crear un lienzo con una barra de desplazamiento vertical
    canvas = tk.Canvas(root, width=img_tk.width(), height=img_tk.height())
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.create_image(0, 0, anchor="nw", image=img_tk)

    # Configurar el tamaño del lienzo para que coincida con el tamaño de la imagen
    canvas.config(scrollregion=canvas.bbox("all"))

    root.mainloop()

if __name__ == "__main__":
    cadena = "combina_con" # Cadena larga para probar la barra de desplazamiento
    draw_dfa(cadena)
