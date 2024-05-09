import tkinter as tk
from tkinter import filedialog, simpledialog


class VentanaPilaCola:
    def __init__(self, ventana, tipo):
        self.ventana = ventana
        self.tipo = tipo

        self.info_frame = tk.Frame(ventana)
        self.info_frame.pack(side=tk.RIGHT)

        self.frame_dibujo = tk.Frame(ventana)
        self.frame_dibujo.pack()

        self.frame = tk.Frame(ventana)
        self.frame.pack()

        self.search_frame = tk.Frame(ventana)
        self.search_frame.pack()

        self.canvas_width = 400
        self.canvas_height = 300
        self.rect_width = 100
        self.rect_height = 30
        self.rect_spacing = 1
        self.canvas = tk.Canvas(self.frame_dibujo, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        if self.tipo == 'pila':
            self.top = self.canvas_height - 30
        else:
            self.top = 20
        self.elementos = []

        self.dato = tk.Entry(self.frame)
        self.dato.pack(side=tk.LEFT)

        self.boton_ingresar = tk.Button(self.frame, text='Ingresar', command=self.ingresar_pila)
        self.boton_ingresar.pack(side=tk.LEFT)

        self.boton_borrar = tk.Button(self.frame, text='Borrar', command=self.borrar_pila)
        self.boton_borrar.pack(side=tk.LEFT)

        self.label_cantidad = tk.Label(self.info_frame, text='Lista Vacia')
        self.label_cantidad.pack()

        self.label_primero = tk.Label(self.info_frame, text='Primer Elemento: -')
        self.label_primero.pack()

        self.label_ultimo = tk.Label(self.info_frame, text='Ultimo Elemento: -')
        self.label_ultimo.pack()

        self.dato_buscado = tk.Entry(self.search_frame)
        self.dato_buscado.pack(side=tk.LEFT)

        self.boton_buscar = tk.Button(self.search_frame, text='Buscar', command=self.buscar_pila)
        self.boton_buscar.pack(side=tk.LEFT)

        self.dato_encontrado = tk.Label(self.info_frame, text='')
        self.dato_encontrado.pack()

        self.boton_guardar = tk.Button(self.info_frame, text='Guardar', command=self.guardar)
        self.boton_guardar.pack(side=tk.LEFT)

        self.boton_abrir = tk.Button(self.info_frame, text='Abrir', command=self.abrir)
        self.boton_abrir.pack(side=tk.LEFT)

    def ingresar_pila(self):
        elemento = self.dato.get()
        if elemento:
            self.elementos.append(elemento)
            self.dibujar_pila()
            self.info_pila()
            self.dato.delete(0, tk.END)

    def borrar_pila(self):
        if self.elementos:
            self.elementos.pop()
            self.dibujar_pila()
            self.info_pila()

    def buscar_pila(self):
        buscado = self.dato_buscado.get()
        if buscado:
            if buscado in self.elementos:
                self.dato_encontrado.config(text=f'Valor encontrado: {buscado}')
            else:
                self.dato_encontrado.config(text=f'Valor no encontrado')

    def info_pila(self):
        cantidad = len(self.elementos)
        self.label_cantidad.config(text=f'Cantidad de elementos: {cantidad}')
        if cantidad > 0:
            self.label_primero.config(text=f'Primero elemento: {self.elementos[cantidad-1]}')
            self.label_ultimo.config(text=f'Ultimo elemento: {self.elementos[0]}')
        self.dato_encontrado.config(text='')

    def dibujar_pila(self):
        self.canvas.delete("all")
        y = self.top
        for elemento in self.elementos:
            x = (self.canvas_width - self.rect_width) / 2
            self.canvas.create_rectangle(x, y, x + self.rect_width, y + self.rect_height, outline="black", fill="lightblue")
            self.canvas.create_text(x + self.rect_width / 2, y + self.rect_height / 2, text=elemento, fill="black")
            if self.tipo == 'pila':
                y -= self.rect_height + self.rect_spacing
            elif self.tipo == 'cola':
                y += self.rect_height + self.rect_spacing

    def guardar(self):
        file_name = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')])
        if file_name:
            with open(file_name, 'w') as f:
                for elemento in self.elementos:
                    f.write(elemento + '\n')

    def abrir(self):
        file_name = filedialog.askopenfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')])
        if file_name:
            with open(file_name, 'r') as f:
                self.elementos = [line.strip() for line in f.readlines()]
                self.dibujar_pila()
                self.info_pila()


class NodoListaSimpleAndCircular:
    def __init__(self, data):
        self.data = data
        self.siguiente = None


class VentanaListaSimple:
    def __init__(self, ventana):
        self.ventana = ventana

        self.info_frame = tk.Frame(ventana)
        self.info_frame.pack(side=tk.RIGHT)

        self.frame_dibujo = tk.Frame(ventana)
        self.frame_dibujo.pack()

        self.frame = tk.Frame(ventana)
        self.frame.pack()

        self.search_frame = tk.Frame(ventana)
        self.search_frame.pack()

        self.canvas_width = 800
        self.canvas_height = 300
        self.rect_width = 100
        self.rect_height = 30
        self.rect_spacing = 2
        self.canvas = tk.Canvas(self.frame_dibujo, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        self.top = self.canvas_height // 2
        self.primer_nodo = None

        self.dato = tk.Entry(self.frame)
        self.dato.pack(side=tk.LEFT)

        self.boton_insertari = tk.Button(self.frame, text='Insertar al inicio', command=self.insertar_inicio)
        self.boton_insertari.pack(side=tk.LEFT)

        self.boton_ingresarf = tk.Button(self.frame, text='Insertar al final', command=self.insertar_final)
        self.boton_ingresarf.pack(side=tk.LEFT)

        self.boton_borrari = tk.Button(self.frame, text='Borrar al inicio', command=self.borrar_inicio)
        self.boton_borrari.pack(side=tk.LEFT)

        self.boton_borrarf = tk.Button(self.frame, text='Borrar al final', command=self.borrar_final)
        self.boton_borrarf.pack(side=tk.LEFT)

        self.label_cantidad = tk.Label(self.info_frame, text='Lista Vacia')
        self.label_cantidad.pack()

        self.label_primero = tk.Label(self.info_frame, text='Primer Elemento: -')
        self.label_primero.pack()

        self.label_ultimo = tk.Label(self.info_frame, text='Ultimo Elemento: -')
        self.label_ultimo.pack()

        self.dato_buscado = tk.Entry(self.search_frame)
        self.dato_buscado.pack(side=tk.LEFT)

        self.boton_buscar = tk.Button(self.search_frame, text='Buscar', command=self.buscar_lista)
        self.boton_buscar.pack(side=tk.LEFT)

        self.dato_encontrado = tk.Label(self.info_frame, text='')
        self.dato_encontrado.pack()

        self.boton_guardar = tk.Button(self.info_frame, text='Guardar', command=self.guardar)
        self.boton_guardar.pack(side=tk.LEFT)

        self.boton_abrir = tk.Button(self.info_frame, text='Abrir', command=self.abrir)
        self.boton_abrir.pack(side=tk.LEFT)

    def insertar_inicio(self):
        elemento = self.dato.get()
        if elemento:
            nuevo_nodo = NodoListaSimpleAndCircular(elemento)
            nuevo_nodo.siguiente = self.primer_nodo
            self.primer_nodo = nuevo_nodo
            self.dibujar_lista()
            self.info()
            self.dato.delete(0, tk.END)

    def insertar_final(self):
        elemento = self.dato.get()
        if elemento:
            nuevo_nodo = NodoListaSimpleAndCircular(elemento)
            if not self.primer_nodo:
                self.primer_nodo = nuevo_nodo
            else:
                nodo_actual = self.primer_nodo
                while nodo_actual.siguiente:
                    nodo_actual = nodo_actual.siguiente
                nodo_actual.siguiente = nuevo_nodo
            self.dibujar_lista()
            self.info()
            self.dato.delete(0, tk.END)

    def borrar_inicio(self):
        if self.primer_nodo:
            self.primer_nodo = self.primer_nodo.siguiente
            self.dibujar_lista()
            self.info()

    def borrar_final(self):
        if self.primer_nodo:
            if not self.primer_nodo.siguiente:
                self.primer_nodo = None
            else:
                nodo_anterior = None
                nodo_actual = self.primer_nodo
                while nodo_actual.siguiente:
                    nodo_anterior = nodo_actual
                    nodo_actual = nodo_actual.siguiente
                nodo_anterior.siguiente = None

            self.dibujar_lista()
            self.info()

    def buscar_lista(self):
        buscado = self.dato_buscado.get()
        if buscado:
            nodo_actual = self.primer_nodo
            encontrado = False
            while nodo_actual:
                if nodo_actual.data == buscado:
                    self.dato_encontrado.config(text=f'Valor encontrado {nodo_actual.data}')
                    encontrado = True
                    break
                nodo_actual = nodo_actual.siguiente
            if not encontrado:
                self.dato_encontrado.config(text=f'Valor {buscado} no encontrado')

    def dibujar_lista(self):
        self.canvas.delete("all")
        x = self.rect_spacing
        nodo_actual = self.primer_nodo
        while nodo_actual:
            self.canvas.create_rectangle(x, self.top - self.rect_height // 2, x + self.rect_width, self.top + self.rect_height // 2, outline='black', fill='lightblue')
            self.canvas.create_text(x + self.rect_width // 2, self.top, text=nodo_actual.data, fill='black')
            x += self.rect_width + self.rect_spacing
            self.flecha(x, self.top)
            x += self.rect_spacing
            nodo_actual = nodo_actual.siguiente

    def flecha(self, x, y):
        self.canvas.create_line(x, y, x + 10, y, fill='black', arrow=tk.LAST)

    def size(self):
        cont = 0
        nodo_actual = self.primer_nodo
        while nodo_actual:
            cont += 1
            nodo_actual = nodo_actual.siguiente
        return cont

    def ultimo(self):
        nodo_actual = self.primer_nodo
        while nodo_actual.siguiente:
            nodo_actual = nodo_actual.siguiente
        return nodo_actual

    def info(self):
        cantidad = self.size()
        self.label_cantidad.config(text=f'Cantidad de elementos: {cantidad}')
        if cantidad > 0:
            self.label_primero.config(text=f'Primero elemento: {self.primer_nodo.data}')
            self.label_ultimo.config(text=f'Ultimo elemento: {self.ultimo().data}')
        self.dato_encontrado.config(text='')

    def guardar(self):
        file_name = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')])
        if file_name:
            with open(file_name, 'w') as f:
                nodo_actual = self.primer_nodo
                while nodo_actual:
                    f.write(nodo_actual.data + '\n')
                    nodo_actual = nodo_actual.siguiente

    def abrir(self):
        file_name = filedialog.askopenfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')])
        if file_name:
            with open(file_name, 'r') as f:
                self.primer_nodo = None
                for line in f:
                    self.insertar_final_valor(line.strip())
            self.dibujar_lista()
            self.info()

    def insertar_final_valor(self, valor):
        nuevo_nodo = NodoListaSimpleAndCircular(valor)
        if not self.primer_nodo:
            self.primer_nodo = nuevo_nodo
        else:
            nodo_actual = self.primer_nodo
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo


class VentanaListaCircular:
    def __init__(self, ventana):
        self.ventana = ventana

        self.info_frame = tk.Frame(ventana)
        self.info_frame.pack(side=tk.RIGHT)

        self.frame_dibujo = tk.Frame(ventana)
        self.frame_dibujo.pack()

        self.frame = tk.Frame(ventana)
        self.frame.pack()

        self.search_frame = tk.Frame(ventana)
        self.search_frame.pack()

        self.canvas_width = 800
        self.canvas_height = 300
        self.rect_width = 100
        self.rect_height = 30
        self.rect_spacing = 2
        self.canvas = tk.Canvas(self.frame_dibujo, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        self.top = self.canvas_height // 2
        self.primer_nodo = None

        self.dato = tk.Entry(self.frame)
        self.dato.pack(side=tk.LEFT)

        self.boton_insertari = tk.Button(self.frame, text='Insertar al inicio', command=self.insertar_inicio)
        self.boton_insertari.pack(side=tk.LEFT)

        self.boton_ingresarf = tk.Button(self.frame, text='Insertar al final', command=self.insertar_final)
        self.boton_ingresarf.pack(side=tk.LEFT)

        self.boton_borrari = tk.Button(self.frame, text='Borrar al inicio', command=self.borrar_inicio)
        self.boton_borrari.pack(side=tk.LEFT)

        self.boton_borrarf = tk.Button(self.frame, text='Borrar al final', command=self.borrar_final)
        self.boton_borrarf.pack(side=tk.LEFT)

        self.boton_rotard = tk.Button(self.frame, text='Rotar Derecha', command=self.rotar_derecha)
        self.boton_rotard.pack(side=tk.LEFT)

        self.boton_rotari = tk.Button(self.frame, text='Rotar Izquierda', command=self.rotar_izquierda)
        self.boton_rotari.pack(side=tk.LEFT)

        self.label_cantidad = tk.Label(self.info_frame, text='Lista Vacia')
        self.label_cantidad.pack()

        self.label_primero = tk.Label(self.info_frame, text='Primer Elemento: -')
        self.label_primero.pack()

        self.label_ultimo = tk.Label(self.info_frame, text='Ultimo Elemento: -')
        self.label_ultimo.pack()

        self.dato_buscado = tk.Entry(self.search_frame)
        self.dato_buscado.pack(side=tk.LEFT)

        self.boton_buscar = tk.Button(self.search_frame, text='Buscar', command=self.buscar_lista)
        self.boton_buscar.pack(side=tk.LEFT)

        self.dato_encontrado = tk.Label(self.info_frame, text='')
        self.dato_encontrado.pack()

        self.boton_guardar = tk.Button(self.info_frame, text='Guardar', command=self.guardar)
        self.boton_guardar.pack(side=tk.LEFT)

        self.boton_abrir = tk.Button(self.info_frame, text='Abrir', command=self.abrir)
        self.boton_abrir.pack(side=tk.LEFT)

    def insertar_inicio(self):
        elemento = self.dato.get()
        if elemento:
            nuevo_nodo = NodoListaSimpleAndCircular(elemento)
            if not self.primer_nodo:
                self.primer_nodo = nuevo_nodo
                nuevo_nodo.siguiente = self.primer_nodo
            else:
                ultimo_nodo = self.ultimo()
                nuevo_nodo.siguiente = self.primer_nodo
                self.primer_nodo = nuevo_nodo
                ultimo_nodo.siguiente = self.primer_nodo
            self.dibujar_lista()
            self.info()
            self.dato.delete(0, tk.END)

    def insertar_final(self):
        elemento = self.dato.get()
        if elemento:
            nuevo_nodo = NodoListaSimpleAndCircular(elemento)
            if not self.primer_nodo:
                self.primer_nodo = nuevo_nodo
                nuevo_nodo.siguiente = self.primer_nodo
            else:
                ultimo_nodo = self.ultimo()
                nuevo_nodo.siguiente = self.primer_nodo
                ultimo_nodo.siguiente = nuevo_nodo
            self.dibujar_lista()
            self.info()
            self.dato.delete(0, tk.END)

    def borrar_inicio(self):
        if self.primer_nodo:
            ultimo_nodo = self.ultimo()
            if self.primer_nodo == ultimo_nodo:
                self.primer_nodo = None
            else:
                self.primer_nodo = self.primer_nodo.siguiente
                ultimo_nodo.siguiente = self.primer_nodo
            self.dibujar_lista()
            self.info()

    def borrar_final(self):
        if self.primer_nodo:
            ultimo_nodo = self.ultimo()
            if self.primer_nodo == ultimo_nodo:
                self.primer_nodo = None
            else:
                nodo_anterior = None
                nodo_actual = self.primer_nodo
                while nodo_actual.siguiente != self.primer_nodo:
                    nodo_anterior = nodo_actual
                    nodo_actual = nodo_actual.siguiente
                nodo_anterior.siguiente = self.primer_nodo

            self.dibujar_lista()
            self.info()

    def rotar_derecha(self):
        if self.primer_nodo:
            ultimo_nodo = self.ultimo()
            self.primer_nodo = ultimo_nodo
            self.dibujar_lista()
            self.info()

    def rotar_izquierda(self):
        if self.primer_nodo:
            self.primer_nodo = self.primer_nodo.siguiente
            self.dibujar_lista()
            self.info()

    def buscar_lista(self):
        buscado = self.dato_buscado.get()
        if buscado:
            nodo_actual = self.primer_nodo
            encontrado = False
            while nodo_actual:
                if nodo_actual.data == buscado:
                    self.dato_encontrado.config(text=f'Valor encontrado {nodo_actual.data}')
                    encontrado = True
                    break
                nodo_actual = nodo_actual.siguiente
                if nodo_actual == self.primer_nodo:
                    break
            if not encontrado:
                self.dato_encontrado.config(text=f'Valor {buscado} no encontrado')

    def dibujar_lista(self):
        self.canvas.delete("all")
        x = self.rect_spacing
        nodo_actual = self.primer_nodo
        while nodo_actual:
            self.canvas.create_rectangle(x, self.top - self.rect_height // 2, x + self.rect_width, self.top + self.rect_height // 2, outline='black', fill='lightblue')
            self.canvas.create_text(x + self.rect_width // 2, self.top, text=nodo_actual.data, fill='black')
            x += self.rect_width + self.rect_spacing
            self.flecha(x, self.top)
            x += self.rect_spacing
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primer_nodo:
                break

    def flecha(self, x, y):
        self.canvas.create_line(x, y, x + 10, y, fill='black', arrow=tk.LAST)

    def size(self):
        cont = 0
        nodo_actual = self.primer_nodo
        while nodo_actual:
            cont += 1
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primer_nodo:
                break
        return cont

    def ultimo(self):
        nodo_actual = self.primer_nodo
        while nodo_actual.siguiente != self.primer_nodo:
            nodo_actual = nodo_actual.siguiente
        return nodo_actual

    def info(self):
        cantidad = self.size()
        self.label_cantidad.config(text=f'Cantidad de elementos: {cantidad}')
        if cantidad > 0:
            self.label_primero.config(text=f'Primero elemento: {self.primer_nodo.data}')
            self.label_ultimo.config(text=f'Ultimo elemento: {self.ultimo().data}')
        self.dato_encontrado.config(text='')

    def guardar(self):
        file_name = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')])
        if file_name:
            with open(file_name, 'w') as f:
                nodo_actual = self.primer_nodo
                while nodo_actual:
                    f.write(nodo_actual.data + '\n')
                    nodo_actual = nodo_actual.siguiente
                    if nodo_actual == self.primer_nodo:
                        break

    def abrir(self):
        file_name = filedialog.askopenfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')])
        if file_name:
            with open(file_name, 'r') as f:
                self.primer_nodo = None
                for line in f:
                    self.insertar_final_valor(line.strip())
            self.dibujar_lista()
            self.info()

    def insertar_final_valor(self, valor):
        nuevo_nodo = NodoListaSimpleAndCircular(valor)
        if not self.primer_nodo:
            self.primer_nodo = nuevo_nodo
            nuevo_nodo.siguiente = self.primer_nodo
        else:
            ultimo_nodo = self.ultimo()
            nuevo_nodo.siguiente = self.primer_nodo
            ultimo_nodo.siguiente = nuevo_nodo


class NodoListaDobleListaDobleCircular:
    def __init__(self, data):
        self.data = data
        self.siguiente = None
        self.anterior = None


class VentanaListaDoble:
    def __init__(self, ventana):
        self.ventana = ventana

        self.info_frame = tk.Frame(ventana)
        self.info_frame.pack(side=tk.RIGHT)

        self.frame_dibujo = tk.Frame(ventana)
        self.frame_dibujo.pack()

        self.frame = tk.Frame(ventana)
        self.frame.pack()

        self.search_frame = tk.Frame(ventana)
        self.search_frame.pack()

        self.canvas_width = 800
        self.canvas_height = 300
        self.rect_width = 100
        self.rect_height = 30
        self.rect_spacing = 2
        self.canvas = tk.Canvas(self.frame_dibujo, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        self.top = self.canvas_height // 2
        self.primer_nodo = None

        self.dato = tk.Entry(self.frame)
        self.dato.pack(side=tk.LEFT)

        self.boton_insertari = tk.Button(self.frame, text='Insertar al inicio', command=self.insertar_inicio)
        self.boton_insertari.pack(side=tk.LEFT)

        self.boton_ingresarf = tk.Button(self.frame, text='Insertar al final', command=self.insertar_final)
        self.boton_ingresarf.pack(side=tk.LEFT)

        self.boton_ingresarp = tk.Button(self.frame, text='Ingresar por posicion', command=self.insertar_pos)
        self.boton_ingresarp.pack(side=tk.LEFT)

        self.boton_borrari = tk.Button(self.frame, text='Borrar al inicio', command=self.borrar_inicio)
        self.boton_borrari.pack(side=tk.LEFT)

        self.boton_borrarf = tk.Button(self.frame, text='Borrar al final', command=self.borrar_final)
        self.boton_borrarf.pack(side=tk.LEFT)

        self.boton_borrarp = tk.Button(self.frame, text='Borrar por posicion', command=self.borrar_pos)
        self.boton_borrarp.pack(side=tk.LEFT)

        self.label_cantidad = tk.Label(self.info_frame, text='Lista Vacia')
        self.label_cantidad.pack()

        self.label_primero = tk.Label(self.info_frame, text='Primer Elemento: -')
        self.label_primero.pack()

        self.label_ultimo = tk.Label(self.info_frame, text='Ultimo Elemento: -')
        self.label_ultimo.pack()

        self.dato_buscado = tk.Entry(self.search_frame)
        self.dato_buscado.pack(side=tk.LEFT)

        self.boton_buscar = tk.Button(self.search_frame, text='Buscar', command=self.buscar_lista)
        self.boton_buscar.pack(side=tk.LEFT)

        self.dato_encontrado = tk.Label(self.info_frame, text='')
        self.dato_encontrado.pack()

        self.boton_guardar = tk.Button(self.info_frame, text='Guardar', command=self.guardar)
        self.boton_guardar.pack(side=tk.LEFT)

        self.boton_abrir = tk.Button(self.info_frame, text='Abrir', command=self.abrir)
        self.boton_abrir.pack(side=tk.LEFT)

    def insertar_inicio(self):
        elemento = self.dato.get()
        if elemento:
            nuevo_nodo = NodoListaDobleListaDobleCircular(elemento)
            if not self.primer_nodo:
                self.primer_nodo = nuevo_nodo
            else:
                nuevo_nodo.siguiente = self.primer_nodo
                self.primer_nodo.anterior = nuevo_nodo
                self.primer_nodo = nuevo_nodo
            self.dibujar_lista()
            self.info()
            self.dato.delete(0, tk.END)

    def insertar_final(self):
        elemento = self.dato.get()
        if elemento:
            nuevo_nodo = NodoListaDobleListaDobleCircular(elemento)
            if not self.primer_nodo:
                self.primer_nodo = nuevo_nodo
            else:
                nodo_actual = self.primer_nodo
                while nodo_actual.siguiente:
                    nodo_actual = nodo_actual.siguiente
                nodo_actual.siguiente = nuevo_nodo
                nuevo_nodo.anterior = nodo_actual
            self.dibujar_lista()
            self.info()
            self.dato.delete(0, tk.END)

    def insertar_pos(self):
        valor = self.dato.get()
        pos = tk.simpledialog.askinteger('Insertar por Posición', 'Ingrese la posición:')
        if valor and pos is not None:
            if pos <= 1:
                self.insertar_inicio()
            else:
                nuevo_nodo = NodoListaDobleListaDobleCircular(valor)
                nodo_actual = self.primer_nodo
                cont = 1
                while nodo_actual.siguiente and cont < pos - 1:
                    nodo_actual = nodo_actual.siguiente
                    cont += 1
                if nodo_actual.siguiente:
                    nuevo_nodo.siguiente = nodo_actual.siguiente
                    nodo_actual.siguiente.anterior = nuevo_nodo
                nodo_actual.siguiente = nuevo_nodo
                nuevo_nodo.anterior = nodo_actual
                self.dibujar_lista()
                self.info()
                self.dato.delete(0, tk.END)

    def borrar_inicio(self):
        if self.primer_nodo:
            if self.primer_nodo.siguiente:
                self.primer_nodo = self.primer_nodo.siguiente
                self.primer_nodo.anterior = None
            else:
                self.primer_nodo = None

            self.dibujar_lista()
            self.info()

    def borrar_final(self):
        if self.primer_nodo:
            if not self.primer_nodo.siguiente:
                self.primer_nodo = None
            else:
                nodo_actual = self.primer_nodo
                while nodo_actual.siguiente:
                    nodo_actual = nodo_actual.siguiente
                nodo_actual.anterior.siguiente = None

            self.dibujar_lista()
            self.info()

    def borrar_pos(self):
        pos = tk.simpledialog.askinteger('Eliminar por Posición', 'Ingrese la posición:')
        if pos is not None:
            if pos <= 1:
                self.borrar_inicio()
            else:
                nodo_actual = self.primer_nodo
                count = 1
                while nodo_actual and count < pos:
                    nodo_actual = nodo_actual.siguiente
                    count += 1
                if nodo_actual:
                    if nodo_actual.siguiente:
                        nodo_actual.anterior.siguiente = nodo_actual.siguiente
                        nodo_actual.siguiente.anterior = nodo_actual.anterior
                    else:
                        nodo_actual.anterior.siguiente = None
                self.dibujar_lista()
                self.info()

    def buscar_lista(self):
        buscado = self.dato_buscado.get()
        if buscado:
            nodo_actual = self.primer_nodo
            encontrado = False
            while nodo_actual:
                if nodo_actual.data == buscado:
                    self.dato_encontrado.config(text=f'Valor encontrado {nodo_actual.data}')
                    encontrado = True
                    break
                nodo_actual = nodo_actual.siguiente
            if not encontrado:
                self.dato_encontrado.config(text=f'Valor {buscado} no encontrado')

    def dibujar_lista(self):
        self.canvas.delete("all")
        x = self.rect_spacing
        nodo_actual = self.primer_nodo
        while nodo_actual:
            self.canvas.create_rectangle(x, self.top - self.rect_height // 2, x + self.rect_width,
                                         self.top + self.rect_height // 2, outline='black', fill='lightblue')
            self.canvas.create_text(x + self.rect_width // 2, self.top, text=nodo_actual.data, fill='black')
            x += self.rect_width + self.rect_spacing
            self.flecha(x, self.top + 5)
            self.flechar(x, self.top - 5)
            x += self.rect_spacing
            nodo_actual = nodo_actual.siguiente

    def flecha(self, x, y):
        self.canvas.create_line(x, y, x + 10, y, fill='black', arrow=tk.LAST)

    def flechar(self, x, y):
        self.canvas.create_line(x, y, x + 10, y, fill='black', arrow=tk.FIRST)

    def size(self):
        cont = 0
        nodo_actual = self.primer_nodo
        while nodo_actual:
            cont += 1
            nodo_actual = nodo_actual.siguiente
        return cont

    def ultimo(self):
        nodo_actual = self.primer_nodo
        while nodo_actual.siguiente:
            nodo_actual = nodo_actual.siguiente
        return nodo_actual

    def info(self):
        cantidad = self.size()
        self.label_cantidad.config(text=f'Cantidad de elementos: {cantidad}')
        if cantidad > 0:
            self.label_primero.config(text=f'Primero elemento: {self.primer_nodo.data}')
            self.label_ultimo.config(text=f'Ultimo elemento: {self.ultimo().data}')
        self.dato_encontrado.config(text='')

    def guardar(self):
        file_name = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')])
        if file_name:
            with open(file_name, 'w') as f:
                nodo_actual = self.primer_nodo
                while nodo_actual:
                    f.write(nodo_actual.data + '\n')
                    nodo_actual = nodo_actual.siguiente

    def abrir(self):
        file_name = filedialog.askopenfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')])
        if file_name:
            with open(file_name, 'r') as f:
                self.primer_nodo = None
                for line in f:
                    self.insertar_final_valor(line.strip())
            self.dibujar_lista()
            self.info()

    def insertar_final_valor(self, valor):
        nuevo_nodo = NodoListaDobleListaDobleCircular(valor)
        if not self.primer_nodo:
            self.primer_nodo = nuevo_nodo
        else:
            nodo_actual = self.primer_nodo
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nodo_actual


class VentanaListaCircularDoble:
    def __init__(self, ventana):
        self.ventana = ventana

        self.info_frame = tk.Frame(ventana)
        self.info_frame.pack(side=tk.RIGHT)

        self.frame_dibujo = tk.Frame(ventana)
        self.frame_dibujo.pack()

        self.frame = tk.Frame(ventana)
        self.frame.pack()

        self.search_frame = tk.Frame(ventana)
        self.search_frame.pack()

        self.canvas_width = 800
        self.canvas_height = 300
        self.rect_width = 100
        self.rect_height = 30
        self.rect_spacing = 2
        self.canvas = tk.Canvas(self.frame_dibujo, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        self.top = self.canvas_height // 2
        self.primer_nodo = None

        self.dato = tk.Entry(self.frame)
        self.dato.pack(side=tk.LEFT)

        self.boton_insertari = tk.Button(self.frame, text='Insertar al inicio', command=self.insertar_inicio)
        self.boton_insertari.pack(side=tk.LEFT)

        self.boton_ingresarf = tk.Button(self.frame, text='Insertar al final', command=self.insertar_final)
        self.boton_ingresarf.pack(side=tk.LEFT)

        self.boton_borrari = tk.Button(self.frame, text='Borrar al inicio', command=self.borrar_inicio)
        self.boton_borrari.pack(side=tk.LEFT)

        self.boton_borrarf = tk.Button(self.frame, text='Borrar al final', command=self.borrar_final)
        self.boton_borrarf.pack(side=tk.LEFT)

        self.boton_rotard = tk.Button(self.frame, text='Rotar Derecha', command=self.rotar_derecha)
        self.boton_rotard.pack(side=tk.LEFT)

        self.boton_rotari = tk.Button(self.frame, text='Rotar Izquierda', command=self.rotar_izquierda)
        self.boton_rotari.pack(side=tk.LEFT)

        self.label_cantidad = tk.Label(self.info_frame, text='Lista Vacia')
        self.label_cantidad.pack()

        self.label_primero = tk.Label(self.info_frame, text='Primer Elemento: -')
        self.label_primero.pack()

        self.label_ultimo = tk.Label(self.info_frame, text='Ultimo Elemento: -')
        self.label_ultimo.pack()

        self.dato_buscado = tk.Entry(self.search_frame)
        self.dato_buscado.pack(side=tk.LEFT)

        self.boton_buscar = tk.Button(self.search_frame, text='Buscar', command=self.buscar_lista)
        self.boton_buscar.pack(side=tk.LEFT)

        self.dato_encontrado = tk.Label(self.info_frame, text='')
        self.dato_encontrado.pack()

        self.boton_guardar = tk.Button(self.info_frame, text='Guardar', command=self.guardar)
        self.boton_guardar.pack(side=tk.LEFT)

        self.boton_abrir = tk.Button(self.info_frame, text='Abrir', command=self.abrir)
        self.boton_abrir.pack(side=tk.LEFT)

    def insertar_inicio(self):
        elemento = self.dato.get()
        if elemento:
            nuevo_nodo = NodoListaDobleListaDobleCircular(elemento)
            if not self.primer_nodo:
                self.primer_nodo = nuevo_nodo
                self.primer_nodo.siguiente = self.primer_nodo
                self.primer_nodo.anterior = self.primer_nodo
            else:
                ultimo_nodo = self.primer_nodo.anterior
                nuevo_nodo.siguiente = self.primer_nodo
                nuevo_nodo.anterior = ultimo_nodo
                self.primer_nodo.anterior = nuevo_nodo
                ultimo_nodo.siguiente = nuevo_nodo
                self.primer_nodo = nuevo_nodo
            self.dibujar_lista()
            self.info()
            self.dato.delete(0, tk.END)

    def insertar_final(self):
        elemento = self.dato.get()
        if elemento:
            nuevo_nodo = NodoListaDobleListaDobleCircular(elemento)
            if not self.primer_nodo:
                self.primer_nodo = nuevo_nodo
                self.primer_nodo.siguiente = self.primer_nodo
                self.primer_nodo.anterior = self.primer_nodo
            else:
                ultimo_nodo = self.primer_nodo.anterior
                nuevo_nodo.siguiente = self.primer_nodo
                nuevo_nodo.anterior = ultimo_nodo
                self.primer_nodo.anterior = nuevo_nodo
                ultimo_nodo.siguiente = nuevo_nodo
            self.dibujar_lista()
            self.info()
            self.dato.delete(0, tk.END)

    def borrar_inicio(self):
        if self.primer_nodo:
            if self.primer_nodo.siguiente == self.primer_nodo:
                self.primer_nodo = None
            else:
                ultimo_nodo = self.primer_nodo.anterior
                segundo_nodo = self.primer_nodo.anterior
                ultimo_nodo.siguiente = segundo_nodo
                segundo_nodo.anterior = ultimo_nodo
                self.primer_nodo = segundo_nodo
            self.dibujar_lista()
            self.info()

    def borrar_final(self):
        if self.primer_nodo:
            if self.primer_nodo.siguiente == self.primer_nodo:
                self.primer_nodo = None
            else:
                ultimo_nodo = self.primer_nodo.anterior
                penultimo_nodo = ultimo_nodo.anterior
                penultimo_nodo.siguiente = self.primer_nodo
                self.primer_nodo.anterior = penultimo_nodo

            self.dibujar_lista()
            self.info()

    def rotar_derecha(self):
        if self.primer_nodo:
            self.primer_nodo = self.primer_nodo.anterior
            self.dibujar_lista()
            self.info()

    def rotar_izquierda(self):
        if self.primer_nodo:
            self.primer_nodo = self.primer_nodo.siguiente
            self.dibujar_lista()
            self.info()

    def buscar_lista(self):
        buscado = self.dato_buscado.get()
        if buscado:
            nodo_actual = self.primer_nodo
            encontrado = False
            while nodo_actual:
                if nodo_actual.data == buscado:
                    self.dato_encontrado.config(text=f'Valor encontrado {nodo_actual.data}')
                    encontrado = True
                    break
                nodo_actual = nodo_actual.siguiente
                if nodo_actual == self.primer_nodo:
                    break
            if not encontrado:
                self.dato_encontrado.config(text=f'Valor {buscado} no encontrado')

    def dibujar_lista(self):
        self.canvas.delete("all")
        x = self.rect_spacing
        nodo_actual = self.primer_nodo
        while nodo_actual:
            self.canvas.create_rectangle(x, self.top - self.rect_height // 2, x + self.rect_width, self.top + self.rect_height // 2, outline='black', fill='lightblue')
            self.canvas.create_text(x + self.rect_width // 2, self.top, text=nodo_actual.data, fill='black')
            x += self.rect_width + self.rect_spacing
            self.flecha(x, self.top + 5)
            self.flechar(x, self.top - 5)
            x += self.rect_spacing
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primer_nodo:
                break

    def flecha(self, x, y):
        self.canvas.create_line(x, y, x + 10, y, fill='black', arrow=tk.LAST)

    def flechar(self, x, y):
        self.canvas.create_line(x, y, x + 10, y, fill='black', arrow=tk.FIRST)

    def size(self):
        cont = 0
        nodo_actual = self.primer_nodo
        while nodo_actual:
            cont += 1
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primer_nodo:
                break
        return cont

    def ultimo(self):
        nodo_actual = self.primer_nodo
        while nodo_actual.siguiente != self.primer_nodo:
            nodo_actual = nodo_actual.siguiente
        return nodo_actual

    def info(self):
        cantidad = self.size()
        self.label_cantidad.config(text=f'Cantidad de elementos: {cantidad}')
        if cantidad > 0:
            self.label_primero.config(text=f'Primero elemento: {self.primer_nodo.data}')
            self.label_ultimo.config(text=f'Ultimo elemento: {self.ultimo().data}')
        self.dato_encontrado.config(text='')

    def guardar(self):
        file_name = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')])
        if file_name:
            with open(file_name, 'w') as f:
                nodo_actual = self.primer_nodo
                while nodo_actual:
                    f.write(nodo_actual.data + '\n')
                    nodo_actual = nodo_actual.siguiente
                    if nodo_actual == self.primer_nodo:
                        break

    def abrir(self):
        file_name = filedialog.askopenfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')])
        if file_name:
            with open(file_name, 'r') as f:
                self.primer_nodo = None
                for line in f:
                    self.insertar_final_valor(line.strip())
            self.dibujar_lista()
            self.info()

    def insertar_final_valor(self, valor):
        nuevo_nodo = NodoListaDobleListaDobleCircular(valor)
        if not self.primer_nodo:
            self.primer_nodo = nuevo_nodo
            self.primer_nodo.siguiente = self.primer_nodo
            self.primer_nodo.anterior = self.primer_nodo
        else:
            ultimo_nodo = self.primer_nodo.anterior
            nuevo_nodo.siguiente = self.primer_nodo
            nuevo_nodo.anterior = ultimo_nodo
            self.primer_nodo.anterior = nuevo_nodo
            ultimo_nodo.siguiente = nuevo_nodo


class NodoArbolBinario:
    def __init__(self, data):
        self.data = data
        self.izquierda = None
        self.derecha = None


class VentanaArbolBinario:
    def __init__(self, ventana):
        self.ventana = ventana

        self.info_frame = tk.Frame(ventana)
        self.info_frame.pack(side=tk.RIGHT)

        self.frame_dibujo = tk.Frame(ventana)
        self.frame_dibujo.pack()

        self.frame = tk.Frame(ventana)
        self.frame.pack()

        self.search_frame = tk.Frame(ventana)
        self.search_frame.pack()

        self.canvas_width = 800
        self.canvas_height = 300
        self.rect_width = 100
        self.rect_height = 30
        self.rect_spacing = 5
        self.canvas = tk.Canvas(self.frame_dibujo, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        self.raiz = None

        self.dato = tk.Entry(self.frame)
        self.dato.pack(side=tk.LEFT)

        self.boton_insertari = tk.Button(self.frame, text='Insertar a la izquierda', command=self.insertar_izquierda)
        self.boton_insertari.pack(side=tk.LEFT)

        self.boton_insertard = tk.Button(self.frame, text='Insertar a la derecha', command=self.insertar_derecha)
        self.boton_insertard.pack(side=tk.LEFT)

        self.boton_borrari = tk.Button(self.frame, text='Borrar', command=self.eliminar)
        self.boton_borrari.pack(side=tk.LEFT)

        self.nivel = tk.Label(self.info_frame, text='Nivel del árbol: -')
        self.nivel.pack()

        self.tamanio = tk.Label(self.info_frame, text='Tamaño del árbol: 0')
        self.tamanio.pack()

        self.raiz_info = tk.Label(self.info_frame, text='El valor de la raiz: -')
        self.raiz_info.pack()

        self.dato_buscado = tk.Entry(self.search_frame)
        self.dato_buscado.pack(side=tk.LEFT)

        self.boton_buscar = tk.Button(self.search_frame, text='Buscar', command=self.buscar)
        self.boton_buscar.pack(side=tk.LEFT)

        self.dato_encontrado = tk.Label(self.info_frame, text='')
        self.dato_encontrado.pack()

        self.boton_guardar = tk.Button(self.info_frame, text='Guardar', command=self.guardar)
        self.boton_guardar.pack(side=tk.LEFT)

        self.boton_abrir = tk.Button(self.info_frame, text='Abrir', command=self.abrir)
        self.boton_abrir.pack(side=tk.LEFT)

    def insertar_izquierda(self):
        valor = self.dato.get()
        if valor:
            nuevo_nodo = NodoArbolBinario(valor)
            if not self.raiz:
                self.raiz = nuevo_nodo
            else:
                self.insertar_izquierda_metodo(self.raiz, nuevo_nodo)
            self.dibujar_arbol()
            self.info()
            self.dato.delete(0, tk.END)

    def insertar_izquierda_metodo(self, padre, nuevo_nodo):
        if padre.izquierda is None:
            padre.izquierda = nuevo_nodo
        else:
            self.insertar_izquierda_metodo(padre.izquierda, nuevo_nodo)

    def insertar_derecha(self):
        valor = self.dato.get()
        if valor:
            nuevo_nodo = NodoArbolBinario(valor)
            if not self.raiz:
                self.raiz = nuevo_nodo
            else:
                self.insertar_derecha_metodo(self.raiz, nuevo_nodo)
            self.dibujar_arbol()
            self.info()
            self.dato.delete(0, tk.END)

    def insertar_derecha_metodo(self, padre, nuevo_nodo):
        if padre.derecha is None:
            padre.derecha = nuevo_nodo
        else:
            self.insertar_derecha_metodo(padre.derecha, nuevo_nodo)

    def eliminar(self):
        valor_eliminar = self.dato.get()
        if valor_eliminar:
            self.raiz = self.eliminar_valor(self.raiz, valor_eliminar)
            self.dibujar_arbol()
            self.info()
            self.dato.delete(0, tk.END)
        else:
            self.dato_encontrado.config(text="Por favor ingresa un valor para eliminar")

    def eliminar_valor(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.data:
            nodo.izquierda = self.eliminar_valor(nodo.izquierda, valor)
        elif valor > nodo.data:
            nodo.derecha = self.eliminar_valor(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                temp = nodo.derecha
                nodo = None
                return temp
            elif nodo.derecha is None:
                temp = nodo.izquierda
                nodo = None
                return temp

            temp = self.encontrar_minimo(nodo.derecha)
            nodo.data = temp.data
            nodo.derecha = self.eliminar_valor(nodo.derecha, temp.data)
        return nodo

    @staticmethod
    def encontrar_minimo(nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def buscar(self):
        valor = self.dato_buscado.get()
        if valor:
            encontrado = self.buscar_valor(self.raiz, valor)
            if encontrado:
                self.dato_encontrado.config(text=f'Valor {valor} encontrado en el árbol')
            else:
                self.dato_encontrado.config(text=f'Valor {valor} no encontrado en el árbol')
        else:
            self.dato_encontrado.config(text='Porfavor ingresa un valor para buscar')

    def buscar_valor(self, nodo, valor):
        if nodo is None:
            return False
        elif nodo.data == valor:
            return True
        elif valor < nodo.data:
            return self.buscar_valor(nodo.izquierda, valor)
        else:
            return self.buscar_valor(nodo.derecha, valor)

    def dibujar_arbol(self):
        self.canvas.delete('all')
        if self.raiz:
            self.dibujar_nodo(self.canvas_width // 2, 50, self.raiz, self.canvas_width // 4)

    def dibujar_nodo(self, x, y, nodo, width):
        if nodo:
            self.canvas.create_rectangle(x - self.rect_width // 2, y - self.rect_height // 2, x + self.rect_width // 2,
                                         y + self.rect_height // 2, fill="lightblue", outline="black", tags="node")
            self.canvas.create_text(x, y, text=str(nodo.data), tags="node")
            if nodo.izquierda:
                self.flecha(x, y + self.rect_height // 2, x - width // 4, y + self.rect_height + self.rect_spacing)
                self.dibujar_nodo(x - width // 4, y + self.rect_height + self.rect_spacing, nodo.izquierda, width // 2)
            if nodo.derecha:
                self.flecha(x, y + self.rect_height // 2, x + width // 4, y + self.rect_height + self.rect_spacing)
                self.dibujar_nodo(x + width // 4, y + self.rect_height + self.rect_spacing, nodo.derecha, width // 2)

    def flecha(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, tags='node')

    def info(self):
        nivel = self.nivel_arbol(self.raiz)
        tamanio = self.arbol_tamanio(self.raiz)
        valor_raiz = self.raiz.data if self.raiz else '-'
        self.nivel.config(text=f'Nivel del árbol: {nivel}')
        self.tamanio.config(text=f'Tamaño del árbol: {tamanio}')
        self.raiz_info.config(text=f'Valor de la raiz: {valor_raiz}')

    def nivel_arbol(self, nodo):
        if nodo is None:
            return 0
        else:
            nivel_izquierdo = self.nivel_arbol(nodo.izquierda)
            nivel_derecha = self.nivel_arbol(nodo.derecha)

        return max(nivel_izquierdo, nivel_derecha) + 1

    def arbol_tamanio(self, nodo):
        if nodo is None:
            return 0
        else:
            return 1 + self.arbol_tamanio(nodo.izquierda) + self.arbol_tamanio(nodo.derecha)

    def guardar(self):
        filename = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')])
        if filename:
            with open(filename, 'w') as f:
                self.preorden_guardar(self.raiz, f)

    def preorden_guardar(self, nodo, file):
        if nodo:
            file.write(nodo.data + '\n')
            self.preorden_guardar(nodo.izquierda, file)
            self.preorden_guardar(nodo.derecha, file)

    def abrir(self):
        filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filename:
            with open(filename, "r") as f:
                self.raiz = None
                for line in f:
                    valor = line.strip()
                    self.insertar_desde_archivo(valor)
            self.dibujar_arbol()
            self.info()

    def insertar_desde_archivo(self, valor):
        if not self.raiz:
            self.raiz = NodoArbolBinario(valor)
        else:
            self.insertar_desde_archivo_recursivo(valor, self.raiz)

    def insertar_desde_archivo_recursivo(self, valor, nodo):
        if valor < nodo.data:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbolBinario(valor)
            else:
                self.insertar_desde_archivo_recursivo(valor, nodo.izquierda)
        elif valor > nodo.data:
            if nodo.derecha is None:
                nodo.derecha = NodoArbolBinario(valor)
            else:
                self.insertar_desde_archivo_recursivo(valor, nodo.derecha)


def pila():
    pila_window = tk.Toplevel()
    pila_window.title("Ventana Pila")
    VentanaPilaCola(pila_window, 'pila')


def cola():
    cola_window = tk.Toplevel()
    cola_window.title("Ventana Cola")
    VentanaPilaCola(cola_window, 'cola')


def lista_simple():
    lista_simple_window = tk.Toplevel()
    lista_simple_window.title("Ventana Lista Simple")
    VentanaListaSimple(lista_simple_window)


def lista_circular():
    lista_circular_window = tk.Toplevel()
    lista_circular_window.title("Ventana Lista Circular")
    VentanaListaCircular(lista_circular_window)


def lista_doble():
    lista_doble_window = tk.Toplevel()
    lista_doble_window.title("Ventana Lista Doblemente Enlazada")
    VentanaListaDoble(lista_doble_window)


def lista_doble_circular():
    lista_doble_circular_window = tk.Toplevel()
    lista_doble_circular_window.title("Ventana Lista Circular Doblemente Enlazada")
    VentanaListaCircularDoble(lista_doble_circular_window)


def arbol_binario():
    arbol_binario_window = tk.Toplevel()
    arbol_binario_window.title("Ventana Arbol Binario")
    VentanaArbolBinario(arbol_binario_window)


def main():
    principal = tk.Tk()
    principal.title("VISUALIZADOR DE ESTRUCTURAS")
    principal.configure(bg="white")

    titulo = tk.Label(principal, text="GESTION", width=15, font=("Arial Black", 40), bg="white")
    titulo.pack(padx=5, pady=5)

    boton_pila = tk.Button(principal, text="PILA", width=30, font=("Arial Black", 12), command=pila)
    boton_pila.pack(padx=5, pady=5)

    boton_cola = tk.Button(principal, text="COLA",  width=30, font=("Arial Black", 12), command=cola)
    boton_cola.pack(padx=5, pady=5)

    boton_lista_simple = tk.Button(principal, text="LISTA SIMPLE",  width=30, font=("Arial Black", 12), command=lista_simple)
    boton_lista_simple.pack(padx=5, pady=5)

    boton_lista_circular = tk.Button(principal, text="LISTA CIRCULAR",  width=30, font=("Arial Black", 12), command=lista_circular)
    boton_lista_circular.pack(padx=5, pady=5)

    boton_lista_doble = tk.Button(principal, text="LISTA DOBLE",  width=30, font=("Arial Black", 12), command=lista_doble)
    boton_lista_doble.pack(padx=5, pady=5)

    boton_lista_doble_circular = tk.Button(principal, text="LISTA DOBLE CIRCULAR",  width=30, font=("Arial Black", 12),
                                           command=lista_doble_circular)
    boton_lista_doble_circular.pack(padx=5, pady=5)

    boton_arbol_binario = tk.Button(principal, text="ARBOL BINARIO",  width=30, font=("Arial Black", 12), command=arbol_binario)
    boton_arbol_binario.pack(padx=5, pady=5)

    principal.mainloop()


if __name__ == "__main__":
    main()
