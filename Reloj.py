import tkinter as tk
from datetime import datetime
from tkinter import colorchooser
import json
import os
from tkinter import font
import ctypes

mutex = ctypes.windll.kernel32.CreateMutexW(None, False, "RelojWidgetUnico")

if ctypes.windll.kernel32.GetLastError() == 183:
    raise SystemExit

ARCHIVO_CONFIG = "config.json"

configuracion = {
    "color": "blue",
    "tamano": 40,
    "x": 500,
    "y": 200,
    "mostrar_fecha": True,
    "formato_24hs":True,
    "tipografia": "Arial"
}

def guardar_configuracion():
    with open(ARCHIVO_CONFIG, "w") as archivo:
        json.dump(configuracion, archivo, indent = 4)

def cargar_configuracion():
    if os.path.exists(ARCHIVO_CONFIG):
        with open(ARCHIVO_CONFIG, "r") as archivo:
            datos = json.load(archivo)

        for clave in configuracion:
            if clave not in datos:
                datos[clave] = configuracion[clave]

        return datos
    return configuracion

configuracion = cargar_configuracion()

ventana = tk.Tk()
ventana.title("RELOJ")
ventana.geometry("")
ventana.configure(bg="black")
ventana.wm_attributes("-transparentcolor", "black")
ventana.overrideredirect(True)
ventana.geometry(f"+{configuracion['x']}+{configuracion['y']}")

pos_x = 0
pos_y = 0

def comenzar_movimiento(event):
    global pos_x,pos_y

    pos_x = event.x
    pos_y = event.y

def mover_ventana(event):
    x = ventana.winfo_x() + event.x - pos_x
    y = ventana.winfo_y() + event.y - pos_y

    ventana.geometry(f"+{x}+{y}")

    configuracion["x"] = x
    configuracion["y"] = y


def terminar_movimiento(event):
    guardar_configuracion()

def cambiar_color():
    color = colorchooser.askcolor(title="Elegir color")

    if color[1]:
        reloj.config(fg=color[1])
        fecha.config(fg=color[1])

        configuracion["color"] = color[1]
        

def cambiar_tamano(tamano):
    tamano = int(tamano)

    reloj.config(font=(configuracion["tipografia"], tamano))
    fecha.config(font=(configuracion["tipografia"], int(tamano/2.5)))

    

    ventana.update_idletasks()
    ventana.geometry("")


def cambiar_fecha(mostrar):
    if mostrar:
        fecha.pack()
    else:
        fecha.pack_forget()

    ventana.update_idletasks()
    ventana.geometry("")
formato_actual= configuracion["formato_24hs"]

def cambiar_formato(formato):

    global formato_actual
    formato_actual = formato
    ahora = datetime.now()

    if formato:
        hora_actual = ahora.strftime("%H:%M")
    else:
        hora_actual = ahora.strftime("%I:%M %p")

    reloj.config(text=hora_actual)


tipografias = [
    "Arial",
    "Cinzel",
    "Cinzel ExtraBold",
    "Cinzel Medium",
    "Cinzel SemiBold",
    "Cinzel Black",
    "Digital-7",
    "Digital-7 Italic",
    "Digital-7 Mono",
    "DS-Digital",
    "Orbitron",
    "Orbitron Black",
    "Orbitron ExtraBold",
    "Orbitron Medium",
    "Orbitron SemiBold",
    "Press Start 2P",
    "Share Tech Mono",
    "VT323"
]
def cambiar_tipografia(tipografia):
    configuracion["tipografia"] = tipografia
    reloj.config(font=(tipografia, configuracion["tamano"]))
    fecha.config(font=(tipografia, int (configuracion["tamano"]/2.5)))

    ventana.update_idletasks()
    ventana.geometry("")

def abrir_configuracion():
        configuracion_ventana = tk.Toplevel(ventana)
        configuracion_ventana.title("Configuracion")
        configuracion_ventana.geometry("300x450")

        tamano_original = configuracion["tamano"]
        color_original = configuracion["color"]
        mostrar_fecha_original = configuracion["mostrar_fecha"]
        formato_24hs_original = configuracion["formato_24hs"]
        tipografia_original = configuracion["tipografia"]

        tk.Label(configuracion_ventana, text = "Configuracion del reloj", 
                 font = ("Arial", 16)). pack(pady=10)

        tk.Label(configuracion_ventana, text = "Tipografias"). pack()

        tipografia_seleccionada = tk.StringVar(value=configuracion["tipografia"])
        selector_tipografia = tk.OptionMenu(
                    configuracion_ventana,
                    tipografia_seleccionada,
                    *tipografias,
                    command=lambda fuente: cambiar_tipografia(fuente)
                )
        selector_tipografia.pack(pady=5)
        
        tk.Label(configuracion_ventana, text="Tamaño").pack()

        selector_tamano = tk.Scale(configuracion_ventana,
                                   from_=20, to=80, orient="horizontal",
                                   command = cambiar_tamano)

        mostrar_fecha = tk.BooleanVar()
        mostrar_fecha.set(configuracion["mostrar_fecha"])

        
        
        def guardar_cambios():
            configuracion["tamano"] = int(selector_tamano.get())
            configuracion["color"] =  reloj.cget("fg")
            configuracion["mostrar_fecha"] = mostrar_fecha.get()
            configuracion["formato_24hs"] = formato_24hs.get()
            configuracion["tipografia"] = tipografia_seleccionada.get()

            guardar_configuracion()
            cambiar_formato(formato_24hs.get())
            configuracion_ventana.destroy()

        def cancelar_cambios():
            cambiar_tamano(tamano_original)
            selector_tamano.set(tamano_original)
            configuracion["tamano"] = tamano_original

            reloj.config(fg=color_original)
            fecha.config(fg=color_original)
            configuracion["color"] = color_original

            cambiar_tipografia(tipografia_original)
            tipografia_seleccionada.set(tipografia_original)
            configuracion["tipografia"] = tipografia_original

            if mostrar_fecha_original:
                fecha.pack()
            else:
                fecha.pack_forget()

            configuracion["mostrar_fecha"] = mostrar_fecha_original
            formato_24hs.set(formato_24hs_original)
            configuracion["formato_24hs"] = formato_24hs_original
            cambiar_formato(formato_24hs_original)

            configuracion_ventana.destroy()

        selector_tamano.set(configuracion["tamano"])
        selector_tamano.pack()

        
        tk.Button(configuracion_ventana, text = "Cambiar color",
                                  command = cambiar_color).pack(pady=10)

        check_fecha = tk.Checkbutton(
                    configuracion_ventana, text = "Mostrar fecha",
                    variable = mostrar_fecha,
                    command=lambda: cambiar_fecha(mostrar_fecha.get())
                )
        
        check_fecha.pack(pady=10)

        formato_24hs = tk.BooleanVar()
        formato_24hs.set(configuracion["formato_24hs"])
        check_formato = tk.Checkbutton(
                   configuracion_ventana,
                   text = "Formato 24 Horas",
                   variable = formato_24hs,
                   command=lambda: cambiar_formato(formato_24hs.get())
               )
       
        check_formato.pack(pady=5)

        
        tk.Button(configuracion_ventana, text="Guardar", 
                  command = guardar_cambios).pack(pady=10)

        tk.Button(configuracion_ventana, text = "Cancelar",
                  command = cancelar_cambios).pack(pady=5)
        

        configuracion_ventana.protocol(
            "WM_DELETE_WINDOW", cancelar_cambios
        )



reloj = tk.Label(ventana, font=(configuracion["tipografia"], configuracion["tamano"]),
                 bg="black", fg=configuracion["color"])
reloj.pack() 

fecha = tk.Label(ventana, font=(configuracion["tipografia"], int(configuracion["tamano"]/2.5)),
               bg="black", fg=configuracion["color"])
if configuracion["mostrar_fecha"]:
    fecha.pack()


reloj.bind("<Button-1>", comenzar_movimiento)
reloj.bind("<B1-Motion>", mover_ventana)
reloj.bind("<ButtonRelease-1>", terminar_movimiento)

fecha.bind("<Button-1>", comenzar_movimiento)
fecha.bind("<B1-Motion>", mover_ventana)
fecha.bind("<ButtonRelease-1>", terminar_movimiento)


menu = tk.Menu(ventana, tearoff=0)
menu_tamano = tk.Menu(ventana, tearoff=0)

menu.add_command(label = "Configuracion", command = abrir_configuracion)

menu.add_command(label = "Cerrar", 
                 command=ventana.destroy)

     


def mostrar_menu(event):
    menu.post(event.x_root, event.y_root)

reloj.bind("<Button-3>" , mostrar_menu)
fecha.bind("<Button-3>", mostrar_menu)


def actualizar_reloj():
    ahora = datetime.now()

    
    if formato_actual:
        hora_actual = ahora.strftime("%H:%M")
    else:
        hora_actual = ahora.strftime("%I:%M %p")

    fecha_actual = ahora.strftime("%d/%m/%Y")

    fecha.config(text=fecha_actual)
    reloj.config(text=hora_actual)

    ventana.after(1000, actualizar_reloj)

actualizar_reloj()

ventana.mainloop()