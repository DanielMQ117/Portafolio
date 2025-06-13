import os
import sys
from tkinter import *
from random import randint
from tkinter import messagebox as MessageBox

# creamos nuestra raiz
root = Tk()

primaryFont = ("Garamond", 20, "bold", "italic")
secondaryFont = ("Garamond", 16, "bold", "italic")

# pixeles
initialPositionY = 200
anchoDelBoton = 46
altoDelBoton = 42


def resource_path(relative_path):
    """Devuelve la ruta absoluta, compatible con PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def newWindow():
    """ Crea una nueva ventana y muestra un mensaje de aceptación """
    isOk = MessageBox.showinfo("💓", "¡Sabía Que Aceptarías! 🌷")
    if isOk:
        root.quit()


def onButton(event):
    """ Mueve el botón a una nueva posición aleatoria dentro de la ventana """
    global anchoDelBoton, altoDelBoton
    global w, h

    x = randint(4, w - 60)
    y = randint(4, h - 60)

    # Posicion de la esquina superior izquierda del botón
    posicionActualX = buttom2.winfo_x()
    posicionActualY = buttom2.winfo_y()

    if posicionActualX < x < (posicionActualX + anchoDelBoton):
        x = x + anchoDelBoton + 10
        if x > (w - anchoDelBoton):
            x = x - 2*(anchoDelBoton + 10)

    if posicionActualY < y < (posicionActualY + altoDelBoton):
        y = y + altoDelBoton + 10
        if y > (h - altoDelBoton):
            y = y - 2*(altoDelBoton + 10)

    buttom2.place(x=x, y=y)


# abrimos la foto
bg_path = resource_path("BG_2.gif")
background = PhotoImage(file=bg_path)

# obtener el ancho y alto de la imagen
w = background.width()
h = background.height()

root.title("Project")
# no permite modificar el tamaño de la ventana en 2D
root.resizable(0, 0)
root.geometry(f"{w}x{h}")                   # aplicar geometria
icon_path = resource_path("corazones.ico")
root.iconbitmap(icon_path)
root.state(newstate="iconic")

frame0 = Frame(root)
frame0.pack(fill="both")
frame0.config(width=w, height=h)        # medida del marco

label0 = Label(frame0, image=background, bd=0)
label0.pack(side="top", anchor="n")

label1 = Label(frame0, text="¿ Puedo Ser Tu Ingeniero ? ",
               bg="#feeaec", bd=0)         # R:254  G:234  B:236
label1.config(font=primaryFont)
label1.place(x=58, y=78)

buttom1 = Button(root, text="Sí ", justify="center", command=newWindow)
buttom1.config(width=3, height=1, bd=2, bg="#d8f0b6", relief="flat", overrelief="raised",
               cursor="heart")           # R:216  G:240  B:182
buttom1.config(font=secondaryFont)
buttom1.place(x=100, y=initialPositionY)

buttom2 = Button(root, text="No ", justify="center",
                 state="normal")               # R:250  G:232  B:196
buttom2.config(width=3, height=1, bd=2, bg="#fae8c4",
               relief="flat", overrelief="raised")
buttom2.config(font=secondaryFont)
buttom2.place(x=260, y=initialPositionY)

buttom2.bind("<Enter>", onButton)             # Move Button
buttom2.bind("<ButtonPress>", onButton)       # Move Button
buttom2.bind("<MouseWheel>", onButton)        # Move Button

root.mainloop()


# Instalar biblioteca: pip install pyinstaller
# Ejecutar comando: pyinstaller --noconsole --onefile --add-data "BG_2.gif;." --add-data "corazones.ico;." App_M.py
# Ejecutar el archivo .exe generado en la carpeta "dist"
