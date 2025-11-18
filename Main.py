import tkinter as tk
import datetime
from PIL import Image, ImageTk
from tkinter import Toplevel, ttk, messagebox

# clases definidas en FuncionesVet
from FuncionesVet import Mascota, Duenio, Veterinaria 

# ==============================================================================
# # Colores y estilos CYBERPUNK
# ==============================================================================
COLOR_PRIMARY = "#00F0FF"    # Aqua neón brillante
COLOR_ACCENT = "#FF00FF"     # Magenta neón (Hover)
COLOR_DARK = "#0D0D0D"       # Negro casi puro (Fondo principal)
COLOR_BG_LIGHT = "#1A1A1A"   # Gris oscuro (No usado en este diseño final)
COLOR_BG_CARD = "#2A2A2A"    # Gris medio (No usado en este diseño final)
COLOR_CANVAS = "#000000"     # Negro absoluto
COLOR_TEXT_LIGHT = "#E0E0E0"  # Blanco grisáceo para texto estático
COLOR_TEXT_ACCENT = "#00F0FF" # Aqua neón para texto de énfasis

FONT_PRIMARY = ("Roboto Mono", 12) 
FONT_TITLE = ("Electrolize", 20, "bold") 
FONT_SUBTITLE = ("Electrolize", 16) 

# --------------------- Instancia Veterinaria ---------------------
vet = Veterinaria("Clínica La Huellita Cyberpunk")

# ==============================================================================
# # Función: Botón (Lógica de Colores de Hover)
# ==============================================================================
def crear_boton_moderno(parent, texto, comando):
    """Crea un botón con estilos modernos y efecto hover (Dark/Neon)."""
    
    # Define la variable frame_btn (Solución al error de 'not defined')
    frame_btn = tk.Frame(parent, bg=COLOR_DARK) 
    frame_btn.pack(pady=2, ipadx=2, ipady=2, fill="x") 
    
    # Configuración base del botón: Fondo oscuro, Texto neón
    boton = tk.Button(frame_btn, text=texto, font=FONT_PRIMARY, 
                      bg=COLOR_DARK, fg=COLOR_PRIMARY, bd=0, relief="flat",
                      activebackground=COLOR_ACCENT, activeforeground=COLOR_DARK, 
                      command=comando)
    boton.pack(ipadx=10, ipady=8, fill="x")
    
    # Efecto Hover: Invierte los colores al entrar (Botón neón, Texto oscuro)
    def on_enter(e):
        boton.config(bg=COLOR_PRIMARY, fg=COLOR_DARK, relief="raised")
    
    # Efecto Leave: Vuelve a los colores oscuros originales
    def on_leave(e):
        boton.config(bg=COLOR_DARK, fg=COLOR_PRIMARY, relief="flat")
    
    boton.bind("<Enter>", on_enter)
    boton.bind("<Leave>", on_leave)
    
    return frame_btn

# ==============================================================================
# # Función: Treeview (Toplevel)
# ==============================================================================
def mostrar_tabla_moderna(title, columnas, datos):
    """Muestra una nueva ventana con una tabla de datos (Treeview) y un campo de búsqueda."""
    ventana = Toplevel(root)
    ventana.title(title)
    ventana.geometry("700x500") # Aumento de tamaño para la tabla
    ventana.grab_set()
    ventana.focus_set()
    ventana.configure(bg=COLOR_DARK) # Fondo oscuro

    frame_tabla = tk.Frame(ventana, bg=COLOR_DARK, padx=10, pady=10)
    frame_tabla.pack(fill="both", expand=True)

    # Campo de búsqueda
    busqueda_var = tk.StringVar()
    tk.Label(frame_tabla, text="Buscar:", bg=COLOR_DARK, fg=COLOR_TEXT_LIGHT, font=FONT_PRIMARY).pack(anchor="nw") # Texto claro
    tk.Entry(frame_tabla, textvariable=busqueda_var, font=FONT_PRIMARY, bg=COLOR_CANVAS, fg=COLOR_TEXT_LIGHT, insertbackground=COLOR_ACCENT).pack(anchor="nw", fill="x", pady=(0, 10)) # Entrada cyberpunk

    # Estilo del Treeview (Ajuste para cyberpunk)
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background=COLOR_BG_CARD, foreground=COLOR_TEXT_LIGHT, 
                    rowheight=28, fieldbackground=COLOR_BG_CARD, font=FONT_PRIMARY,
                    bordercolor=COLOR_PRIMARY, borderwidth=1)
    style.map("Treeview", background=[("selected", COLOR_ACCENT)], foreground=[("selected", COLOR_DARK)]) 
    style.configure("Treeview.Heading", font=FONT_PRIMARY, background=COLOR_DARK, foreground=COLOR_TEXT_ACCENT) 
    
    tree = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
    
    # Scrollbars
    scrollbar_y = ttk.Scrollbar(frame_tabla, orient="vertical", command=tree.yview)
    scrollbar_x = ttk.Scrollbar(frame_tabla, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
    scrollbar_y.pack(side="right", fill="y")
    scrollbar_x.pack(side="bottom", fill="x")
    tree.pack(fill="both", expand=True)

    # Configuración de columnas
    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor="center", stretch=True)

    # Función de filtrado dinámico
    def filtrar(*args):
        query = busqueda_var.get().lower()
        tree.delete(*tree.get_children())
        for fila in datos:
            if any(query in str(valor).lower() for valor in fila):
                tree.insert("", "end", values=fila)

    busqueda_var.trace_add("write", filtrar)
    filtrar()

# ==============================================================================
# # Funciones GUI de Operaciones (APLICACIÓN DE ESTILO CYBERPUNK)
# ==============================================================================

# Registrar Dueño
def registrar_duenio_gui():
    ventana = Toplevel(root)
    ventana.title("Registrar Dueño")
    ventana.geometry("400x250")
    ventana.grab_set()
    ventana.focus_set()
    ventana.configure(bg=COLOR_DARK) # Fondo oscuro

    # Labels y Entries con estilo Cyberpunk
    tk.Label(ventana, text="Nombre del dueño:", bg=COLOR_DARK, fg=COLOR_TEXT_LIGHT, font=FONT_PRIMARY).pack(anchor="nw", padx=20, pady=(20,5))
    nombre_var = tk.StringVar()
    tk.Entry(ventana, textvariable=nombre_var, font=FONT_PRIMARY, bg=COLOR_CANVAS, fg=COLOR_PRIMARY, insertbackground=COLOR_ACCENT).pack(anchor="nw", padx=20, fill="x")

    tk.Label(ventana, text="Teléfono:", bg=COLOR_DARK, fg=COLOR_TEXT_LIGHT, font=FONT_PRIMARY).pack(anchor="nw", padx=20, pady=(15,5))
    telefono_var = tk.StringVar()
    tk.Entry(ventana, textvariable=telefono_var, font=FONT_PRIMARY, bg=COLOR_CANVAS, fg=COLOR_PRIMARY, insertbackground=COLOR_ACCENT).pack(anchor="nw", padx=20, fill="x")

    def guardar():
        # ... (Lógica de guardado)
        nombre = nombre_var.get().strip()
        telefono = telefono_var.get().strip()
        if nombre and telefono:
            d = Duenio(nombre, telefono)
            
            exito = vet.registrar_duenio(d)
            if exito:
                messagebox.showinfo("Éxito", f"Dueño {nombre} registrado correctamente")
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo registrar el dueño")
        else:
            messagebox.showerror("Error", "Completar ambos campos")

    crear_boton_moderno(ventana, "Registrar", guardar)

# Ver Dueños
def ver_duenios_gui():
    datos = [(d.nombre, d.telefono) for d in vet.clientes]
    mostrar_tabla_moderna("Dueños Registrados", ["Nombre", "Teléfono"], datos)

# Registrar Mascota
def registrar_mascota_gui():
    ventana = Toplevel(root)
    ventana.title("Registrar Mascota")
    ventana.geometry("400x480") 
    ventana.grab_set()
    ventana.focus_set()
    ventana.configure(bg=COLOR_DARK) # Fondo oscuro

    # Labels y Entries con estilo Cyberpunk
    tk.Label(ventana, text="Nombre del dueño:", bg=COLOR_DARK, fg=COLOR_TEXT_LIGHT, font=FONT_PRIMARY).pack(anchor="nw", padx=20, pady=(20,5))
    duenio_var = tk.StringVar()
    tk.Entry(ventana, textvariable=duenio_var, font=FONT_PRIMARY, bg=COLOR_CANVAS, fg=COLOR_PRIMARY, insertbackground=COLOR_ACCENT).pack(anchor="nw", padx=20, fill="x")

    tk.Label(ventana, text="Nombre mascota:", bg=COLOR_DARK, fg=COLOR_TEXT_LIGHT, font=FONT_PRIMARY).pack(anchor="nw", padx=20, pady=(5,5))
    nombre_var = tk.StringVar()
    tk.Entry(ventana, textvariable=nombre_var, font=FONT_PRIMARY, bg=COLOR_CANVAS, fg=COLOR_PRIMARY, insertbackground=COLOR_ACCENT).pack(anchor="nw", padx=20, fill="x")

    tk.Label(ventana, text="Edad (años):", bg=COLOR_DARK, fg=COLOR_TEXT_LIGHT, font=FONT_PRIMARY).pack(anchor="nw", padx=20, pady=(5,5))
    edad_var = tk.StringVar()
    tk.Entry(ventana, textvariable=edad_var, font=FONT_PRIMARY, bg=COLOR_CANVAS, fg=COLOR_PRIMARY, insertbackground=COLOR_ACCENT).pack(anchor="nw", padx=20, fill="x")

    tk.Label(ventana, text="Especie:", bg=COLOR_DARK, fg=COLOR_TEXT_LIGHT, font=FONT_PRIMARY).pack(anchor="nw", padx=20, pady=(5,5))
    especie_var = tk.StringVar()
    tk.Entry(ventana, textvariable=especie_var, font=FONT_PRIMARY, bg=COLOR_CANVAS, fg=COLOR_PRIMARY, insertbackground=COLOR_ACCENT).pack(anchor="nw", padx=20, fill="x")

    tk.Label(ventana, text="Peso (kg):", bg=COLOR_DARK, fg=COLOR_TEXT_LIGHT, font=FONT_PRIMARY).pack(anchor="nw", padx=20, pady=(5,5))
    peso_var = tk.StringVar()
    tk.Entry(ventana, textvariable=peso_var, font=FONT_PRIMARY, bg=COLOR_CANVAS, fg=COLOR_PRIMARY, insertbackground=COLOR_ACCENT).pack(anchor="nw", padx=20, fill="x")

    def guardar():
        # ... (Lógica de guardado)
        nombre_duenio = duenio_var.get().strip()
        nombre = nombre_var.get().strip()
        edad = edad_var.get().strip()
        especie = especie_var.get().strip()
        peso = peso_var.get().strip()

        duenio = vet.buscar_duenio(nombre_duenio)
        if not duenio:
            messagebox.showerror("Error", f"Dueño '{nombre_duenio}' no encontrado. Regístrelo primero.")
            return

        if nombre and edad and especie and peso:
            try:
                mascota = Mascota(nombre, edad, especie, peso) 
                
                if mascota.edad == 0 or mascota.peso == 0.0:
                    raise ValueError("Edad o peso deben ser números válidos.")
                
                if duenio.registrar_mascota(mascota):
                    messagebox.showinfo("Éxito", f"{nombre} registrada a nombre de {duenio.nombre}. Edad: {mascota.edad}, Peso: {mascota.peso}kg")
                    ventana.destroy()
                else:
                    messagebox.showerror("Error", "No se pudo registrar la mascota")
            except ValueError as e:
                messagebox.showerror("Error", str(e))
            except Exception as e:
                messagebox.showerror("Error", f"Error inesperado: {e}")
        else:
            messagebox.showerror("Error", "Completar todos los campos")

    crear_boton_moderno(ventana, "Registrar Mascota", guardar)

# Ver Servicios
def ver_servicios_gui():
    datos = [(s, f"${p:.2f}") for s, p in vet.servicios.items()]
    mostrar_tabla_moderna("Servicios Registrados", ["Servicio", "Precio"], datos)

# Agregar Servicio
def agregar_servicio_gui():
    ventana = Toplevel(root)
    ventana.title("Agregar Servicio")
    ventana.geometry("400x250")
    ventana.grab_set()
    ventana.focus_set()
    ventana.configure(bg=COLOR_DARK) # Fondo oscuro

    # Labels y Entries con estilo Cyberpunk
    tk.Label(ventana, text="Nombre del servicio:", bg=COLOR_DARK, fg=COLOR_TEXT_LIGHT, font=FONT_PRIMARY).pack(anchor="nw", padx=20, pady=(20,5))
    servicio_var = tk.StringVar()
    tk.Entry(ventana, textvariable=servicio_var, font=FONT_PRIMARY, bg=COLOR_CANVAS, fg=COLOR_PRIMARY, insertbackground=COLOR_ACCENT).pack(anchor="nw", padx=20, fill="x")

    tk.Label(ventana, text="Precio:", bg=COLOR_DARK, fg=COLOR_TEXT_LIGHT, font=FONT_PRIMARY).pack(anchor="nw", padx=20, pady=(15,5))
    precio_var = tk.StringVar()
    tk.Entry(ventana, textvariable=precio_var, font=FONT_PRIMARY, bg=COLOR_CANVAS, fg=COLOR_PRIMARY, insertbackground=COLOR_ACCENT).pack(anchor="nw", padx=20, fill="x")

    def guardar():
        # ... (Lógica de guardado)
        nombre_servicio = servicio_var.get().strip()
        precio_str = precio_var.get().strip().replace(",", ".") 
        
        if nombre_servicio and precio_str:
            exito = vet.agregar_servicio(nombre_servicio, precio_str)
            
            if exito:
                messagebox.showinfo("Éxito", f"Servicio {nombre_servicio} agregado.")
                ventana.destroy()
            else:
                messagebox.showerror("Error", "Precio inválido. Debe ser un número.")
        else:
            messagebox.showerror("Error", "Completar todos los campos")

    crear_boton_moderno(ventana, "Agregar Servicio", guardar)

# Registrar Consulta
def registrar_consulta_gui():
    ventana = Toplevel(root)
    ventana.title("Registrar Consulta")
    ventana.geometry("400x300")
    ventana.grab_set()
    ventana.focus_set()
    ventana.configure(bg=COLOR_DARK) # Fondo oscuro

    # Labels y Entries con estilo Cyberpunk
    tk.Label(ventana, text="Nombre del dueño:", bg=COLOR_DARK, fg=COLOR_TEXT_LIGHT, font=FONT_PRIMARY).pack(anchor="nw", padx=20, pady=(20,5))
    duenio_var = tk.StringVar()
    tk.Entry(ventana, textvariable=duenio_var, font=FONT_PRIMARY, bg=COLOR_CANVAS, fg=COLOR_PRIMARY, insertbackground=COLOR_ACCENT).pack(anchor="nw", padx=20, fill="x")

    tk.Label(ventana, text="Nombre mascota:", bg=COLOR_DARK, fg=COLOR_TEXT_LIGHT, font=FONT_PRIMARY).pack(anchor="nw", padx=20, pady=(15,5))
    mascota_var = tk.StringVar()
    tk.Entry(ventana, textvariable=mascota_var, font=FONT_PRIMARY, bg=COLOR_CANVAS, fg=COLOR_PRIMARY, insertbackground=COLOR_ACCENT).pack(anchor="nw", padx=20, fill="x")

    tk.Label(ventana, text="Servicio:", bg=COLOR_DARK, fg=COLOR_TEXT_LIGHT, font=FONT_PRIMARY).pack(anchor="nw", padx=20, pady=(15,5))
    servicio_var = tk.StringVar()
    tk.Entry(ventana, textvariable=servicio_var, font=FONT_PRIMARY, bg=COLOR_CANVAS, fg=COLOR_PRIMARY, insertbackground=COLOR_ACCENT).pack(anchor="nw", padx=20, fill="x")

    def guardar():
        # ... (Lógica de guardado)
        nombre_duenio = duenio_var.get().strip()
        nombre_mascota = mascota_var.get().strip()
        servicio = servicio_var.get().strip()

        if not (nombre_duenio and nombre_mascota and servicio):
            messagebox.showerror("Error", "Completar todos los campos")
            return

        exito = vet.registrar_consulta(nombre_duenio, nombre_mascota, servicio)
        
        if exito:
            messagebox.showinfo("Éxito", f"Consulta '{servicio}' registrada para {nombre_mascota}.")
            ventana.destroy()
        else:
            error_msg = "Error al registrar: Verifique que el Dueño, Mascota y Servicio existan."
            messagebox.showerror("Error", error_msg)

    crear_boton_moderno(ventana, "Registrar Consulta", guardar)

# Historial de Mascota
def ver_historial_gui():
    ventana = Toplevel(root)
    ventana.title("Búsqueda de Historial")
    ventana.geometry("400x250")
    ventana.grab_set()
    ventana.focus_set()
    ventana.configure(bg=COLOR_DARK) # Fondo oscuro

    # Labels y Entries con estilo Cyberpunk
    tk.Label(ventana, text="Nombre del dueño:", bg=COLOR_DARK, fg=COLOR_TEXT_LIGHT, font=FONT_PRIMARY).pack(anchor="nw", padx=20, pady=(20,5))
    duenio_var = tk.StringVar()
    tk.Entry(ventana, textvariable=duenio_var, font=FONT_PRIMARY, bg=COLOR_CANVAS, fg=COLOR_PRIMARY, insertbackground=COLOR_ACCENT).pack(anchor="nw", padx=20, fill="x")

    tk.Label(ventana, text="Nombre mascota:", bg=COLOR_DARK, fg=COLOR_TEXT_LIGHT, font=FONT_PRIMARY).pack(anchor="nw", padx=20, pady=(15,5))
    mascota_var = tk.StringVar()
    tk.Entry(ventana, textvariable=mascota_var, font=FONT_PRIMARY, bg=COLOR_CANVAS, fg=COLOR_PRIMARY, insertbackground=COLOR_ACCENT).pack(anchor="nw", padx=20, fill="x")

    def mostrar():
        # ... (Lógica de búsqueda)
        nombre_duenio = duenio_var.get().strip()
        nombre_mascota = mascota_var.get().strip()
        
        duenio = vet.buscar_duenio(nombre_duenio)
        if not duenio:
            messagebox.showerror("Error", "Dueño no encontrado")
            return
        
        mascota = duenio.buscar_mascota(nombre_mascota)
        if not mascota:
            messagebox.showerror("Error", "Mascota no encontrada")
            return
        
        # Prepara los datos para la tabla
        datos = [(f"Especie: {mascota.especie}", "---")]
        datos.append((f"Edad Actual: {mascota.edad} años", f"Peso Actual: {mascota.peso} kg"))
        
        if mascota.historial_medico:
            datos.extend([(c, "---") for c in mascota.historial_medico])
        else:
            datos.append(("Sin registros de consultas.", "---"))
            
        mostrar_tabla_moderna(f"Historial de {mascota.nombre}", ["Detalle / Evento", "Valor"], datos)
        ventana.destroy()

    crear_boton_moderno(ventana, "Ver Historial", mostrar)

# Renovar vacuna
def renovar_vacuna_gui():
    ventana = Toplevel(root)
    ventana.title("Renovación de Vacunas/Tratamiento")
    ventana.geometry("400x300") # Un poco más grande para el nuevo campo
    ventana.grab_set()
    ventana.focus_set()
    ventana.configure(bg=COLOR_DARK)

    # Labels y Entries con estilo Cyberpunk
    tk.Label(ventana, text="Nombre del dueño:", bg=COLOR_DARK, fg=COLOR_TEXT_LIGHT, font=FONT_PRIMARY).pack(anchor="nw", padx=20, pady=(20,5))
    duenio_var = tk.StringVar()
    tk.Entry(ventana, textvariable=duenio_var, font=FONT_PRIMARY, bg=COLOR_CANVAS, fg=COLOR_PRIMARY, insertbackground=COLOR_ACCENT).pack(anchor="nw", padx=20, fill="x")

    tk.Label(ventana, text="Nombre mascota:", bg=COLOR_DARK, fg=COLOR_TEXT_LIGHT, font=FONT_PRIMARY).pack(anchor="nw", padx=20, pady=(15,5))
    mascota_var = tk.StringVar()
    tk.Entry(ventana, textvariable=mascota_var, font=FONT_PRIMARY, bg=COLOR_CANVAS, fg=COLOR_PRIMARY, insertbackground=COLOR_ACCENT).pack(anchor="nw", padx=20, fill="x")
    # Campo para Tipo de Renovación (Vacuna)
    tk.Label(ventana, text="Tipo de Renovación:", bg=COLOR_DARK, fg=COLOR_TEXT_LIGHT, font=FONT_PRIMARY).pack(anchor="nw", padx=20, pady=(15,5))
    vacuna_var = tk.StringVar()
    tk.Entry(ventana, textvariable=vacuna_var, font=FONT_PRIMARY, bg=COLOR_CANVAS, fg=COLOR_PRIMARY, insertbackground=COLOR_ACCENT).pack(anchor="nw", padx=20, fill="x")

    def aplicar():
        # ... (Lógica de aplicación)
        nombre_duenio = duenio_var.get().strip()
        nombre_mascota = mascota_var.get().strip()
        
        duenio = vet.buscar_duenio(nombre_duenio)
        if not duenio:
            messagebox.showerror("Error", "Dueño no encontrado")
            return
        
        mascota = duenio.buscar_mascota(nombre_mascota)
        if not mascota:
            messagebox.showerror("Error", "Mascota no encontrada")
            return
            
      # NUEVA LÍNEA: Obtener el tipo de renovación
        tipo_renovacion = vacuna_var.get().strip() 
        
        if not tipo_renovacion:
            messagebox.showerror("Error", "Debe especificar el tipo de renovación o vacuna.")
            return
        # ------------------ Lógica de Registro ------------------
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")
        
        # Formatear el mensaje del historial
        registro_evento = f"[RENOVACIÓN {fecha_actual}] {tipo_renovacion} aplicada."
        
        # AÑADIR EL EVENTO AL HISTORIAL DE LA MASCOTA
        mascota.registrar_evento(registro_evento)        
        # Mensaje de éxito y cierre de ventana
        messagebox.showinfo("Éxito", f"Renovación '{tipo_renovacion}' registrada para {mascota.nombre}.")
        ventana.destroy()
        # --------------------------------------------------------
    crear_boton_moderno(ventana, "Registrar Renovación", aplicar)


# Generar Factura
def generar_factura_gui():
    ventana = Toplevel(root)
    ventana.title("Generar Factura")
    ventana.geometry("400x300")
    ventana.grab_set()
    ventana.focus_set()
    ventana.configure(bg=COLOR_DARK) # Fondo oscuro

    # Labels y Entries con estilo Cyberpunk
    tk.Label(ventana, text="Nombre del dueño:", bg=COLOR_DARK, fg=COLOR_TEXT_LIGHT, font=FONT_PRIMARY).pack(anchor="nw", padx=20, pady=(20,5))
    duenio_var = tk.StringVar()
    tk.Entry(ventana, textvariable=duenio_var, font=FONT_PRIMARY, bg=COLOR_CANVAS, fg=COLOR_PRIMARY, insertbackground=COLOR_ACCENT).pack(anchor="nw", padx=20, fill="x")

    tk.Label(ventana, text="Nombre mascota:", bg=COLOR_DARK, fg=COLOR_TEXT_LIGHT, font=FONT_PRIMARY).pack(anchor="nw", padx=20, pady=(15,5))
    mascota_var = tk.StringVar()
    tk.Entry(ventana, textvariable=mascota_var, font=FONT_PRIMARY, bg=COLOR_CANVAS, fg=COLOR_PRIMARY, insertbackground=COLOR_ACCENT).pack(anchor="nw", padx=20, fill="x")

    tk.Label(ventana, text="Servicio:", bg=COLOR_DARK, fg=COLOR_TEXT_LIGHT, font=FONT_PRIMARY).pack(anchor="nw", padx=20, pady=(15,5))
    servicio_var = tk.StringVar()
    tk.Entry(ventana, textvariable=servicio_var, font=FONT_PRIMARY, bg=COLOR_CANVAS, fg=COLOR_PRIMARY, insertbackground=COLOR_ACCENT).pack(anchor="nw", padx=20, fill="x")

    def generar():
        # ... (Lógica de generación)
        nombre_duenio = duenio_var.get().strip()
        nombre_mascota = mascota_var.get().strip()
        servicio = servicio_var.get().strip()

        factura_data = vet.generar_factura(nombre_duenio, nombre_mascota, servicio)
        
        if factura_data:
            columnas = ["Veterinaria", "Dueño", "Mascota", "Servicio", "Precio"]
            precio_float_val = factura_data[4] 
            datos = [factura_data[:4] + [f"${precio_float_val:.2f}"]]
            
            mostrar_tabla_moderna("Factura Generada", columnas, datos)
            ventana.destroy()
        else:
            messagebox.showerror("Error", "Error generando factura. Verifique Dueño, Mascota y Servicio.")

    crear_boton_moderno(ventana, "Generar Factura", generar)


# ==============================================================================
# # Ventana Principal (Responsive Refactoring)
# ==============================================================================
root = tk.Tk()
root.title("Clínica Huellita Cyberpunk 🐾")
# Eliminamos root.geometry()
root.resizable(True, True) # Permitimos redimensionamiento
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Marco contenedor para centrar el contenido horizontalmente
container_frame = tk.Frame(root, bg=COLOR_DARK)
# Usar grid para llenar el root
container_frame.grid(row=0, column=0, sticky="nsew")
# 2. Definimos los pesos para la adaptabilidad
# La columna 0 (Imagen) y la columna 1 (Botones) se expandirán 50/50 (weight=1)
container_frame.grid_columnconfigure(0, weight=1) 
container_frame.grid_columnconfigure(1, weight=1) 
container_frame.grid_rowconfigure(0, weight=1)    # La fila única también se expande

# 1. Marco Izquierdo: Imagen y Título

frame_image_side = tk.Frame(container_frame, bg=COLOR_DARK, padx=20, pady=20, bd=3, relief="flat", highlightbackground=COLOR_PRIMARY, highlightthickness=2)
# Marco Izquierdo (Columna 0)
frame_image_side.grid(row=0, column=0, sticky="nsew", padx=10, pady=10) # sticky="nsew" reemplaza a fill=BOTH

# Títulos de la izquierda (fg corregido)
tk.Label(frame_image_side, text=f"{vet.nombre} 🐾", font=FONT_TITLE,
         fg=COLOR_PRIMARY, bg=COLOR_DARK).pack(pady=(10, 5))
tk.Label(frame_image_side, text="Bienvenido al Sistema de Gestión", font=FONT_SUBTITLE,
         fg=COLOR_TEXT_LIGHT, bg=COLOR_DARK).pack(pady=(0, 20))

# Área de la Imagen
canvas_width = 360
canvas_height = 400
canvas_img = tk.Canvas(frame_image_side, width=canvas_width, height=canvas_height,
                        bg=COLOR_CANVAS, highlightthickness=0)
canvas_img.pack(pady=20)
# ... (Lógica de carga de imagen - sin cambios)
image_path = "Fondo.png" 

# [ ... Lógica Try/Except de la imagen (mantener sin cambios) ... ]

# Carga de imagen (Lógica Try/Except completa)
try:
    original_image = Image.open(image_path)
    width_ratio = canvas_width / original_image.width
    height_ratio = canvas_height / original_image.height
    resize_ratio = min(width_ratio, height_ratio)
    new_width = int(original_image.width * resize_ratio)
    new_height = int(original_image.height * resize_ratio)
    resized_image = original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    photo_image = ImageTk.PhotoImage(resized_image)
    canvas_img.image = photo_image 
    x_center = (canvas_width - new_width) / 2
    y_center = (canvas_height - new_height) / 2
    canvas_img.create_image(x_center, y_center, anchor=tk.NW, image=photo_image)
except FileNotFoundError:
    canvas_img.create_text(canvas_width/2, canvas_height/2, text="Imagen no encontrada", font=("Segoe UI", 16, "bold"), fill=COLOR_TEXT_LIGHT)
except Exception as e:
    canvas_img.create_text(canvas_width/2, canvas_height/2, text="Error al cargar imagen", font=("Segoe UI", 16, "bold"), fill=COLOR_TEXT_LIGHT)
    
tk.Label(frame_image_side, text="¡El mejor cuidado para tus mascotas!", font=FONT_PRIMARY,
      fg=COLOR_TEXT_LIGHT, bg=COLOR_DARK).pack(pady=(10, 0)) # <-- Texto claro

# 2. Marco Derecho: Botones de Funcionalidad

frame_button_side = tk.Frame(container_frame, bg=COLOR_DARK, padx=20, pady=20, bd=3, relief="flat", highlightbackground=COLOR_PRIMARY, highlightthickness=2)
# Marco Derecho (Columna 1)
frame_button_side.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
# Título del menú (bg corregido)
tk.Label(frame_button_side, text="Menú Principal de Gestión", font=FONT_TITLE,
          fg=COLOR_ACCENT, bg=COLOR_DARK).pack(pady=(10, 15))


# Bloque de Clientes y Mascotas (fg corregido)
tk.Label(frame_button_side, text="— Clientes y Pacientes —", font=FONT_SUBTITLE,
          fg=COLOR_TEXT_LIGHT, bg=COLOR_DARK).pack(pady=(5, 5))

crear_boton_moderno(frame_button_side, "Registrar Dueño 👤", registrar_duenio_gui)
crear_boton_moderno(frame_button_side, "Ver Dueños 👨‍👩‍👧‍👦", ver_duenios_gui)
crear_boton_moderno(frame_button_side, "Registrar Mascota 🐾", registrar_mascota_gui)
crear_boton_moderno(frame_button_side, "Ver Historial 📜", ver_historial_gui)
crear_boton_moderno(frame_button_side, "Registrar Renovación de Vacuna 💉", renovar_vacuna_gui)

# Bloque de Servicios y Consultas (fg corregido)
tk.Label(frame_button_side, text="— Servicios y Consultas —", font=FONT_SUBTITLE,
          fg=COLOR_TEXT_LIGHT, bg=COLOR_DARK).pack(pady=(15, 5)) # <-- PADY aumentado para separación

crear_boton_moderno(frame_button_side, "Ver Servicios y Precios 💊", ver_servicios_gui)
crear_boton_moderno(frame_button_side, "Agregar Nuevo Servicio ➕", agregar_servicio_gui)
crear_boton_moderno(frame_button_side, "Registrar Consulta 📝", registrar_consulta_gui)
crear_boton_moderno(frame_button_side, "Generar Factura 💰", generar_factura_gui)

# Agrega un espacio extra debajo del último botón
tk.Frame(frame_button_side, height=20, bg=COLOR_DARK).pack(fill="x", pady=(0,5)) 


root.mainloop()