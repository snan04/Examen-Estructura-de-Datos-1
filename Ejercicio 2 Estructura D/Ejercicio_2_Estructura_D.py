import tkinter as tk
from queue import Queue

class QueueProgram:
    def __init__(self, master):
        self.master = master
        self.queue = Queue()
        self.elements = []
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Ingresar elementos a la cola:").grid(row=0, column=0)
        self.element_entry = tk.Entry(self.master)
        self.element_entry.grid(row=0, column=1)
        tk.Button(self.master, text="Encolar", command=self.enqueue).grid(row=0, column=2)
        tk.Button(self.master, text="Desencolar", command=self.dequeue).grid(row=1, column=2)
        tk.Button(self.master, text="Comprobar si esta vacio", command=self.is_empty).grid(row=2, column=2)

    def enqueue(self):
        element = int(self.element_entry.get())
        if element == 0:
            return
        self.queue.put(element)
        self.elements.append(element)
        print(f"En cola {element}. El tamano de la cola ahora es {self.queue.qsize()}.")

    def dequeue(self):
        if not self.queue.empty():
            element = self.queue.get()
            print(f"Descolado {element}. El tamano de la cola ahora es {self.queue.qsize()}.")
            return element
        else:
            print("La cola esta vacia.")

    def is_empty(self):
        if self.queue.empty():
            print("La cola esta vacia.")
            return True
        else:
            print(f"La cola tiene {self.queue.qsize()} elementos.")
            return False

root = tk.Tk()
app = QueueProgram(root)
root.mainloop()
